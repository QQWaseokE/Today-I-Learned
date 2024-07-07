import {Component} from 'react'
import ClassComponent from './ClassComponent'

export default class App extends Component {
  render() {
    return (
      <ul>
        <ClassComponent href="http://www.google.coom" text="go to Google" />
        <ClassComponent href="http://www.twitter.coom" text="go to Twitter" />
      </ul>
    )
  }
}
