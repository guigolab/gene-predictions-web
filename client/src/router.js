import Vue from "vue";
import Router from "vue-router";
// import Phylo from './views/PhyloGeneticTree.vue'
// import Genome from './views/GenomeBrowser.vue'
import GenePrediction from './views/GenePrediction.vue'
import Home from './views/Home.vue'
import GeneId from './views/GeneId.vue'


Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/geneid",
      name: "geneid",
      component: GeneId
    },
    {
      path: "/gene-prediction",
      name: "gene-prediction",
      component: GenePrediction
    }
  ]
});
