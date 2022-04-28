import '@fontsource/roboto'
import {
  JBrowseLinearGenomeView,
  createViewState
} from '@jbrowse/react-linear-genome-view'

import React from 'react'
import store from '../store'


export default class JBrowse extends React.Component {
  constructor(props){
    super(props);
    this.state = {
        assembly: store.getters['jbrowse/assembly'],
        tracks: store.getters['jbrowse/tracks'],
        defaultSession: store.getters['jbrowse/defaultSession']
    }
  }
  render() {
    const configuration = {
      "theme" :{
        "palette": {
          "primary": {
            "main": "#311b92"
          },
          "secondary": {
            "main": "#0097a7"
          },
          "tertiary": {
            "main": "#f57c00"
          },
          "quaternary": {
            "main": "#d50000"
          }
        }
      },
      "logoPath":{
        "uri": "<%= BASE_URL %>favicon.ico"
      }
    }
    var {assembly,tracks,defaultSession} = this.state
    var state = createViewState({
      assembly,
      tracks,
      configuration,
      defaultSession
    })
    return (
      <JBrowseLinearGenomeView viewState={state} />
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
