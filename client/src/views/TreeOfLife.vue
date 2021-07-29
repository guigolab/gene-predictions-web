<template>
<b-container fluid>
  <b-row>
    <b-col>
      <svg ref="svg" class="tree-svg">
    </svg>
    </b-col>
  </b-row>
  <FileListModal :files="files"></FileListModal>
</b-container>
</template>

<script>
import * as d3 from "d3";
import TaxonNodeDataService from "../services/TaxonNodeDataService";
import taxonFileService from "../services/TaxonFileService";
import FileListModal from "../components/modal/FileListModal.vue"


export default {
  name: "tree-of-life",
  data() {
    return {
        // color: null,
        clusterAttr: null,
        link: null,
        linkExtension: null,
        outerRadius: 0,
        innerRadius: 0,
        width: 0,
        data: Object,
        files: null
       
    };
  },
    components:{
    FileListModal,
  },
  mounted() {
      this.width = this.$refs.svg.clientWidth
      this.outerRadius = this.width/2
      this.innerRadius = this.outerRadius - 170
      TaxonNodeDataService.getTree(true)
            .then(response => {
                this.data = response.data[0]
                this.chart = this.createTree();
            })
            .catch(e => {
            console.log(e);
            });
//     window.addEventListener('resize', () => {
//     this.outerRadius = window.innerWidth/2
//   });
     },
  methods: {
    createTree(){
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
    
    return Object.assign(svg.node());
    },

    update(checked) {
    const t = d3.transition().duration(750);
      this.linkExtension.transition(t).attr("d", checked ? this.linkExtensionVariable : this.linkExtensionConstant);
      this.link.transition(t).attr("d", checked ? this.linkVariable : this.linkConstant);
    },
   info(component) {
     return function(d){
        component.getFiles(d.data.taxid)
     }
        },

    getFiles(taxid){
      taxonFileService.getAll(taxid)
            .then(response => {
            this.files  = response.data;
            this.$root.$emit('bv::show::modal', 'file-list-modal')
            })
            .catch(e => {
            console.log(e);
            });
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
        // console.log(d.color)

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
    color () {
      const color = d3.scaleOrdinal()
    .domain(["Sarcopterygii","Actinopterygii","Mammalia"])
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
    .selectAll("g")
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
      .text(d => d);
},
  },
  computed: {
    
    },
    output() {
    }

};
</script>

<style>
.leaves-class {
  cursor: pointer;
  font-size: 14px;
}
.tree-svg {
    width: inherit;
    height: 100%;
}
text {
  font-size: 14px;
}
/* g {
  transform: translate(-350px,-0px);
} */
</style>