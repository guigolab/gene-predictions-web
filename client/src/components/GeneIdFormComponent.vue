<template>
<b-overlay :show="loading" rounded="sm">
    <b-container>
        <b-row>
            <b-col>
                <b-form enctype="multipart/form-data" novalidate v-if="show" @submit="onSubmit" @reset="onReset">
                    <b-form-group label="Try it out" label-size="lg"
                    label-class="font-weight-bold pt-0"
                    class="mb-0"
                    label-cols-lg="3"
                    >
                        <b-form-row class="row-field">
                            <b-col cols="4">
                        <label for="textarea-fasta">Paste your FASTA sequence here</label>
                            </b-col>
                            <b-col>
                        <b-form-textarea id="textarea-fasta"
                        :required="!Boolean(form.fastaText) && !Boolean(form.fastaFile)"
                        v-model="form.fastaText" :state="fastaFileSize" :disabled="Boolean(form.fastaFile)" rows="3"
                        >
                        </b-form-textarea>
                            <b-form-invalid-feedback v-if="form.fastaText" :state="fastaFileSize">Maximum sequence size for plots: 150,000 bps</b-form-invalid-feedback>
                            </b-col>
                        </b-form-row>
                        <b-form-row class="row-field">
                            <b-col cols="4">
                        <label for="fasta-file">search a FASTA file to process</label>
                            </b-col>
                            <b-col>
                        <b-form-file
                        @change="onFileChange"
                        :required="!Boolean(form.fastaText) && !Boolean(form.fastaFile)"
                        :disabled="Boolean(form.fastaText)"
                        accept=".fasta, .fa"
                        id="fasta-file"
                        :state="fastaFileSize"
                        v-model="form.fastaFile"
                        drop-placeholder="Drop fasta file here..."
                        >
                        </b-form-file>
                        <b-form-invalid-feedback v-if="form.fastaFile" :state="fastaFileSize">Maximum sequence size for plots: 150,000 bps</b-form-invalid-feedback>
                            </b-col>
                        </b-form-row>
                        <b-form-row class="row-field">
                            <b-col cols="4">
                        <label for="textarea-gff">Paste your GFF evidences here (Field separator: tab)</label>
                            </b-col>
                            <b-col>
                        <b-form-textarea
                        :disabled="Boolean(form.gffFile)"
                        id="textarea-gff"
                        v-model="form.gffText"
                        rows="3"
                        >
                        </b-form-textarea>
                            </b-col>
                        </b-form-row>
                        <b-form-row class="row-field">
                            <b-col cols="4">
                        <label for="gff-file">search a GFF file to process</label>
                            </b-col>
                            <b-col>
                        <b-form-file
                        :disabled="Boolean(form.gffText)"
                        accept=".gff, .gff3"
                        id="gff-file"
                        v-model="form.gffFile"
                        drop-placeholder="Drop gff file here..."
                        >
                        </b-form-file>
                            </b-col>
                        </b-form-row>
                    </b-form-group>
                    <b-form-group label="Prediction options"
                    label-class="font-weight-bold pt-0"
                    class="mb-0"
                    label-cols-lg="3"
                   >
                            <b-form-row class="row-field">
                                <b-col cols="4">
                            <label for="param-select">select a parameter file from an organism</label>
                                </b-col>
                                <b-col>

                            <b-form-select id="param-select"
                                v-model="form.selectedParam"
                                class="mb-3"
                                :options="formOptions.paramFiles"
                                value-field="name"
                                text-field="organism"
                            >
                            </b-form-select>
                                </b-col>
                            </b-form-row>
                            <b-form-row class="row-field">
                                <b-col cols="4">
                            <label for="predmode-checkbox">select a prediction mode </label>
                                </b-col>
                                <b-col>
                            <b-form-checkbox-group
                                id="predmode-checkbox"
                                v-model="form.selectedMode"
                                :options="formOptions.predictionOptions.predictionModes"
                                :aria-describedby="ariaDescribedby"
                            ></b-form-checkbox-group>
                                </b-col>
                            </b-form-row>
                            <b-form-row class="row-field">
                                <b-col cols="4">
                            <label for="dna-checkbox">DNA strands </label>
                                </b-col>
                                <b-col>
                            <b-form-checkbox-group
                            id="dna-checkbox"
                                v-model="form.selectedStrands"
                                :options="formOptions.predictionOptions.dnaStrands"
                                :aria-describedby="ariaDescribedby"
                            ></b-form-checkbox-group>
                                </b-col>
                            </b-form-row>
                            <b-form-row class="row-field">
                                <b-col>
                            <b-form-checkbox
                            id="graph-rap"
                            v-model="form.graphicalRap"
                            :state="graphicalRap"
                            name="graph-rap"
                            switch>
                            Do you want a graphical representation of the predictions ?
                            (it might be time consuming depending on the size of the sequence)
                            </b-form-checkbox>
                            <b-form-invalid-feedback :state="graphicalRap">The output format must be GFF</b-form-invalid-feedback>
                                </b-col>
                            </b-form-row>
                    </b-form-group>
                    <b-form-group label="Output options"
                    label-class="font-weight-bold pt-0"
                    class="mb-0"
                    label-cols-lg="3">
                    <b-form-row class="row-field">
                        <b-col cols="4">
                        <label for="output-select">select an output format</label>
                        </b-col>
                        <b-col>
                        <b-form-select id="output-select"
                            v-model="form.outputOption"
                            class="mb-3"
                            :options="formOptions.outputOptions.outputFormat">
                        </b-form-select>
                        </b-col>
                    </b-form-row>
                    <b-form-row class="row-field">
                        <b-col cols="4">
                        <label for="signals-checkbox">Signals </label>
                        </b-col>
                        <b-col>
                        <b-form-checkbox-group
                            id="signals-checkbox"
                            v-model="form.signals"
                            :options="formOptions.outputOptions.signals"
                            :aria-describedby="ariaDescribedby">
                            </b-form-checkbox-group>
                        </b-col>
                    </b-form-row>
                    <b-form-row class="row-field">
                        <b-col cols="4">
                        <label for="exons-checkbox">Exons</label>
                        </b-col>
                        <b-col>
                        <b-form-checkbox-group
                        id="exons-checkbox"
                            v-model="form.exons"
                            :options="formOptions.outputOptions.exons"
                            :aria-describedby="ariaDescribedby">
                        </b-form-checkbox-group>
                        </b-col>
                    </b-form-row>
                    </b-form-group>
                    <div class="buttons-form">
                        <b-button type="reset" variant="danger">Reset</b-button>
                        <b-button :disabled="!fastaSubmitted" type="submit" variant="primary" style="float: inline-end">Submit</b-button>
                    </div>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
    </b-overlay>
</template>
<script>
import geneidService from "../services/GeneIdService"

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
            exons: [],
            signals: [],
            selectedOptions: [],
            outputOption: '-G', //geneid as default value
            graphicalRap: true
            },
            show: true,
            loading: false,
            fileSize : 0,  
        }
    },
    mounted(){
        this.form.selectedParam = this.formOptions.paramFiles[0].name
        this.form.selectedMode = this.formOptions.predictionOptions.predictionModes[0].value
    },
    computed: {
        fastaSubmitted(){
            return this.form.fastaText || this.form.fastaFile
        },
        fastaFileSize(){
            return this.graphicalRap && this.form.fastaFile ? this.fileSize < 15000000 ? true : false : null
        },
        fastaTextSize(){
            return this.graphicalRap && this.form.fastaText ? new Blob([this.form.fastaText]).size < 15000000 ? true : false : null

        },
        graphicalRap(){
            // return this.form.graphicalRap ? (this.form.outputOption === '-G' ? true : false) : null
            return this.form.graphicalRap ? this.form.outputOption === '-G' ? true: false : null
        },
        // checkSize(){
        //     return this.graphicalRap ? this.fastaSubmitted && (this.fileSize < 15000000 || new Blob([this.form.fastaText]).size < 15000000) ? true : false : null
        // },

        

    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        // this.validateForm()
        
        this.loading = true
        var formData = new FormData()
        if(this.form.exons.length > 0 || this.form.signals.length > 0){
            this.form.selectedOptions = this.form.exons.concat(this.form.signals)
            this.form.exons = []
            this.form.signals = []
            console.log(this.form.selectedOptions)
        }
        for (const [key, value] of Object.entries(this.form)) {
            if (value){
                formData.append(key,value)
            }
        }
        geneidService.sendForm(formData)
        .then(response => {
            // response contains a geneid model object
            const geneId = response.data
            console.log(geneId)
            this.$router.push({ name: 'geneid-result', params: { resultId: geneId._id.$oid }})
        })
      },
    //   validateForm(){
    //       if (this.form.fastaText || this.form.fastaFile){
    //           if(this.form.graphicalRap){

    //           }
    //       }else{

    //           return false
    //       }
    //       if(this.form.graphicalRap && (this.fileSize < 15000000 || new Blob([this.form.fastaText]).size < 15000000)){

    //       }
    //   },
       onReset(event) {
        event.preventDefault()
        // Reset our form values
        Object.keys(this.form).forEach(key => {
            if (key !== 'outputOption'){
                if(Array.isArray(this.form[key])){
                    this.form[key] = []
                }else{
                    this.form[key] = null
                }
            }
        })
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
      onFileChange(e) {
        if(e.target.id === 'fasta-file'){
            console.log(e)
            this.fileSize = e.target.files[0].size
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
.row-field {
    margin-top: 15px;
    margin-bottom: 15px;
}
</style>