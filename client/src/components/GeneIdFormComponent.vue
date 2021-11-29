<template>
<b-overlay :show="loading" rounded="sm">
    <b-container>
        <b-row>
            <b-col>
                <b-button :disabled="demoLoaded" @click="setDemoForm()">Load Demo</b-button>
                <b-form enctype="multipart/form-data" novalidate v-if="show" @submit="onSubmit" @reset="onReset">
                <b-card class="card-container" bg-variant="light">
                    <b-form-group label="Data input" label-size="lg"
                    label-class="font-weight-bold pt-0"
                    class="mb-0"
                    label-cols-lg="3"
                    >
                         <b-form-group
                            label="Paste your FASTA sequence here:"
                            label-for="textarea-fasta"
                            label-cols-sm="3"
                            label-align-sm="right"
                        >
                        <b-form-textarea id="textarea-fasta"
                        class="pt-2"
                        :required="!Boolean(form.fastaText) && !Boolean(form.fastaFile)"
                        v-model="form.fastaText" :state="fastaFileSize" :disabled="Boolean(form.fastaFile)" rows="5"
                        >
                        </b-form-textarea>
                            <b-form-invalid-feedback v-if="form.fastaText" :state="fastaFileSize">Maximum sequence size for plots: 150,000 bps</b-form-invalid-feedback>
                         </b-form-group>
                        <b-form-group
                        label="Upload a FASTA file to process:"
                        label-for="fasta-file"
                        label-cols-sm="3"
                        label-align-sm="right"
                        >
                        <b-form-file
                        @change="onFileChange"
                        class="pt-2"
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
                        </b-form-group>
                        <b-form-group
                        label="Paste your GFF evidences here (Field separator: tab):"
                        label-for="textarea-gff"
                        label-cols-sm="3"
                        label-align-sm="right"
                        >
                        <b-form-textarea
                        class="pt-2"
                        :disabled="Boolean(form.gffFile)"
                        id="textarea-gff"
                        v-model="form.gffText"
                        rows="5"
                        >
                        </b-form-textarea>
                        </b-form-group>
                         <b-form-group
                        label="Upload a GFF file to process:"
                        label-for="gff-file"
                        label-cols-sm="3"
                        label-align-sm="right"
                        >
                        <b-form-file
                        class="pt-2"
                        :disabled="Boolean(form.gffText)"
                        accept=".gff, .gff3"
                        id="gff-file"
                        v-model="form.gffFile"
                        drop-placeholder="Drop gff file here..."
                        >
                        </b-form-file>
                         </b-form-group>
                    </b-form-group>
                </b-card>
                <b-card class="card-container" bg-variant="light">
                    <b-form-group label="Prediction options"
                    label-size="lg"
                    label-class="font-weight-bold pt-0"
                    class="mb-0"
                    label-cols-lg="3"
                   >
                            <b-form-group
                                label="Select a parameter file from an organism:"
                                label-for="param-select"
                                label-cols-sm="3"
                                label-align-sm="right"
                            >
                            <b-form-select id="param-select"
                            class="pt-2"
                                v-model="form.selectedParam"
                                :options="formOptions.paramFiles"
                                value-field="name"
                                text-field="organism"
                            >
                            </b-form-select>
                            </b-form-group>
                            <b-form-group
                            label="Select a prediction mode:"
                            label-for="predmode-checkbox"
                            label-cols-sm="3"
                            label-align-sm="right"
                            >
                            <b-form-radio-group
                                id="predmode-checkbox"
                                class="pt-2"
                                v-model="form.selectedMode"
                                required
                                :options="formOptions.predictionOptions.predictionModes"
                                :state="assemblingMode"
                                :aria-describedby="ariaDescribedby"
                            ></b-form-radio-group>
                                <b-form-invalid-feedback :state="assemblingMode">Must insert GFF evidences with assembling mode. Exons and Signals options are not compatible with this mode</b-form-invalid-feedback>
                            </b-form-group>
                            <b-form-group
                            label="DNA strands:"
                            label-for="dna-checkbox"
                            label-cols-sm="3"
                            label-align-sm="right"
                            >
                            <b-form-radio-group
                            id="dna-checkbox"
                            class="pt-2"
                                v-model="form.selectedStrands"
                                :options="formOptions.predictionOptions.dnaStrands"
                                :aria-describedby="ariaDescribedby"
                            ></b-form-radio-group>
                            </b-form-group>
                             <b-form-group
                            >
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
                             </b-form-group>
                    </b-form-group>
                </b-card>
                <b-card class="card-container" bg-variant="light">
                    <b-form-group label="Output options"
                    label-size="lg"
                    label-class="font-weight-bold pt-0"
                    class="mb-0"
                    label-cols-lg="3">
                            <b-form-group
                            label="Select an output format:"
                            label-for="output-select"
                            label-cols-sm="3"
                            label-align-sm="right"
                            >
                        <b-form-select id="output-select"
                            v-model="form.outputOption"
                            :options="formOptions.outputOptions.outputFormat">
                        </b-form-select>
                        </b-form-group>
                        <b-form-group
                            label="Signals:"
                            label-for="signals-checkbox"
                            label-cols-sm="3"
                            label-align-sm="right"
                            >
                        <b-form-checkbox-group
                            id="signals-checkbox"
                            class="pt-2"
                            v-model="form.signals"
                            :options="formOptions.outputOptions.signals"
                            :aria-describedby="ariaDescribedby">
                            </b-form-checkbox-group>
                        </b-form-group>
                              <b-form-group
                            label="Exons:"
                            label-for="exons-checkbox"
                            label-cols-sm="3"
                            label-align-sm="right"
                            >
                        <b-form-checkbox-group
                        id="exons-checkbox"
                        class="pt-2"
                            v-model="form.exons"
                            :options="formOptions.outputOptions.exons"
                            :aria-describedby="ariaDescribedby">
                        </b-form-checkbox-group>
                              </b-form-group>
                    </b-form-group>
                </b-card>
                    <div class="buttons-form">
                        <b-button type="reset" variant="danger">Reset</b-button>
                        <b-button :disabled="!validateForm" type="submit" variant="primary" style="float: inline-end">Submit</b-button>
                    </div>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
    </b-overlay>
</template>
<script>
import geneidService from "../services/GeneIdService"
import {resources} from "../static-config"
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
            demoLoaded: false,
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
        assemblingMode(){
            return this.form.selectedMode === '-O' ? (this.form.gffFile || this.form.gffText) && (this.form.exons.length === 0 && this.form.signals.length === 0) ? true : false : null
        },
        fastaFileSize(){
            return this.graphicalRap && this.form.fastaFile ? this.fileSize < 15000000 ? true : false : null
        },
        fastaTextSize(){
            return this.graphicalRap && this.form.fastaText ? new Blob([this.form.fastaText]).size < 15000000 ? true : false : null
        },
        graphicalRap(){
            // return this.form.graphicalRap ? (this.form.outputOption === '-G' ? true : false) : null
            return this.form.graphicalRap ? this.form.outputOption === '-G' ? true : false : null
        },
        validateForm(){
            return (this.graphicalRap === null || this.graphicalRap) &&
                    (this.fastaSubmitted) && 
                    (this.assemblingMode === null || this.assemblingMode) &&
                    (this.fastaFileSize === null || this.fastaFileSize) &&
                    (this.fastaTextSize === null || this.fastaTextSize)           
        }    

    },
    methods: {
      setDemoForm(){
        this.form.fastaText = resources.formDemo.fastaText
        this.form.fastaFile = null
        this.form.gffText = resources.formDemo.gffText
        this.form.gffFile = null
        this.form.outputOption = resources.formDemo.outputOption
        this.form.selectedParam = 'dros-param'
        this.form.selectedMode = this.formOptions.predictionOptions.predictionModes[0].value
        this.form.selectedStrands = resources.formDemo.selectedStrands
        this.demoLoaded = true
      },
      onSubmit(event) {
        event.preventDefault()
        // this.validateForm()
        this.loading = true
        var formData = new FormData()
        if(this.form.exons.length > 0 || this.form.signals.length > 0){
            this.form.selectedOptions = this.form.exons.concat(this.form.signals)
            this.form.exons = []
            this.form.signals = []
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
            this.$router.push({ name: 'geneid-result', params: { resultId: geneId._id.$oid }})
        })
      },
       onReset(event) {
        event.preventDefault()
            this.form.fastaText= ''
            this.form.fastaFile= null
            this.form.gffText= ''
            this.form.gffFile= null
            this.form.selectedStrands= ''
            this.form.exons= []
            this.form.signals= []
            this.form.selectedParam = this.formOptions.paramFiles[0].name
            this.form.selectedMode = this.formOptions.predictionOptions.predictionModes[0].value
            this.form.selectedOptions= []
            this.form.outputOption= '-G' //geneid as default value
            this.form.graphicalRap= true
            this.fileSize = 0
            this.demoLoaded = false
        // Trick to reset/clear native browser form validation state
        // // this.show = false
        // // this.$nextTick(() => {
        // //   this.show = true
        // // })
      },
      onFileChange(e) {
        if(e.target.id === 'fasta-file'){
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
.card-container{
    margin-top: 5px;
    margin-bottom: 5px;
}
</style>