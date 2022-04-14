<template>
    <b-row>
        <b-col>
            <gene-id-form-component/>
        </b-col>
    </b-row>
</template>
<script>
import GeneIdFormComponent from '../components/GeneIdFormComponent.vue'
// import fileService from "../services/TaxonFileService";

export default {
    components: {
        GeneIdFormComponent
    },
    created() {
        if(this.$store.getters['form/params'].length === 0){
            this.$store.dispatch('form/getParams')  
        }
    }
}
</script>
