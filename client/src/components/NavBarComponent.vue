<template>
    <div>
  <b-navbar toggleable="true" type="dark" variant="info">
    <b-navbar-brand to="/"> Genome BioInformatics Research Lab </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse">
    </b-navbar-toggle>
    <b-sidebar id="nav-collapse" aria-labelledby="sidebar-no-header-title" no-header right
      backdrop
      shadow>
    <div class="p3">
      <b-nav vertical align="end">
          <b-nav-item  active-class="active" class="nav-link" to="/" >
           <b-icon icon="house" variant="outline-info"></b-icon>
            HOME 
          </b-nav-item> 
          <b-nav-item class="nav-link" to="/geneid" >
          <b-icon icon="binoculars" variant="outline-info"></b-icon>
            GENEID
          </b-nav-item>
          <b-nav-item class="nav-link" to="/geneid-training" >
          <b-icon icon="gear-wide" variant="outline-info"></b-icon>
            GENEID TRAINING
          </b-nav-item>    
          <b-nav-item class="nav-link" to="/geneid-accuracy" >
          <b-icon icon="eyeglasses" variant="outline-info"></b-icon>
            GENEID ACCURACY
          </b-nav-item>    
          <b-nav-item active-class="active" class="nav-link" href="https://genome.crg.cat/software/geneid/docs_1.2/index.html" >
        <b-icon icon="book" variant="outline-info"></b-icon>      
            GENEID 1.2 DOCS
          </b-nav-item>
          <b-nav-item active-class="active" class="nav-link" to="/sgp2" >
          <b-icon icon="binoculars-fill" variant="outline-info"></b-icon>
            SGP2 
          </b-nav-item> 
            <b-nav-item active-class="active" class="nav-link" to="/sgp2-algorithm" >
        <b-icon icon="calculator-fill" variant="outline-info"></b-icon>
            SGP2 ALGORITHM
          </b-nav-item> 
          <b-nav-item active-class="active" class="nav-link" to="/software-download" >
        <b-icon icon="download" variant="outline-info"></b-icon>
           DOWNLOADS
          </b-nav-item>  
      </b-nav>
    </div>
    </b-sidebar>
    </b-navbar>
</div>
</template>
<script>
// import Router from 'vue-router'
export default {
        data(){
            return {
                // links: Router.routes
            }
        }
    }
</script>


<style scoped>
.nav-link {
  color: #17a2b8;
  font-family: Raleway;
}
</style>