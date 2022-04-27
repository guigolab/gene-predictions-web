<template>
  <div v-if="visible">
    <j-browse :assemblyName="assemblyName" :defaultSession="defaultSession" :assembly="assembly" :tracks="tracks"/>
  </div>
</template>

<script>
// import '@fontsource/roboto'
import JBrowse from '../utils/jBrowse.js'

  export default {
    props:['assemblyName'],
    data(){
      return {
        visible:true
      }
    },
    watch:{
      assemblyName(){
        this.visible=!this.visible
        this.visible=!this.visible
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