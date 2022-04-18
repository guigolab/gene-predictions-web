<template>

  <div>
    <h2>{{assemblyName}}</h2>
    <j-browse :assemblyName="assemblyName" :assembly="assembly" :tracks="tracks"/>
  </div>
</template>

<script>
import '@fontsource/roboto'
import JBrowse from '../utils/jBrowse.js'

  export default {
    props:['assemblyName'],
    components: {
       'j-browse': JBrowse
    },
    computed:{
      assembly(){
        return this.$store.getters['jbrowse/assembly']
      },
      tracks(){
        return this.$store.getters['jbrowse/tracks']
      }
    }

  }
</script>