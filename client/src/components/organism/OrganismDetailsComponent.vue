<template>
<b-container class="router-container" fluid>
    <b-row>
        <b-col>
            <b-row>
                <b-col>
                    <h2>{{organism.common_name ? organism.name +' ('+ organism.common_name + ')': organism.name}}</h2>
                </b-col>
            </b-row>
            <b-row>
                <b-col style="font-size: 0.85rem">
                    <b-link v-for="node in reverseItems(organism.taxon_lineage)" :key="node.taxid" 
                    :to="{name: 'tree-of-life', params: {node: node.name}}"
                    >
                        {{node.name}} (<strong>{{node.rank}}</strong>)
                    </b-link>
                </b-col>
            </b-row>
        </b-col>
    </b-row>
    <b-row>
        <b-col lg="3">
            <div class="accordion" role="tablist">
                <b-card bg-variant="light" no-body class="mb-1" v-for="assembly in organism.genomes" :key="assembly.name">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button variant="info" block v-b-toggle="assembly.name">{{assembly.name}}</b-button>
                    </b-card-header>
                    <b-collapse :id="assembly.name" accordion="my-accordion" role="tabpanel">
                        <b-card-body>
                            <p>Fasta files of {{assembly.name}}</p>
                            <b-list-group>
                                <b-list-group-item :href="assembly.fastaLocation">Download fa.gz</b-list-group-item>
                                <b-list-group-item :href="assembly.faiLocation">Download fa.gz.fai</b-list-group-item>
                                <b-list-group-item :href="assembly.gziLocation">Download fa.gz.gzi</b-list-group-item>
                            </b-list-group>
                        </b-card-body>
                        <b-card-body>
                            <p>Gff3 files of {{assembly.name}}</p>
                            <b-list-group v-for="ann in getAssemblyAnnotations(assembly.name)" :key="ann.name">
                                <!-- <p>{{ann.name}}</p> -->
                                <p>{{ann.name}}</p>
                                <b-icon-question :id="assembly.name+'annotation'"/>
                                <b-tooltip :target="assembly.name+'annotation'" triggers="hover">
                                    Evidence source: {{transformEvidences(ann.evidenceSource)}}
                                </b-tooltip>
                                <b-list-group>
                                    <b-list-group-item :href="ann.gffGzLocation">Download gff3.gz</b-list-group-item>
                                    <b-list-group-item :href="ann.tabIndexLocation">Download gff3.gz.tbi</b-list-group-item>
                                </b-list-group>
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>
            </div>
        </b-col>
        <b-col lg="9">
            <div v-if="selectedAssembly">
                <j-browse :assemblyName="selectedAssembly"/>
            </div>
        </b-col>
    </b-row>
</b-container>
</template>

<script>
import {BCollapse,BCard,BCardHeader,BCardBody,BButton,BTooltip,BIconQuestion,BListGroup,BListGroupItem} from 'bootstrap-vue'
import JBrowse from '../../views/JBrowseComponent.vue'
export default {
    components: { JBrowse,BCard,BCollapse,BButton,BListGroup,BListGroupItem,BCardHeader,BCardBody,BTooltip,BIconQuestion},
    props:['organism'],
    watch:{
        organism: {
            handler(){
                this.$root.$emit('bv::toggle::collapse', this.firstAssemblyName)
                this.toGenomeBrowser(this.firstAssemblyName)
            },
            deep:true
        }
    },
    computed:{
        firstAssemblyName(){
            return this.organism.genomes[0].name
        }
    },
    data(){
        return {
            selectedAssembly:''
        }
    },
    mounted(){
        this.$root.$emit('bv::toggle::collapse', this.firstAssemblyName)
        this.$root.$on('bv::collapse::state', (collapseId, isJustShown) => {
            if(isJustShown){
                this.toGenomeBrowser(collapseId)
            }
        })
    },
    methods: {
        getAssemblyAnnotations(assemblyName){
            return this.organism.annotations.filter(ann => ann.targetGenome === assemblyName)
        },
        reverseItems(items) {
            return items.slice().reverse();
        },
        transformEvidences(evidenceString){
            const values = evidenceString.split('.')
            const taxIdToName = this.organism.taxon_lineage.filter(node => node.taxid == values[1])[0].name
            return values[0]+' '+values[2]+' '+taxIdToName
        },
        toGenomeBrowser(assemblyName){
            const annotations = this.getAssemblyAnnotations(assemblyName)
            const assemblyObj = this.organism.genomes.filter(el => el.name === assemblyName)[0] || this.organism.genomes[0]
            const sessionTracks = []
            const assemblyView = {
              name : assemblyName,
              sequence: {
                type: 'ReferenceSequenceTrack',
                trackId: assemblyName,
                adapter: {
                  type: 'BgzipFastaAdapter',
                  fastaLocation: {
                    uri: assemblyObj.fastaLocation,
                    locationType: 'UriLocation',
                  },
                  faiLocation: {
                    uri: assemblyObj.faiLocation,
                    locationType: 'UriLocation',
                  },
                  gziLocation: {
                    uri: assemblyObj.gziLocation,
                    locationType: 'UriLocation',
                  },
                },
              },
              aliases: [assemblyName]
            }
            sessionTracks.push({
              type: 'ReferenceSequenceTrack',
              configuration: assemblyName,
              displays: [
                {
                  type: 'LinearReferenceSequenceDisplay',
                  configuration:
                    `${assemblyName}-LinearReferenceSequenceDisplay`,
                },
              ],
            })
            this.$store.commit('jbrowse/setAssembly', assemblyView)
            const tracks = []
            annotations.forEach(ann => {
              tracks.push({
                type: 'FeatureTrack',
                trackId: ann.name,
                name: ann.name,
                assemblyNames: [assemblyName],
                category: ['Annotation'],
                adapter: {
                  type: 'Gff3TabixAdapter',
                gffGzLocation: {
                  uri: ann.gffGzLocation,
                  locationType: 'UriLocation',
                  },
                index: {
                  location: {
                    uri: ann.tabIndexLocation,
                    locationType: 'UriLocation'
                  }
                }
                }
              })
              sessionTracks.push({
                type: 'FeatureTrack',
                configuration: ann.name,
                displays: [
                  {
                    type: 'LinearBasicDisplay',
                    configuration: `${ann.name}-LinearBasicDisplay`,
                  },
                ]
              })
            })
            this.$store.commit('jbrowse/setTracks', tracks)
               const defaultSession = {
                name: 'new session',
                view: {
                  id: 'linearGenomeView',
                  type: 'LinearGenomeView',
                  tracks: sessionTracks
                }
              }
            this.$store.commit('jbrowse/setDefaultSession', defaultSession)
            this.selectedAssembly = assemblyName
        } 
    }
}

</script>
<style>
.tab-element{
    padding-top: 10px;
    padding-bottom: 10px;
    min-height: 66vh;
}

#species-image{
margin-right: 10px;
}
.map-container{
    width: 100%;
    height: 100%;
    min-height: 150px

}
</style>