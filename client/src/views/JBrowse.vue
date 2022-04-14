<template>
  <div>
    <j-browse/>
  </div>
</template>

<script>
import '@fontsource/roboto'
// import {ReactInVue} from 'vuera'
import JBrowse from '../utils/jBrowse.js'

// const JBrowse = ReactInVue(View)
// import {
//   JBrowseLinearGenomeView,
// } from '@jbrowse/react-linear-genome-view'



  export default {
    deta(){
      return{
        state:null
      }
    },
    components: {
       'j-browse': JBrowse
    },

  }
</script>
