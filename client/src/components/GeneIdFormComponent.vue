<template>
  <b-form v-if="show" @submit="onSubmit" @reset="onReset">
        <b-form-group label="Gene Id form" label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0">
            <b-form-group label="Paste your FASTA/GFF sequence here">
                <b-form-textarea
                id="textarea"
                v-model="form.text"
                rows="3"
                max-rows="6"
                ></b-form-textarea>
            </b-form-group>
            <b-form-group label="... or search a FASTA/GFF file to process">
                <b-form-file
                v-model="form.file1"
                :state="Boolean(form.file1)"
                drop-placeholder="Drop here..."
                ></b-form-file>
            </b-form-group>
        </b-form-group>
        <b-form-group label="Prediction options" label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0">
            <b-form-group v-for="(item,index) in form.options" :key="index" :label="item.title" v-slot="{ ariaDescribedby }">
                <b-form-checkbox-group v-bind:id="index"
                    v-model="item.active"
                    :options="item.options"
                    :state="item.active"
                    :aria-describedby="ariaDescribedby"
                    name="checkbox-validation"
                ></b-form-checkbox-group>
                <b-form-invalid-feedback :state="item.active">Please select one</b-form-invalid-feedback>
                <b-form-valid-feedback :state="item.active">Thank you</b-form-valid-feedback>
            </b-form-group>
        </b-form-group>
        <div class="buttons-form">
        <b-button type="reset" variant="danger">Reset</b-button>
          <b-button type="submit" variant="primary" style="float: inline-end">Submit</b-button>
        </div>
    </b-form>
</template>
<script>
import config from '../static-config'
export default {
    name: "gene-id-form",
    data () {
        return {
            form : {
            text: '',
            file1: null,
            selectedOptions: [],
            options: config.predictionOptions
            },
            show: true,
            
        }
    },
    // computed: {
    //     active() {
    //         console.log(this)
    //         return this.form.selectedOptions[index].length === 1
    //     }
    // },
      methods: {
      onSubmit(event) {
        event.preventDefault()
        console.log(this.form);
        alert(JSON.stringify(this.form))
      },
       onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.selectedOptions = []
        this.form.file1 = null,
        this.form.text = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
      }
}
</script>
<style>
.buttons-form{
    display: block;
}
</style>