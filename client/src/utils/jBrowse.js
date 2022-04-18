import '@fontsource/roboto'
import {
  JBrowseLinearGenomeView,
  createViewState
} from '@jbrowse/react-linear-genome-view'

import React from 'react'

export default class JBrowse extends React.Component {
  constructor(props){
    super(props);
    this.state = {
        assembly: this.props.assembly,
        assemblyName: this.props.assemblyName,
        tracks: this.props.tracks
    }
  }
  render() {
    const {assembly} = this.state
    const {tracks} = this.state
    const {assemblyName} = this.state
    console.log(assemblyName)
    const state = createViewState({
      assembly,
      tracks
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
