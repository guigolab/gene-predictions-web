<template>
<b-container class="router-container" fluid>
    <b-row>
        <b-col>
        <b-jumbotron style="margin-bottom:0px!important" header-level="4" bg-variant="white" text-variant="dark" border-variant="white">
        <template #header>{{organism.name}}</template>
        <template #lead>
            {{organism.common_name}}
        </template>
        <hr class="my-4" >
        <div style="font-size: 0.85rem !important">
            <b-link v-for="node in reverseItems(organism.ordered_lineage)" :key="node.taxid" 
            :to="{name: 'tree-of-life', params: {node: node.name}}"
            >
                {{node.name}} (<strong>{{node.rank}}</strong>)
            </b-link>
        </div>
        </b-jumbotron>
        </b-col>
    </b-row>
    <!-- <b-row>
        <b-col>
            <b-row>
                <b-col>
                    <h2>{{organism.common_name ? organism.name +' ('+ organism.common_name + ')': organism.name}}</h2>
                </b-col>
            </b-row>
            <b-row>
                <b-col style="font-size: 0.85rem">
                    <b-link v-for="node in reverseItems(organism.ordered_lineage)" :key="node.taxid" 
                    :to="{name: 'tree-of-life', params: {node: node.name}}"
                    >
                        {{node.name}} (<strong>{{node.rank}}</strong>)
                    </b-link>
                </b-col>
            </b-row>
        </b-col>
    </b-row> -->
    <!-- <b-row>
        <b-col>
            <b-card-text></b-card-text>
        </b-col>
    </b-row> -->
    <b-row>
        <b-col lg="3">
            <b-card :title="assembly.name" border-variant="info" header-tag="header" v-for="assembly in organism.genomes" :key="assembly.name">
                    <b-button variant="outline-info" @click="getAssemblyMetadata(assembly.insdc_accession)" block>Metadata</b-button>
                    <div class="accordion" role="tablist">
                        <b-card border-variant="info" no-body class="mb-1">
                            <b-card-header header-tag="header" class="p-1" role="tab">
                                <b-button variant="outline-info" block v-b-toggle="assembly.name+'fasta'">Fasta files</b-button>
                            </b-card-header>
                            <b-collapse :id="assembly.name+'fasta'" accordion="my-accordion" role="tabpanel">
                                <b-list-group>
                                    <b-list-group-item :href="assembly.fastaLocation">Download fa.gz</b-list-group-item>
                                    <b-list-group-item :href="assembly.faiLocation">Download fa.gz.fai</b-list-group-item>
                                    <b-list-group-item :href="assembly.gziLocation">Download fa.gz.gzi</b-list-group-item>
                                </b-list-group>
                            </b-collapse>
                        </b-card>
                        <b-card border-variant="info" no-body class="mb-1">
                            <b-card-header header-tag="header" class="p-1" role="tab">
                                <b-button variant="outline-info" block v-b-toggle="assembly.name+'gff'">Gff3 files</b-button>
                            </b-card-header>
                            <b-collapse :id="assembly.name+'gff'" visible accordion="my-accordion" role="tabpanel">
                                <b-card border-variant="info">
                                <b-list-group v-for="ann in getAssemblyAnnotations(assembly.name)" :key="ann.name">
                                <!-- <p>{{ann.name}}</p> -->
                                <p :id="ann.name">{{ann.name}}</p>
                                <b-tooltip :target="ann.name" triggers="hover">
                                    Evidence source: {{transformEvidences(ann.evidenceSource)}}
                                </b-tooltip>
                                <b-list-group>
                                    <b-list-group-item :href="ann.gffGzLocation">Download gff3.gz</b-list-group-item>
                                    <b-list-group-item :href="ann.tabIndexLocation">Download gff3.gz.tbi</b-list-group-item>
                                </b-list-group>
                                </b-list-group>
                            </b-card>
                            </b-collapse>
                        </b-card>
                    </div>
            </b-card>
        </b-col>
        <b-col lg="9">
            <div v-if="selectedAssembly">
                <j-browse :assemblyName="selectedAssembly"/>
            </div>
        </b-col>
    </b-row>
    <assembly-info-modal :metadata="metadata" :chromosomes="chromosomes" :biosample="biosample"/>
</b-container>
</template>

<script>
import {BCollapse,BCard,BCardHeader,BButton,BTooltip,BListGroup,BListGroupItem,BJumbotron} from 'bootstrap-vue'
import JBrowse from '../../views/JBrowseComponent.vue'
import DataPortalService from '../../services/DataPortalService'
import AssemblyInfoModal from '../modal/AssemblyInfoModal.vue'
export default {
    components: { JBrowse,BCard,BCollapse,BButton,BListGroup,BListGroupItem,BCardHeader,BTooltip, AssemblyInfoModal,BJumbotron},
    props:['organism'],
    watch:{
        organism: {
            handler(){
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
            selectedAssembly:'',
            metadataLoaded: false,
            chromosomes:[],
            biosample:null,
            metadata:null,
        }
    },
    created(){
        this.toGenomeBrowser(this.firstAssemblyName)
        // this.$root.$emit('bv::toggle::collapse', this.firstAssemblyName)
    },
    methods: {
        getAssemblyAnnotations(assemblyName){
            return this.organism.annotations.filter(ann => ann.targetGenome === assemblyName)
        },
        getMetadataFields(assembly){
            const metadata = Object.entries(assembly)
            .map(([key,value]) => 
                {
                    console.log(key)
                    console.log(typeof value === 'string')
                    if (typeof value === 'string'){
                        return [key,value]
                    }
                }).filter(entry => entry)
            console.log(metadata)
            return Object.fromEntries(metadata)
            // return {chromosomes,biosample,...assembly}
        },
        reverseItems(items) {
            return items.slice().reverse();
        },
        getAssemblyMetadata(accession){
            this.$store.dispatch('portal/showLoading')
            DataPortalService.getAssemblyMetadata(accession)
            .then(response => {
                if(response.data && response.data.assemblies){
                    this.chromosomes = response.data.assemblies[0].assembly.chromosomes
                    this.biosample = response.data.assemblies[0].assembly.biosample
                    this.metadata = this.getMetadataFields(response.data.assemblies[0].assembly)
                    this.$store.dispatch('portal/hideLoading')
                    this.$bvModal.show('assembly-info-modal')
                }
                this.$store.dispatch('portal/hideLoading')
                return null
            })
            .catch(e => {
                console.log(e)
                this.$store.dispatch('portal/hideLoading')
            })
        },
        transformEvidences(evidenceString){
            const values = evidenceString.split('.')
            const taxIdToName = this.organism.ordered_lineage.filter(node => node.taxid === values[1])
            if(taxIdToName.length){
                return values[0]+' '+values[2]+' '+taxIdToName[0].name
            }
            return evidenceString
            
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