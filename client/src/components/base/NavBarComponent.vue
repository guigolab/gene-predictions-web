<template>
    <div style="margin-bottom:15px">
  <b-navbar toggleable="true" type="dark" variant="info">
  <b-navbar-brand to="/"> Geneid Web Server </b-navbar-brand>    <b-navbar-toggle target="nav-collapse">
    </b-navbar-toggle>
    <b-sidebar id="nav-collapse" bg-variant="dark" text-variant="light" shadow aria-labelledby="sidebar-no-header-title" no-header right
      backdrop
      >
    <div class="p3">
      <b-nav vertical align="end">
          <b-nav-item  active-class="active" class="nav-link" to="/" >
           <b-icon icon="house" variant="outline-info"></b-icon>
            HOME 
          </b-nav-item>
          <b-nav-item  active-class="active" class="nav-link" :to="{name: 'tree-of-life', params: {node: 'root'}}">
           <b-icon icon="diagram3" variant="outline-info"></b-icon>
            TREE OF LIFE 
          </b-nav-item> 
          <!-- <b-nav-item class="nav-link" to="/geneid-form" >
          <b-icon icon="gear-wide" variant="outline-info"></b-icon>
            GENEID WEB SERVER
          </b-nav-item> -->
      </b-nav>
    </div>
    </b-sidebar>
    </b-navbar>
</div>
</template>
<script>
import { BNavbar, BSidebar, BNav, BNavbarToggle, BNavItem, BNavbarBrand} from 'bootstrap-vue'

export default {
  components: {
    BNavbar, BSidebar, BNav, BNavbarToggle, BNavItem, BNavbarBrand
  }
  
}
</script>
<style scoped>
.nav-link {
  color: white !important;
}
</style>