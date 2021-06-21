<template>
  <div class="list row shadow p-3">
    <div class="col-md-12">
      <div class="list row mb-2">
        <div class="col-md-6">
          <h4>Species List</h4>
        </div>
        <!-- <div class="col-md-6">
              <b-button v-b-modal.create-user-modal variant="primary">
                <b-icon icon="plus" aria-hidden="true"></b-icon>Create
              </b-button>
              <b-button variant="danger align-right ml-3" v-b-modal.confirmation-modal>
                <b-icon icon="trash-fill" aria-hidden="true"></b-icon>Delete All
              </b-button> 
        </div> -->
      </div>
    </div>
    <div class="col-md-12">
      <b-table 
        id="species-table"
        striped
        hover
        :items="species"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        show-empty
        v-b-modal.file-list-modal
      >
        <template #cell(index)="data">
          {{ ((currentPage-1) * perPage)+(data.index + 1) }}
        </template>
        <!-- <template #cell(delete)="data">
          <a @click="selectedSpeciesr=data.item" v-b-modal.confirmation-modal>
            <b-icon icon="trash-fill" variant="danger" aria-hidden="true"></b-icon>
          </a>
        </template>
        <template #cell(edit)="data">
          <a @click="selectedUser=data.item" v-b-modal.confirmation-modal>
            <b-icon icon="pencil-fill" variant="primary" aria-hidden="true"></b-icon>
          </a>
        </template> -->
      </b-table>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="users-table"
        ></b-pagination>
    </div>
    
    <!-- <CreateUserModal
      v-on:initiateCreate="createUser"
    ></CreateUserModal>
   
    <Confirmation
      v-on:confirmationOk="deleteUser"
      v-bind:user="selectedUser"
    ></Confirmation> -->

  </div>
</template>

<script>
import SpeciesDataService from "../services/SpeciesDataService";
// import Confirmation from "../components/modal/Confirmation";
// import VisualizeSpeciesModal from "../components/modal/VisualizModal";

export default {
  name: "species-list",
  data() {
    return {
      selectedSpecies:{"tax_id":null,"name":null},
      species: [],
      fields: ["index","tax_id", "name"],
      currentPage: 1,
      perPage: 3,
    };
  },
  components:{
    // Confirmation,
    // CreateUserModal
  },
    methods: {
        retrieveSpecies() {
        SpeciesDataService.getAll()
            .then(response => {
            this.species = response.data;
            console.log(response.data);
            })
            .catch(e => {
            console.log(e);
            });
        }
        },
    computed: {
        rows() {
            return this.species.length
            }
        },
    mounted() {
        this.retrieveSpecies();
    }
};

</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
