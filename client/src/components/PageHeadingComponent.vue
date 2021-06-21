<template>
    <div class="page-header-container">
    <h1 class="text-center">{{title}}</h1>
    <span class="text-center">{{description}}</span>
    </div>
</template>

<script>
import description from '../static-config'

export default {
    name: "PageHeadingComponent",
    data () {
        return {
            title: "GENE PREDICTIONS ON WHOLE GENOMES",
            description: description.resources.genePDescription
            // links: {"geneid": }predictions
            }
    }
}
</script>
<style >
.page-header-container{
    margin-bottom: 15px;
}
</style>