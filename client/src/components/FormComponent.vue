<template>
    <b-overlay :show="loading" rounded="sm">
        <b-container>
            <b-row>
                <b-col>
                    <b-form enctype="multipart/form-data" @submit="onSubmit" @reset="onReset">
                         <b-card class="card-container" bg-variant="light">
                            <div v-for="group in groups" :key="group.label">
                            <b-form-group 
                                :label="group.label"
                                label-cols-lg="3"
                                label-size="lg"
                                label-class="font-weight-bold pt-0"
                                class="mb-0"
                            > 
                                <div v-for="field in group.fields" :key="field.label"> 
                                <b-form-group 
                                label-cols-sm="3"
                                label-align-sm="right"
                                :label-for="field.label"
                                :label="field.description"
                                > 
                                     <div v-if="field.type === 'text-area'">
                                        <b-form-textarea
                                        class="pt-2"
                                        :id="field.label"
                                        :state="field.label === 'fastaText'? Boolean(fastaFile) ? null : Boolean(fastaText) : null"
                                        :disabled="field.label === 'fastaText'? Boolean(fastaFile) : Boolean(gffFile)"
                                        v-model="self()[field.label]"
                                        rows="5"
                                        >
                                        </b-form-textarea>
                                    </div>
                                    <div v-else-if="field.type === 'file'">
                                        <b-form-file
                                        class="pt-2"
                                        @change="onFileChange"
                                        :id="field.label"
                                        :state="field.label === 'fastaFile'? Boolean(fastaText) ? null : Boolean(fastaFile) : null"
                                        :disabled="field.label === 'fastaFile'? Boolean(fastaText) : Boolean(gffText)"
                                        v-model="self()[field.label]"
                                        drop-placeholder="Drop file here..."
                                        :accept="field.label === 'fastaFile'?'.fa, .fasta':'.gff, .gff3'"
                                        >
                                        </b-form-file>
                                    </div>
                                    <div v-else-if="field.type === 'select'">
                                        <b-form-select
                                        class="pt-2"
                                        :id="field.label"
                                        :options="field.label === 'param' ? paramOptions : field.options"
                                        v-model="self()[field.label]"
                                        >
                                        </b-form-select>
                                    </div>
                                    <div v-else-if="field.type === 'radio-group'">
                                        <b-form-radio-group
                                        :id="field.label"
                                        :options="field.options"
                                        v-model="self()[field.label]"
                                        class="pt-2"
                                        >
                                        </b-form-radio-group>
                                    </div>
                                    <div v-else-if="field.type === 'checkbox-group'">
                                        <b-form-checkbox-group
                                        class="pt-2"
                                        :id="field.label"
                                        :options="field.options"
                                        v-model="self()[field.label]"
                                        >
                                        </b-form-checkbox-group>
                                    </div>
                                    <div v-else-if="field.type === 'checkbox'">
                                        <b-form-checkbox
                                        class="pt-2"
                                        :id="field.label"
                                        v-model="self()[field.label]"
                                        :state="graph ? output === '-G' : null"
                                        switch
                                        >
                                        </b-form-checkbox>
                                        <b-form-invalid-feedback :state=" graph ? output === '-G' : null">The output format must be GFF</b-form-invalid-feedback>
                                    </div> 
                                 </b-form-group> 
                                 </div> 
                             </b-form-group>
                            </div>
                        </b-card>
                        <b-button @click="download">Download</b-button>
                        <b-button type="submit">Submit</b-button>
                    </b-form> 
                </b-col>
            </b-row>
        </b-container>
    </b-overlay>
</template>
<script>
// import geneidService from "../services/GeneIdService"
import fileService from "../services/TaxonFileService"
import {formGroups} from "../static-config"
import {mapFields} from "../helper"
export default {
    data(){
        return {
            groups: formGroups,
            paramOptions: [],
            loading: false,
        }
    },
    computed: {
        options(){
            return this.exons.concat(this.signals)
        },
        ...mapFields({
            fields: ['fastaText','fastaFile','gffText','gffFile',
            'param','strands', 'mode', 'exons',
            'signals', 'output', 'graph'],
            base: "geneIdForm",
            mutation: "form/update"
        }),
    },
    methods: {
        self() {
            return this
        },
        download(){
            var file = "fasta.fa"
            const url = window.URL.createObjectURL(new Blob([this.fastaFile], { type: 'application/octet-stream'}));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', file);
            link.click();
        },
        onFileChange(e) {
            console.log(e)
            this[e.target.id] = e.target.files[0]
            // this[field] = e.target.files[0]
        },   
        onSubmit(event) {
        event.preventDefault()
        // this.validateForm()
        // this.loading = true
        // var formData = new FormData()
        // if(this.form.exons.length > 0 || this.form.signals.length > 0){
        //     this.form.selectedOptions = this.form.exons.concat(this.form.signals)
        //     this.form.exons = []
        //     this.form.signals = []
        // }
        // for (const [key, value] of Object.entries(this.form)) {
        //     if (value){
        //         formData.append(key,value)
        //     }
        // }
        // geneidService.sendForm(formData)
        // .then(response => {
        //     // response contains a geneid model object
        //     const geneId = response.data
        //     this.$router.push({ name: 'geneid-result', params: { resultId: geneId._id.$oid }})
        // })
      },
      onReset(){

      }
    },
    mounted(){
        //inject param options
        this.loading = true
        fileService.getAll({type: 'param'}).then(response => {
            this.$nextTick(() => {
                this.paramOptions = response.data.map(param => ({text : param.organism, value : param.name}))
                this.loading = false
            })
        })

    },


}
</script>