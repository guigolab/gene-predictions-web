<template>
    <b-container>
    <page-heading-component :header="texts"></page-heading-component>
    <div style="margin-bottom:20px;">
        <span style="display:block;">All the files can be obtained from our <a :href="texts.links.ftpServer">ftp server</a></span>
        <!-- <b-button style="margin-bottom: 15px;margin-top:15px;" variant="outline-info" :href="texts.links.changeLog">GENEID CHANGE LOG</b-button> -->
    </div>
      <b-row>
        <b-col cols="12" md ="8">
            <div style="display:flex;">
            <h3>geneid releases</h3>
            <b-button style="border: none;" variant="outline-info" class="mb-2" v-b-tooltip.hover title="download cumulative ChangeLog" :href="texts.links.changeLog">
                <b-icon icon="file-earmark-text" variant="outline-info"></b-icon>
            </b-button>
            <b-button style="border: none;" variant="outline-info" class="mb-2" v-b-tooltip.hover title="How to install geneid" :href="texts.links.geneIDinstructions">
                <b-icon icon="question-circle-fill"></b-icon>
            </b-button>
            <b-button style="border: none;" variant="outline-info" class="mb-2" v-b-tooltip.hover title="GitHub" href="https://github.com/guigolab/geneid">
                <b-icon icon="github"></b-icon>
            </b-button>
            </div>
            <div id="geneid-files">
            <b-card v-for="version in texts.geneIDVersions" :key="version.version" style="margin-bottom: 15px;" :title="version.version" border-variant="info" text-variant="info">
                <b-list-group vertical>
                    <b-list-group-item v-for="value in version.values" :key="value" border-variant="info">
                        <div>
                            <small>{{value.info}}</small>
                        </div>
                        <div v-if="value.checkSum">
                            <small> <strong> Please, verify the check-sum file value: </strong></small>
                            <ul style="font-size:70%">
                            <li>type: <strong>{{value.checkSum.type}}</strong></li>
                            <li>value: <strong>{{value.checkSum.value}}</strong></li>
                            </ul>
                        </div>
                        <b-button v-if="value.link" variant="outline-info" :href="value.link">{{value.description}}</b-button>
                        <b-dropdown v-if="value.links" variant="outline-info" :text="value.description">
                            <b-dropdown-item v-for="link in value.links" :key="link.name" :href="link.value" >{{link.name}}</b-dropdown-item>
                        </b-dropdown>
                    </b-list-group-item>
                </b-list-group>
            </b-card>
            </div>
        </b-col>
        <b-col cols="6" md="4">
            <div style="display:flex;">
            <h3>sgp2 releases</h3>
            <b-button style="border: none;" variant="outline-info" class="mb-2" v-b-tooltip.hover title="How to install sgp2" :href="texts.links.sgp2Instructions">
                <b-icon icon="question-circle-fill"></b-icon>
            </b-button>
            <b-button style="border: none;" variant="outline-info" class="mb-2" v-b-tooltip.hover title="GitHub" href="https://github.com/guigolab/sgp2">
                <b-icon icon="github"></b-icon>
            </b-button>
            </div>
            <div id="geneid-files">
            <b-card v-for="version in texts.SGP2Versions" :key="version.version" style="margin-bottom: 15px;" :title="version.version" border-variant="info" text-variant="info" >
                <b-list-group vertical>
                    <b-list-group-item v-for="value in version.values" :key="value">
                        <b-button variant="outline-info" :href="value.link">{{value.description}}</b-button>
                    </b-list-group-item>
                </b-list-group>
            </b-card>
            </div>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import PageHeadingComponent from '../components/PageHeadingComponent.vue';
import config from '../static-config'

export default {
    name: 'download-distributions',
    data() {
        return {
            texts: config.resources.downloadPageTexts
        }
    },
    mounted(){
    },
    components: {
        PageHeadingComponent
    }
};
</script>
<style>
#geneid-files {
    max-height: 500px;
    overflow: scroll;
}
</style>
