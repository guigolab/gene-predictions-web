<template>
    <b-row>
        <page-heading-component :header="header"></page-heading-component>
    <b-col>
    <p> command: {{result.geneid_cmd}} </p>
    <!-- <p> exec time: {{result.run_time}} -->
    <div id="output-container">{{result.output}}</div>
    <p>{{message}}</p>
    <img v-if="imageSrc" :src="imageSrc"/>
    <b-button v-if="result.output_file" @click="downloadFile(result.output_file.$oid)">Download Output File</b-button>
    <b-button v-if="result.ps" @click="downloadFile(result.ps.$oid)">Download Postscript File</b-button>
    </b-col>
        </b-row>
</template>
<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
import geneidService from "../services/GeneIdService"

export default {
    props: ['resultId'],
    data(){
        return {
            header: "geneid result page",
            result: Object,
            imageSrc: '',
            message: ''
            
        }
    },
  components: {
        PageHeadingComponent,
    },
    mounted() {
         geneidService.getResult(this.resultId).then(response => {
            this.result = response.data
            console.log(this.result)
            return response.data
        })
        .then(result => {
            if(result.jpg){
                geneidService.downloadFile(result.jpg.$oid).then(response => {
                const urlCreator = window.URL || window.webkitURL
                    this.$nextTick(() => {
                        this.imageSrc = urlCreator.createObjectURL(response.data)
                    })
                })
            }
        })
        .catch(e => {
            this.message = e
        })
    },
    methods: {
        downloadFile(fileId){
            geneidService.downloadFile(fileId).then(response => {
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data], { type: { type: 'application/postscript' }}));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'file output');
                link.click();
            })
        }
    }
}
</script>
<style>
#output-container {
    white-space: break-spaces;
    line-height: 1rem;
}
</style>