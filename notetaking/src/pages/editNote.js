import Image from 'next/image'
import { Inter } from 'next/font/google'
import Title1 from "../components/Title1.jsx"
import Body from "../components/Body.jsx"
import Header from '../components/Header.jsx'
import Specifications from '../components/Specifications.jsx'

const inter = Inter({ subsets: ['latin'] })



export default function editNote() {
  /*const styles = {
    main: {
      backgroundColor: "#FFFFFF",
      width: "100%",
      height: "100%",
    },
    inputText: {
      padding: "10px",
      color: "red",
    },
  };*/
  return (
    <div>
    <Header/>
    <Title1/>
    <Specifications/>
    <Body/>
    </div>
  )
}
