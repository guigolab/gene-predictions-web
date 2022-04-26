<template>
  <div>
    {{assemblyName}}
    <j-browse :assemblyName="assemblyName" :defaultSession="defaultSession" :assembly="assembly" :tracks="tracks"/>
  </div>
</template>

<script>
// import '@fontsource/roboto'
import JBrowse from '../utils/jBrowse.js'

  export default {
    props:['assemblyName'],
    watch:{
      assemblyName(){
        this.$forceUpdate()
      }
    },
    components: {
       'j-browse': JBrowse
    },
    computed:{
      assembly(){
        return this.$store.getters['jbrowse/assembly']
      },
      tracks(){
        return this.$store.getters['jbrowse/tracks']
      },
      defaultSession(){
        return this.$store.getters['jbrowse/defaultSession']
      }
    }

  }
</script>