<template>
    <b-row>
    <b-col>
        <b-card v-if="imageSrc && result.ps" :img-src="imageSrc" img-alt="ggff2ps" img-left>
            <b-row>
                <b-button-toolbar aria-label="Toolbar with button groups and dropdown menu">
                    <b-button-group class="mx-1">
                    <b-button>Download PS image</b-button>
                    <b-button>Download result</b-button>
                    </b-button-group>
                </b-button-toolbar>
            </b-row>
            <b-row>
                <b-col>
                    <b-card-text>
                        <strong>command: </strong>{{result.geneid_cmd}}
                    </b-card-text>
                </b-col>
            </b-row>
            <b-row>
                <b-col>
                    <b-card-text>
                        <strong>runnning time: </strong>{{result.run_time}}
                    </b-card-text>
                </b-col>
            </b-row>
        </b-card>
    <!-- <div class="accordion" role="tablist">
        <b-card v-if="!result.output_file" no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.result-output variant="info">Result Output</b-button>
            </b-card-header>
            <b-collapse id="result-output" accordion="my-accordion" visible role="tabpanel">
                <b-card-body id="output-container">
                    {{result.output}}
                </b-card-body>
            </b-collapse>
        </b-card>
        <b-card v-else>
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.result-output variant="info">Result Output</b-button>
            </b-card-header>
            <b-collapse id="result-output" accordion="output" visible role="tabpanel">
                <b-card-body id="output-container">
                    The result has been saved into a file as its size is over 15Mb
                    <b-button v-if="result.output_file" @click="downloadFile(result.output_file.$oid)">Download Output File</b-button>
                </b-card-body>
            </b-collapse>
        </b-card>
         <b-card v-if="imageSrc && result.ps" no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.result-images variant="info">Result Images</b-button>
            </b-card-header>
            <b-collapse id="result-images" accordion="images" role="tabpanel">
                <b-card-body>
                    <img v-if="imageSrc" :src="imageSrc"/>
                    <b-button v-if="result.ps" @click="downloadFile(result.ps.$oid)">Download Postscript File</b-button>
                </b-card-body>
            </b-collapse>
        </b-card>
        <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.result-options variant="info">Other Infos</b-button>
            </b-card-header>
            <b-collapse id="result-options" accordion="options" role="tabpanel">
                <b-card-body>
                    <p>Command: {{result.geneid_cmd}}</p>
                    <p>Species: {{result.param_species}}</p>
                    <p>Runtime: {{result.run_time}}</p>
                </b-card-body>
            </b-collapse>
        </b-card>
    </div> -->
    <!-- <p> command: {{result.geneid_cmd}} </p>
    <p> exec time: {{result.run_time}} </p>
     <div id="output-container">{{result.output}}</div>
    <p>{{message}}</p>
    <img v-if="imageSrc" :src="imageSrc"/>
    <b-button v-if="result.output_file" @click="downloadFile(result.output_file.$oid)">Download Output File</b-button>
    <b-button v-if="result.ps" @click="downloadFile(result.ps.$oid)">Download Postscript File</b-button> -->
    </b-col>
        </b-row>
</template>
<script>
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
    },
    mounted() {
         geneidService.getResult(this.resultId).then(response => {
            this.result = response.data
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
                link.setAttribute('download', 'output.ps');
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