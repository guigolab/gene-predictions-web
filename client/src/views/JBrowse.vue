<template>
  <div>
    <h1>I'm a Vue component</h1>
    <j-browse/>
  </div>
</template>

<script>
import '@fontsource/roboto'
// import {
//   JBrowseLinearGenomeView,
// } from '@jbrowse/react-linear-genome-view'

  import jBrowse from '../utils/jBrowse.jsx'

  export default {

    components: { 'j-browse': jBrowse},
  }
</script>