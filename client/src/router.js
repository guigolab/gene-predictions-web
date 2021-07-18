import Vue from "vue";
import Router from "vue-router";
// import Phylo from './views/PhyloGeneticTree.vue'
// import Genome from './views/GenomeBrowser.vue'
import SGP2Algorithm from './views/SGP2Algorithm.vue'
import SoftwareDownload from './views/SoftwareDownload.vue'
import GenePrediction from './views/GenePrediction.vue'
import GeneIdAccuracy from './views/GeneIdAccuracy.vue'
import GeneIdTraining from './views/GeneIdTraining.vue'
import SGP2 from './views/SGP2.vue'
// import Home from './views/Home.vue'
import GeneId from './views/GeneId.vue'


Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "gene-prediction",
      component: GenePrediction
    },
    {
      path: "/geneid",
      name: "geneid",
      component: GeneId
    },
    {
      path: "/geneid-accuracy",
      name: "geneid-accuracy",
      component: GeneIdAccuracy
    },
    {
      path: "/geneid-training",
      name: "geneid-training",
      component: GeneIdTraining
    },
    {
      path:"/software-download",
      name: "download-distributions",
      component: SoftwareDownload
    },
    {
      path:"/sgp2",
      name: "sgp2",
      component: SGP2
    },
    {
      path:"/sgp2-algorithm",
      name: "sgp2-algorithm",
      component: SGP2Algorithm
    }
  ]
});
