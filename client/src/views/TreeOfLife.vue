<template>
 <b-overlay :show="show">
  <b-breadcrumb style="background-color:white">
       <b-breadcrumb-item :to="{name: 'home-page',path: '/'}">
      <b-icon icon="chevron-left" scale="1" shift-v="1" aria-hidden="true"></b-icon>
        Back
    </b-breadcrumb-item>
  </b-breadcrumb>
  <b-row>
    <b-col>
      <b-container fluid>
          <b-row>
            <b-col cols="2">
            <div v-for="name in stack"
            :key="name">
            <b-button @click="createTree(name)" pill 
            :variant="secondary">{{name}} 
            </b-button>
            </div>
            </b-col>
            <b-col cols="8">
              <h1 style="text-align:center">{{node}}</h1>
              <svg ref="svg"  class="tree-svg">
              </svg>
            </b-col>
            <b-col cols="2">
            </b-col>
          </b-row>
      </b-container>
    </b-col>
  <organism-info-modal :organism="taxon" :imageSrc="imageSrc"></organism-info-modal>
  </b-row>
</b-overlay>
</template>

<script>
import * as d3 from "d3";
import organismsDataService from "../services/OrganismsDataService";
import OrganismInfoModal from "../components/modal/OrganismInfoModal.vue"
import treeService from "../services/TreeService"


export default {
  name: "tree-of-life",
  props: ['node'],
  data() {
    return {
        clusterAttr: null,
        link: null,
        linkExtension: null,
        outerRadius: 0,
        innerRadius: 0,
        width: 0,
        data: null,
        files: null,
        show: false,
        domains: [],
        legendDomains: [],
        taxon: Object,
        stack: [],
    };
  },
    components:{
    OrganismInfoModal,
  },
  mounted() {
      this.width = this.$refs.svg.clientWidth
      this.outerRadius = this.width/2
      this.innerRadius = this.outerRadius - 170
      this.createTree(this.node)
     },
  methods: {
    createTree(name){
      const index = this.stack.indexOf(name)
      if(index > -1 && this.stack.slice(index).length > 0){
        this.stack = this.stack.slice(0,index)
      }
      this.node = name
      this.show = true
      treeService.getTree(name)
              .then(response => {
                  this.data = response.data
                  this.legendDomains = this.getDomains(this.data, []).slice(0,9)
                  this.domains = this.legendDomains.map(value => value.name)
                  this.chart = this.createD3Tree();
              })
              .catch(e => {
                console.log(e);
              });
    },
    createD3Tree(){
        const root = d3.hierarchy(this.data, d => d.children)
        .sum(d => d.children ? 0 : 1)
        .sort((a, b) => (a.value - b.value) || d3.ascending(a.data.length, b.data.length));
    var cluster = this.radialCluster();
    cluster(root);
    this.setRadius(root, root.data.length = 0, this.innerRadius / this.maxLength(root));
    this.setColor(root);
  
    const svg = d3.select(this.$refs.svg)
        .attr("viewBox", [-this.outerRadius, -this.outerRadius, this.width, this.width])
        .attr("font-family", "sans-serif")
        .attr("font-size", 10);
  
    // svg.append("g")
    //     .call(this.legend);
  
    svg.append("style").text(`
  
  .link--active {
    stroke: #000 !important;
    stroke-width: 1.5px;
  }
  
  .link-extension--active {
    stroke-opacity: .6;
  }
  
  .label--active {
    font-weight: bold;
  }
  
  `);
    this.legend(svg);
    this.linkExtension =svg.append("g")
        .attr("fill", "none")
        .attr("stroke", "#000")
        .attr("stroke-opacity", 0.25)
      .selectAll("path")
      .data(root.links().filter(d => !d.target.children))
      .join("path")
        .each(function(d) { d.target.linkExtensionNode = this; })
        .attr("d", this.linkExtensionConstant);
  
    this.link = svg.append("g")
        .attr("fill", "none")
        .attr("stroke", "#000")
      .selectAll("path")
      .data(root.links())
      .join("path")
        .each(function(d) { d.target.linkNode = this; })
        .attr("d", this.linkConstant)
        .attr("stroke", d => d.target.color);
  
    svg.append("g")
      .selectAll("text")
      .data(root.leaves())
      .join("text")
        .attr("dy", ".31em")
        .attr("transform", d => `rotate(${d.x - 90}) translate(${this.innerRadius + 4},0)${d.x < 180 ? "" : " rotate(180)"}`)
        .attr("text-anchor", d => d.x < 180 ? "start" : "end")
        .attr("class","leaves-class")
        .text(d => d.data.name.replace(/_/g, " ")).on("click", this.info(this))
        .on("mouseover", this.mouseovered(true))
        .on("mouseout", this.mouseovered(false));
    this.show = false

    return Object.assign(svg.node());
    },

    update(checked) {
    const t = d3.transition().duration(750);
      this.linkExtension.transition(t).attr("d", checked ? this.linkExtensionVariable : this.linkExtensionConstant);
      this.link.transition(t).attr("d", checked ? this.linkVariable : this.linkConstant);
    },
   info(component) {
     return function(_, d){
       if(d.data){
        component.getData(d.data)
        }
        else {
          component.getData(d)
        }
     }
    },

    getDomains(node,domains) {
      if(node.children){
        node.children.forEach(n => {
          domains = this.getDomains(n,domains)
          })
        if (node.children.length > 1)
          domains.push(node)
      }
      return domains.sort((a,b) => b.leaves-a.leaves)
    },

    getData(taxon){
      const name = taxon.name || taxon
      if(name.split(" ").length > 1){
        organismsDataService.getOrganism(name).then(response => {
          this.taxon = response.data
          this.$root.$emit('bv::show::modal', 'organism-info-modal')
        })
      }
      else {
        if(this.node == name){
          return
        }
        if(!this.stack.includes(this.node)){
          this.stack.push(this.node)
        }
        this.createTree(name)
      }
      // organismsDataService.getData()
      // taxonFileService.getAll(taxon.taxid)
      //       .then(response => {
      //       this.files  = response.data;
      //       if(this.files.length > 0) {
      //         taxonFileService.download(this.files[0].name).then(response => {
      //             const urlCreator = window.URL || window.webkitURL
      //           this.imageSrc = urlCreator.createObjectURL(response.data)
      //            this.taxon = taxon
      //           
      //         })
      //       }
      //       else {
      //         this.imageSrc= ''
      //         this.taxon = taxon
      //         this.$root.$emit('bv::show::modal', 'file-list-modal')
      //       }
           
      //       })
      //       .catch(e => {
      //       console.log(e);
      //       });
    },
    mouseovered(active) {
      return function(event, d) {
        d3.select(this).classed("label--active", active);
        d3.select(d.linkExtensionNode).classed("link-extension--active", active).raise();
        do {
        d3.select(d.linkNode).classed("link--active", active).raise();
        d = d.parent;
        }
        while (d);
      };
    },
    maxLength(d) {
      return d.data.length + (d.children ? d3.max(d.children, this.maxLength) : 0);
    },
    setRadius(d, y0, k) {
        d.radius = (y0 += d.data.length) * k;
        if (d.children) d.children.forEach(d => this.setRadius(d, y0, k));
    },
    setColor(d) {
        var name = d.data.name;
        d.color = this.color().domain().indexOf(name) >= 0 ? this.color()(name) : d.parent ? d.parent.color : null;
        if (d.children){
           d.children.forEach((item) => {
             this.setColor(item)});
          }
    },
    linkVariable(d) {
      return this.linkStep(d.source.x, d.source.radius, d.target.x, d.target.radius);
    },
    linkConstant(d) {
      return this.linkStep(d.source.x, d.source.y, d.target.x, d.target.y);
    },
    linkExtensionVariable(d) {
      return this.linkStep(d.target.x, d.target.radius, d.target.x, this.innerRadius);
    },
    linkExtensionConstant(d) {
      return this.linkStep(d.target.x, d.target.y, d.target.x, this.innerRadius);
    },
    linkStep(startAngle, startRadius, endAngle, endRadius) {
      const c0 = Math.cos(startAngle = (startAngle - 90) / 180 * Math.PI);
      const s0 = Math.sin(startAngle);
      const c1 = Math.cos(endAngle = (endAngle - 90) / 180 * Math.PI);
      const s1 = Math.sin(endAngle);
      return "M" + startRadius * c0 + "," + startRadius * s0
          + (endAngle === startAngle ? "" : "A" + startRadius + "," + startRadius + " 0 0 " + (endAngle > startAngle ? 1 : 0) + " " + startRadius * c1 + "," + startRadius * s1)
          + "L" + endRadius * c1 + "," + endRadius * s1;
    }, 
    color() {
      const color = d3.scaleOrdinal()
      .domain(this.domains)
      .range(d3.schemeCategory10)
      return color
    },
    radialCluster(){
     return d3.cluster()
    .size([360, this.innerRadius])
    .separation(() => 1)   
    },
    legend(svg){
      const g = svg
        .selectAll("g").text('').attr('fill',null).attr('stroke',null)
        .data(this.color().domain())
        .join("g")
        .attr("transform", (d, i) => `translate(${-this.outerRadius},${-this.outerRadius + i * 20})`);
        g.append("rect")
        .attr("width", 18)
        .attr("height", 18)
        .attr("fill", this.color());

        g.append("text")
        .attr("x", 24)
        .attr("y", 9)
        .attr("dy", "0.35em")
        .attr("class","legend-text")
        .text(d =>d +' ('+ this.legendDomains.find(value => value.name === d).rank +')')
        .on("click", this.info(this))
        .on("mouseover", this.mouseovered(true))
        .on("mouseout", this.mouseovered(false));
    },
  },
  computed: {
    
    },
    output() {
    }

};
</script>

<style>
.leaves-class, .legend-text {
  cursor: pointer;
  font-size: 14px;
}
.tree-svg {
    width: inherit;
    height: 100%;
    overflow: visible;
}
text {
  font-size: 14px;
}
/* g {
  transform: translate(-350px,-0px);
} */
</style>