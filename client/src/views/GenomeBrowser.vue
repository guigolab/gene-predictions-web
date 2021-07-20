<template>
<b-container>
    <page-heading-component :header="header"></page-heading-component> 
    <GenomeBrowserComponent v-if="tracks" :tracks="tracks"></GenomeBrowserComponent>
</b-container>
</template>

<script>
import GenomeBrowserComponent from '../components/GenomeBrowserComponent.vue'
import PageHeadingComponent from '../components/PageHeadingComponent.vue';
import taxonFileService from "../services/TaxonFileService";


export default {
  name: "genome-page",
    data(){
        return {
            tracks: null,
            header: {
                title: null
            }
        }
    },
  components: {
      GenomeBrowserComponent,
    PageHeadingComponent,
  },

 beforeRouteEnter (to, from, next) {
    taxonFileService.getTracks(to.params.fileName)
    .then(response => {
        next(vm => {vm.tracks = response.data
         vm.header.title= to.params.fileName})
    })
    // getPost(to.params.id, (err, post) => {
    //   next(vm => vm.setData(err, post))
    // })
    // console.log("parent")
  },
  methods: {
      setTracks (tracks) {
          console.log("father")
            this.tracks = tracks
      }
  }
};
</script>

<style>
/* #canvas {
    width: inherit;
    height: inherit;
} */
</style>