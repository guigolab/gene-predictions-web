<template>
    <div class="page-header-container">
    <h1 class="text-center">{{header.title}}</h1>
    <span class="text-center">{{header.description}}</span>
    </div>
</template>

<script>

export default {
    name: "PageHeadingComponent",
    props: ['header']
}
</script>
<style >
.page-header-container{
    margin-bottom: 5px;
}
</style>