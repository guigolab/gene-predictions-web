<template>
<b-overlay :show="loading" rounded="sm">
    <b-container>
        <b-row>
            <b-col>
                <b-button variant="info" :disabled="demoLoaded" @click="setDemoForm()">Load Demo</b-button>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <b-form enctype="multipart/form-data" novalidate v-if="show" @submit="onSubmit" @reset="onReset">
                <b-card class="card-container" bg-variant="light">
                    <b-form-group 
                        label="Data input" 
                        label-size="lg"
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
                        :required="!Boolean(fastaText) && !Boolean(fastaFile)"
                        v-model="fastaText" :state="fastaFileSize" :disabled="Boolean(fastaFile)" rows="5"
                        >
                        </b-form-textarea>
                            <b-form-invalid-feedback v-if="fastaText" :state="fastaFileSize">Maximum sequence size for plots: 150,000 bps</b-form-invalid-feedback>
                         </b-form-group>
                        <b-form-group
                        label="Upload a FASTA file to process:"
                        label-for="fasta-file"
                        label-cols-sm="3"
                        label-align-sm="right"
                        >
                        <b-form-file
                        @change="onFastaFileChange"
                        class="pt-2"
                        :required="!Boolean(fastaText) && !Boolean(fastaFile)"
                        :disabled="Boolean(fastaText)"
                        accept=".fasta, .fa"
                        id="fasta-file"
                        :state="fastaFileSize"
                        :value="fastaFile"
                        drop-placeholder="Drop fasta file here..."
                        >
                        </b-form-file>
                        <b-form-invalid-feedback v-if="fastaFile" :state="fastaFileSize">Maximum sequence size for plots: 150,000 bps</b-form-invalid-feedback>
                        </b-form-group>
                        <b-form-group
                        label="Paste your GFF evidences here (Field separator: tab):"
                        label-for="textarea-gff"
                        label-cols-sm="3"
                        label-align-sm="right"
                        >
                        <b-form-textarea
                        class="pt-2"
                        :disabled="Boolean(gffFile)"
                        id="textarea-gff"
                        v-model="gffText"
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
                        :disabled="Boolean(gffText)"
                        accept=".gff, .gff3"
                        id="gff-file"
                        v-model="gffFile"
                        drop-placeholder="Drop gff file here..."
                        >
                        </b-form-file>
                         </b-form-group>
                    </b-form-group>
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
                                v-model="param"
                                :options="paramOptions"
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
                                v-model="mode"
                                required
                                :options="formOptions.mode"
                                :state="assemblingMode"
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
                                v-model="strands"
                                :options="formOptions.strands"
                            ></b-form-radio-group>
                        </b-form-group>
                        <b-form-group>
                            <b-form-checkbox
                            id="graph-rap"
                            v-model="gff2ps"
                            :state="graphicalRap"
                            name="graph-rap"
                            switch>
                            Do you want a graphical representation of the predictions ?
                            </b-form-checkbox>
                            <b-form-invalid-feedback :state="graphicalRap">The output format must be GFF</b-form-invalid-feedback>
                        </b-form-group>
                    </b-form-group>
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
                                v-model="output"
                                :options="formOptions.output">
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
                                v-model="signals"
                                :options="formOptions.signals">
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
                                v-model="exons"
                                :options="formOptions.exons">
                            </b-form-checkbox-group>
                        </b-form-group>
                    </b-form-group>
                <template #footer>
                    <b-button-toolbar justify>
                        <b-button type="reset" variant="danger">Reset</b-button>
                        <b-button :disabled="!validateForm" type="submit" variant="primary">Submit</b-button>
                    </b-button-toolbar>
                </template>
                </b-card>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
    </b-overlay>
</template>
<script>
import geneidService from "../services/GeneIdService"

import {mapFields} from '../helper' 
import {formFields} from "../static-config"

export default {
    name: "gene-id-form",
    data () {
        return {
            formOptions : formFields,
            fastaFile: null,
            gffFile: null,
            show: true,
            loading: false,
            fileSize : 0, 
            demoLoaded: false,
        }
    },
    computed: {
        ...mapFields({
            fields: [
                'fastaText','gffText',
                'param','strands','mode','exons','signals',
                'output','gff2ps'
            ],
            module: 'form',
            base: 'geneidForm',
            mutation: 'form/updateForm'
        }),
        paramOptions(){
            return this.$store.getters['form/params']
        },
        fastaSubmitted(){
            return this.fastaText || this.fastaFile
        },
        assemblingMode(){
            return this.mode === '-O' ? (this.gffFile || this.gffText) && (this.exons.length === 0 && this.signals.length === 0) : null
        },
        fastaFileSize(){
            return this.gff2ps && this.fastaFile ? this.fileSize < 15000000 : null
        },
        fastaTextSize(){
            return this.gff2ps && this.fastaText ? new Blob([this.fastaText]).size < 15000000 : null
        },
        graphicalRap(){
            // return this.gff2ps ? (this.output === '-G' ? true : false) : null
            return this.gff2ps ? this.output === '-G' : null
        },
        validateForm(){
            return (this.gff2ps === null || this.gff2ps) &&
                    (this.fastaSubmitted) && 
                    (this.assemblingMode === null || this.assemblingMode) &&
                    (this.fastaFileSize === null || this.fastaFileSize) &&
                    (this.fastaTextSize === null || this.fastaTextSize)           
        }    

    },
    methods: {
      setDemoForm(){
          this.$store.dispatch('form/loadDemo')
      },
      onSubmit(event) {
        event.preventDefault()
        // this.validateForm()
        this.loading = true
        var formData = new FormData()
        if(this.fastaFile){
            formData.append('fastaFile', this.fastaFile)
        }
        if(this.gffFile){
            formData.append('gffFile', this.gffFile)
        }
        if(this.exons.length > 0 || this.signals.length > 0){
            const options = this.exons.concat(this.signals)
            formData.append('options', options)
            this.exons = []
            this.signals = []
        }
        const form = this.$store.getters['form/getForm']
        Object.keys(form)
        .filter(key => Array.isArray(form[key]) ? form[key].length > 0 : form[key])
        .forEach(key => formData.append(key, form[key]))
        geneidService.sendForm(formData)
        .then(response => {
            // response contains a geneid model object
            // store result in vuex here
            // store file ids for download
            const geneId = response.data
            this.$router.push({ name: 'geneid-result', params: { resultId: geneId._id.$oid }})
        })
      },
       onReset(event) {
        event.preventDefault()
            // this.fastaText= ''
            // this.fastaFile= null
            // this.gffText= ''
            // this.gffFile= null
            // this.strands= ''
            // this.exons= []
            // this.signals= []
            // this.selectedParam = this.formOptions.paramFiles[0].name
            // this.selectedMode = this.formOptions.predictionOptions.predictionModes[0].value
            // this.selectedOptions= []
            // this.output= '-G' //geneid as default value
            // this.gff2ps= true
            // this.fileSize = 0
            // this.demoLoaded = false
        // Trick to reset/clear native browser form validation state
        // // this.show = false
        // // this.$nextTick(() => {
        // //   this.show = true
        // // })
      },
      onFastaFileChange(e) {
        console.log(this.fastaFile)
        this.fastaFile = e.target.files[0]
        console.log(this.fastaFile)
        // console.log(this.$store.getters['form/getFastaFile'])
        // // console.log(e.target.files[0])
        // this.$store.commit('form/updateForm',{label: 'fastaFile', value: e.target.files[0]})
        // console.log(this.$store.getters['form/getFastaFile'])
        // this.fastaFile = e.target.files[0]
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