const state = () => ({
   assembly: {
    name: 'GRCh38',
    sequence: {
      type: 'ReferenceSequenceTrack',
      trackId: 'GRCh38-ReferenceSequenceTrack',
      adapter: {
        type: 'BgzipFastaAdapter',
        fastaLocation: {
          uri: 'http://localhost/files/Bos_taurus.ARS-UCD1.2.dna.toplevel.fa.gz',
          locationType: 'UriLocation',
        },
        faiLocation: {
          uri: 'http://localhost/files/Bos_taurus.ARS-UCD1.2.dna.toplevel.fa.gz.fai',
          locationType: 'UriLocation',
        },
        gziLocation: {
          uri: 'http://localhost/files/Bos_taurus.ARS-UCD1.2.dna.toplevel.fa.gz.gzi',
          locationType: 'UriLocation',
        },
      },
    },
    aliases: ['hg38'],
    // refNameAliases: {
    //   adapter: {
    //     type: 'RefNameAliasAdapter',
    //     location: {
    //         // uri: 'http://ftp.ebi.ac.uk/pub/databases/ena/assembly/GCA_901/GCA_901699/GCA_901699155.2_sequence_report.txt',
    //         uri: 'https://s3.amazonaws.com/jbrowse.org/genomes/GRCh38/hg38_aliases.txt',
    //         locationType: 'UriLocation',
    //     },
    //   },
    // },
   },
   tracks: [
    {
        type: 'FeatureTrack',
        trackId: 'BTaurus',
        name: 'Bos Taurus Geneid',
        assemblyNames: ['GRCh38'],
        // assemblyNames: ['bStrTur1.1'],
        category: ['Annotation'],
        adapter: {
          type: 'Gff3TabixAdapter',
          gffGzLocation: {
            uri: 'http://localhost/files/bos_taurus.no_extra_evidence.gff3.gz',
            locationType: 'UriLocation',
          },
          index: {
            location: {
              uri: 'http://localhost/files/bos_taurus.no_extra_evidence.gff3.gz.tbi',
              locationType: 'UriLocation',
            },
          },
        },
      },
      {
        type: 'FeatureTrack',
        trackId: 'BMutus',
        name: 'Bos Mutus Geneid',
        assemblyNames: ['GRCh38'],
        // assemblyNames: ['bStrTur1.1'],
        category: ['Annotation'],
        adapter: {
          type: 'Gff3TabixAdapter',
          gffGzLocation: {
            uri: 'http://localhost/files/bos_mutus.no_extra_evidence.gff3.gz',
            locationType: 'UriLocation',
          },
          index: {
            location: {
              uri: 'http://localhost/files/bos_mutus.no_extra_evidence.gff3.gz.tbi',
              locationType: 'UriLocation',
            },
          },
        },
      },
    // {
    //     type: 'FeatureTrack',
    //     trackId: 'ncbi_refseq_109_hg38',
    //     name: 'NCBI RefSeq (GFF3Tabix)',
    //     // assemblyNames: ['GRCh38'],
    //     assemblyNames: ['bStrTur1.1'],
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
   ],
   defaultSession: {
    name: 'My session',
    view: {
      id: 'linearGenomeView',
      type: 'LinearGenomeView',
      tracks: [
        {
          type: 'ReferenceSequenceTrack',
          configuration: 'GRCh38-ReferenceSequenceTrack',
          displays: [
            {
              type: 'LinearReferenceSequenceDisplay',
              configuration:
                'GRCh38-ReferenceSequenceTrack-LinearReferenceSequenceDisplay',
            },
          ],
        },
        {
          type: 'FeatureTrack',
          configuration: 'ncbi_refseq_109_hg38',
          displays: [
            {
              type: 'LinearBasicDisplay',
              configuration: 'ncbi_refseq_109_hg38-LinearBasicDisplay',
            },
          ],
        },
      ],
    },
   },
})
const mutations= {
    setAssembly(state, payload){
      state.assembly = {...payload}
    },
    setTracks(state, payload){
        state.tracks = [...payload]
    },
    setDefaultSession(state, payload){
        state.defaultSession = {...payload}
    }
}
const getters = {
    assembly(state){
        return state.assembly
    },
    tracks(state){
        return state.tracks
    },
    defaultSession(state){
        return state.defaultSession
    }
}
export default {
    namespaced: true,
    state,
    getters,
    mutations
}