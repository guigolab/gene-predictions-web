<template>
    <b-row>
            <page-heading-component :header="header"></page-heading-component>
    <b-col>
        <FormComponent v-if="form.paramFiles.length > 0" :formOptions="form"/>
    </b-col>
        </b-row>
</template>
<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
import FormComponent from '../components/GeneIdFormComponent.vue'
import fileService from "../services/TaxonFileService";
import config from '../static-config'

export default {
    data(){
        return {
            header: "geneid web Server",
            form: {
                predictionOptions: config.resources.predictionOptions,
                outputOptions: config.resources.outputOptions,
                paramFiles: [],
            }
        }
    },
  components: {
        PageHeadingComponent,
        FormComponent
    },
    mounted() {
        fileService.getAll({type: 'param'}).then(response => {
            this.form.paramFiles = response.data
        })
    }
}
</script>
<style>

</style>