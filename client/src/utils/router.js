import Vue from "vue";
import Router from "vue-router";
import HomePage from '../views/HomePage.vue'



Vue.use(Router);

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home-page",
      component: HomePage
    },
    // {
    //   path:"/genome-browser/:fileName",
    //   name:"genome-browser",
    //   props: true,
    //   component: Genome
    // },
    {
      path: '/tree-of-life',
      redirect: {name: 'tree-of-life', params: {node: 'Eukaryota'}}
    },
    // {
    //   path: '/jbrowse/:assemblyName',
    //   name: 'jbrowse',
    //   component: () => import(/* webpackPrefetch: true */ '../views/JBrowse.vue'),
    //   props:true
      
    // },
    {
      path: "/organisms/:name",
      name: "organism-details",
      props: true,
      component: () => import(/* webpackPrefetch: true */ '../views/OrganismDetailsPage.vue')
    },
    {
      path: "/tree-of-life/:node",
      name: "tree-of-life",
      props: true,
      component: () => import(/* webpackPrefetch: true */ '../views/TreeOfLife.vue')
    },
    {
      path: "/geneid-form",
      name: "geneid-form",
      component: () => import(/* webpackPrefetch: true */ '../views/GeneIdFormPage.vue')
    },
    {
      path: "/geneid-result/:resultId",
      name: "geneid-result",
      props: true,
      component: () => import(/* webpackPrefetch: true */ '../views/GeneIdResultPage.vue')
    }    
  ]
});
