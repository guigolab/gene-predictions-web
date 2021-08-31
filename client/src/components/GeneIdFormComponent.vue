<template>
<div>
    <b-container>
        <b-row>
            <b-col>
                <b-form enctype="multipart/form-data" v-if="show" @submit="onSubmit" @reset="onReset">
                    <b-form-group label="Try it out" label-size="lg"
                    label-class="font-weight-bold pt-0"
                    class="mb-0">
                        <label for="textarea-fasta">Paste your FASTA sequence here</label>
                        <b-form-textarea id="textarea-fasta" v-model="form.fastaText" :state="fastaForm" :disabled="Boolean(form.fastaFile)" rows="3" max-rows="6"
                        >
                        </b-form-textarea>
                        <label for="fasta-file">search a FASTA file to process</label>
                        <b-form-file
                        @change="onFileChange"
                        :disabled="Boolean(form.fastaText)"
                        accept=".fasta"
                        id="fasta-file"
                        v-model="form.fastaFile"
                        :state="fastaForm"
                        drop-placeholder="Drop here..."
                        >
                        </b-form-file>
                        <b-button @click="form.fastaFile = null">Reset via v-model</b-button>
                        <label for="textarea-gff">Paste your GFF evidences here (Field separator: tab)</label>
                        <b-form-textarea
                        :disabled="Boolean(form.gffFile)"
                        id="textarea-gff"
                        v-model="form.gffText"
                        rows="3"
                        max-rows="6"
                        :state="gffForm"
                        >
                        </b-form-textarea>
                        <label for="gff-file">search a GFF file to process</label>
                        <b-form-file
                        :disabled="Boolean(form.gffText)"
                        accept=".gff, .gff3"
                        id="gff-file"
                        v-model="form.gffFile"
                        :state="gffForm"
                        drop-placeholder="Drop here..."
                        >
                        </b-form-file>
                        <b-button @click="form.gffFile = null">Reset via v-model</b-button>
                    </b-form-group>
                    <b-form-group label="Prediction options"
                    label-class="font-weight-bold pt-0"
                    class="mb-0">
                            <label for="param-select">select a parameter file from an organism</label>
                            <b-form-select id="param-select"
                                v-model="form.selectedParam"
                                class="mb-3"
                                :options="formOptions.paramFiles"
                            >
                            </b-form-select>
                            <label for="predmode-checkbox">select a prediction mode </label>
                            <b-form-checkbox-group
                                id="predmode-checkbox"
                                v-model="form.selectedMode"
                                :options="formOptions.predictionOptions.predictionModes"
                                :aria-describedby="ariaDescribedby"
                            ></b-form-checkbox-group>
                            <label for="dna-checkbox">DNA strands </label>
                            <b-form-checkbox-group
                            id="dna-checkbox"
                                v-model="form.selectedStrands"
                                :options="formOptions.predictionOptions.dnaStrands"
                                :aria-describedby="ariaDescribedby"
                            ></b-form-checkbox-group>
                        <b-form-group>
                            <b-form-checkbox
                            id="graph-rap"
                            v-model="form.graphicalRap"
                            value="true"
                            unchecked-value="false"
                            name="graph-rap"
                            switch>
                            Do you want a graphical representation of the predictions ?
                            (it might be time consuming depending on the size of the sequence)
                            </b-form-checkbox>
                        </b-form-group>
                    </b-form-group>
                    <b-form-group label="Output options"
                    label-class="font-weight-bold pt-0"
                    class="mb-0">
                        <label for="output-select">select an output format</label>
                        <b-form-select id="output-select"
                            v-model="form.outputOption"
                            class="mb-3"
                            :options="formOptions.outputOptions.outputFormat">
                        </b-form-select>
                        <label for="signals-checkbox">Signals </label>
                        <b-form-checkbox-group
                            id="signals-checkbox"
                            v-model="form.selectedOptions"
                            :options="formOptions.outputOptions.signals"
                            :aria-describedby="ariaDescribedby">
                            </b-form-checkbox-group>
                        <label for="exons-checkbox">Exons </label>
                        <b-form-checkbox-group
                        id="exons-checkbox"
                            v-model="form.selectedOptions"
                            :options="formOptions.outputOptions.exons"
                            :aria-describedby="ariaDescribedby">
                        </b-form-checkbox-group>
                    </b-form-group>
                    <div class="buttons-form">
                    <b-button type="reset" variant="danger">Reset</b-button>
                    <b-button type="submit" variant="primary" style="float: inline-end">Submit</b-button>
                    </div>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
    <div id="output-container">{{output}}</div>
    <img v-if="imageSrc" :src="imageSrc"/>
    <b-button v-if="psLink" :href="psLink">Download Postscript File</b-button>
    </div>
</template>
<script>
import geneidService from "../services/GeneIdService"
// import http from "../http-geneid"

export default {
    name: "gene-id-form",
    props: ['formOptions'],
    data () {
        return {
            form : {
            fastaText: '',
            fastaFile: null,
            gffText: '',
            gffFile: null,
            selectedParam: '',
            selectedStrands: '',
            selectedMode: '',
            selectedOptions: [],
            outputOption: '', //geneid as default value
            graphicalRap: true
            },
            show: true,
            imageSrc: '',
            output: '',
            psLink:''
            
            // fastaFileURI:'',
            
            
        }
    },
    mounted(){
        this.form.selectedParam = this.formOptions.paramFiles[0].value
        this.form.selectedMode = this.formOptions.predictionOptions.predictionModes[0].value
    },
    computed: {
        fastaForm(){
            return this.form.fastaText || this.form.fastaFile
        },
        gffForm(){
            return this.form.gffText || this.form.gffFile
        }
    },
    methods: {
    validateForm(){},
      onSubmit(event) {
        event.preventDefault()
        var formData = new FormData()
        for (const [key, value] of Object.entries(this.form)) {
            console.log(value)
            if (value){
                formData.append(key,value)
            }
        }
        geneidService.sendForm(formData)
        .then(response => {
            // response contains a geneid model
            const geneId = response.data
            this.output = geneId.output
            if(geneId.jpg){
                geneidService.getParams(geneId.jpg.$oid).then(response => {
                    const urlCreator = window.URL || window.webkitURL
                    this.imageSrc = urlCreator.createObjectURL(response.data)
                })
                //send image as attachment 
                // and create download button for ps image download
            }
            if(geneId.ps){
                  geneidService.getParams(geneId.ps.$oid).then(response => {
                    console.log(response)
                    this.psLink = window.URL.createObjectURL(new Blob([response.data], { type: { type: 'application/postscript' }}));
                    // const link = document.createElement('a');
                    // link.href = url;
                    // link.setAttribute('download', 'postscript file output');
                    // link.click();
                })
            }
            // this.imageSrc = response.data[2]
            // console.log(response)
            geneidService.delete(geneId._id.$oid).then(response=>{
                console.log(response)
            })
        })
      },
       onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form = null
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
      onFileChange(e) {
        if(e.target.id === 'fasta-file'){
            this.form.fastaFile = e.target.files[0]
        } 
        if (e.target.id === 'gff-file'){
            this.form.gffFile = e.target.files[0]
        }
      },    
    }
}
</script>
<style>
.buttons-form{
    display: block;
}
#output-container {
    white-space: break-spaces;
    line-height: 1rem;
}
</style>