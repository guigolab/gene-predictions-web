<template>
    <b-container>
            <page-heading-component :header="header"></page-heading-component>
        <b-row>
    <b-col cols="6" md="4" class="form">
        <GeneIdForm> </GeneIdForm>
     </b-col>
    <b-col cols="12" md ="8">
    <div class="accordion" role="tablist">
    <b-card no-body v-for="chapter in chapters" :key="chapter.title" class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
      </b-card-header>
      <b-button block @click="chapter.show = !chapter.show" variant="info">{{chapter.title}}</b-button>
      <b-collapse v-model="chapter.show" id="collapse-1" class="mt-2">
        <b-card-body>
          <b-card-text>{{chapter.description}}</b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>
    </div>
    </b-col>
        </b-row>
    </b-container>
      <!-- <div class="col-12 mt-2">
         <div class="row mb-4" v-for="chapter in chapters" :key="chapter.title">
            <div class="col-12">
               <b-button @click="chapter.show = !chapter.show" variant="primary">{{chapter.title}}</b-button>
               <b-collapse v-model="chapter.show" id="collapse-1" class="mt-2">
                  <b-card>
                     <p class="card-text">{{chapter.description}}</p>
                  </b-card>
               </b-collapse>
            </div>
         </div>
      </div> -->
<!-- </div> -->
<!-- 
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-2 variant="info">Accordion 2</b-button>
      </b-card-header>
      <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-text>{{ text }}</b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle.accordion-3 variant="info">Accordion 3</b-button>
      </b-card-header>
      <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-card-text>{{ text }}</b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card> -->
  <!-- </div> -->
</template>
<script>
import configs from '../static-config'
import GeneIdForm from '../components/GeneIdFormComponent.vue'
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
export default {
    name: 'gene-id',

    data() {
        return {
            chapters: [],
            text: '',
            header: configs.resources.geneIdDescription
        }
    },
    components: {
        GeneIdForm,
        PageHeadingComponent
    },
    mounted() {
        configs.resources.geneIdtexts
        .forEach((item) => {
            item.show = false;
            console.log(item);
            this.chapters.push(item);
        });
    }
}
</script>
<style lang="scss">

</style>