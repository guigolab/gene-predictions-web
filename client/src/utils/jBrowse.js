import '@fontsource/roboto'
// import React from 'react'
import {
  createViewState,
  JBrowseLinearGenomeView,
} from '@jbrowse/react-linear-genome-view'

import store from '../store'
import React from 'react'


const assembly = store.getters['jbrowse/assembly']
const tracks = store.getters['jbrowse/tracks']
// const defaultSession = store.getters['jbrowse/defaultSession']
// const assembly = {
//   name: 'GRCh38',
//   sequence: {
//     type: 'ReferenceSequenceTrack',
//     trackId: 'GRCh38-ReferenceSequenceTrack',
//     adapter: {
//       type: 'BgzipFastaAdapter',
//       fastaLocation: {
//         uri: 'https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz',
//         locationType: 'UriLocation',
//       },
//       faiLocation: {
//         uri: 'https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz.fai',
//         locationType: 'UriLocation',
//       },
//       gziLocation: {
//         uri: 'https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/fasta/GRCh38.fa.gz.gzi',
//         locationType: 'UriLocation',
//       },
//     },
//   },
//   aliases: ['hg38'],
//   refNameAliases: {
//     adapter: {
//       type: 'RefNameAliasAdapter',
//       location: {
//         uri: 'https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/hg38_aliases.txt',
//         locationType: 'UriLocation',
//       },
//     },
//   },
// }

// const tracks = [
//   {
//     type: 'FeatureTrack',
//     trackId: 'ncbi_refseq_109_hg38',
//     name: 'NCBI RefSeq (GFF3Tabix)',
//     assemblyNames: ['GRCh38'],
//     category: ['Annotation'],
//     adapter: {
//       type: 'Gff3TabixAdapter',
//       gffGzLocation: {
//         uri: 'https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz',
//         locationType: 'UriLocation',
//       },
//       index: {
//         location: {
//           uri: 'https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/ncbi_refseq/GCA_000001405.15_GRCh38_full_analysis_set.refseq_annotation.sorted.gff.gz.tbi',
//           locationType: 'UriLocation',
//         },
//       },
//     },
//   },
// ]

// const defaultSession = {
//   name: 'My session',
//   view: {
//     id: 'linearGenomeView',
//     type: 'LinearGenomeView',
//     tracks: [
//       {
//         type: 'ReferenceSequenceTrack',
//         configuration: 'GRCh38-ReferenceSequenceTrack',
//         displays: [
//           {
//             type: 'LinearReferenceSequenceDisplay',
//             configuration:
//               'GRCh38-ReferenceSequenceTrack-LinearReferenceSequenceDisplay',
//           },
//         ],
//       },
//       {
//         type: 'FeatureTrack',
//         configuration: 'ncbi_refseq_109_hg38',
//         displays: [
//           {
//             type: 'LinearBasicDisplay',
//             configuration: 'ncbi_refseq_109_hg38-LinearBasicDisplay',
//           },
//         ],
//       },
//     ],
//   },
// }

export default class JBrowse extends React.Component {
  constructor(props) {
    super(props);
    this.state = null
  }
  
  render() {
    return (
      <JBrowseLinearGenomeView viewState={createViewState({
        assembly,
        tracks,
        // location: '1:10..100',
        // location: '10:29,838,737..29,838,819',
        // defaultSession,
      })} />
    )
  }
}

// function View() {
//   const state = createViewState({
//     assembly,
//     tracks,
//     location: '10:29,838,737..29,838,819',
//     defaultSession,
//   })
//   return (<JBrowseLinearGenomeView viewState={state} />)
// }
// export default View

// export const JBrowse = () => {
//   const state = createViewState({
//     assembly,
//     tracks,
//     location: '10:29,838,737..29,838,819',
//     defaultSession,
//   })
//   return (<JBrowseLinearGenomeView viewState={state} />)
// }