<template>
    <b-container>
            <page-heading-component :header="header"></page-heading-component>
    <b-row>
    <b-col>
        <FormComponent v-if="form.paramFiles.length > 0" :formOptions="form"/>
    </b-col>
        </b-row>
    </b-container>
</template>
<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
import FormComponent from '../components/GeneIdFormComponent.vue'
import geneidService from "../services/GeneIdService";
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
        geneidService.getParams().then(response => {
            this.form.paramFiles = response.data[0]
        })
    }
}
</script>
<style>

</style>