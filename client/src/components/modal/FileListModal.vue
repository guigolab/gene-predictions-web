<template>
   <b-modal size="xl" id="data-modal" scrollable :title="organism +' '+model">
      <table-component
        stacked
        :items="data"
      >
        <template #cell(fastaLocation)="row">
          <a :href="row.item['fastaLocation']">Download</a>
        </template>
        <template #cell(faiLocation)="row">
          <a :href="row.item['faiLocation']">Download</a>
        </template> 
        <template #cell(gziLocation)="row">
          <a :href="row.item['gziLocation']">Download</a>
        </template> 
        <template #cell(gffGzLocation)="row">
          <a :href="row.item['gffGzLocation']">Download</a>
        </template> 
        <template #cell(tabIndexLocation)="row">
          <a :href="row.item['tabIndexLocation']">Download</a>
        </template> 
        <template #cell(paramLocation)="row">
          <a :href="row.item['paramLocation']">Download</a>
        </template>
        <template #cell(created)="row">
         {{new Date(row.item['created'].$date)}}
        </template>
      </table-component>
    </b-modal>
</template>

<script>
import TableComponent from "../base/TableComponent.vue";

export default {
  name: "file-list-modal",
  props: ['data', 'organism', 'model'],
  components: { TableComponent},
};

</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
