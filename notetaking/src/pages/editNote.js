import Image from 'next/image'
import { Inter } from 'next/font/google'
import Title1 from "../components/Title1.jsx"
import Body from "../components/Body.jsx"
import Header from '../components/Header.jsx'
import Specifications from '../components/Specifications.jsx'
import SubmitButton from '@/components/SubmitButton.jsx'
import CancelButton from '@/components/CancelButton.jsx'

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
    /*<div>
    <Title1/>
    <Body/>
    </div>*/
    <div class = "div 7">
      <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: "16px"}}>
      
      <Title1 />
      
    </div>
    <Body />

    <div class = "wrapper grid">
        <div class = "div5"><SubmitButton/></div>
        <div class = "div6"><CancelButton/></div>
      </div>
  </div>
  )
}
