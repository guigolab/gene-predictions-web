<template>
<b-container>
    <PageHeadingComponent :header="header"></PageHeadingComponent>
    <IGVBrowserComponent v-if="tracks"></IGVBrowserComponent>
    <!-- <GenomeBrowserComponent v-if="tracks" :tracks="tracks"></GenomeBrowserComponent> -->
</b-container>
</template>

<script>

// import GenomeBrowserComponent from '../components/GenomeBrowserComponent.vue'
import IGVBrowserComponent from './IGVBrowserComponent.vue';
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
    // GenomeBrowserComponent,
    PageHeadingComponent,
    IGVBrowserComponent,
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