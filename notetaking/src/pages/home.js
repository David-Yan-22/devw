import React, { useState } from "react";
import {useContext } from "react";
import AddCircleIcon from '@mui/icons-material/AddCircle';

function Home() {
    const [rectangles, setRectangles] = useState([]);

    const addRectangle = () => {
      const newRectangle = {
        color: generatePastelColor(),
      };
      setRectangles([...rectangles, newRectangle]);
    };

    const generatePastelColor = () => {
        let R = Math.floor((Math.random() * 127) + 127);
        let G = Math.floor((Math.random() * 127) + 127);
        let B = Math.floor((Math.random() * 127) + 127);
        
        let rgb = (R << 16) + (G << 8) + B;
        return `#${rgb.toString(16)}`;      
      }


    const BoxEdit = () => {
        return (
          <div className="box">
            <img className="edit-icon" alt="Icon pencil" src="./icons/edit_icon.png" />
          </div>
        );
      };
    
    const BoxAdd = () => {
        return (
          <div className="box">
            <img className="edit-icon" alt="Icon pencil" src="icons/pluis_icon.png" />
          </div>
        );
      };
    
    
  return (
    <div className="desktop">
      <div className="div">
        <div className="text-wrapper">Violet’s Notes</div>


        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 50 50" fill="none" onClick={addRectangle}  className="add-note">
            <path d="M18.75 0V18.75H0V31.25H18.75V50H31.25V31.25H50V18.75H31.25V0H18.75Z" fill="grey"/>
        </svg>

        <div className="rectangle-container">
            {rectangles.map((rectangle, index) => (
            <div 
                key={index}
                className="rectangle"
                style={{
                width: '244px',
                height: '227px',
                backgroundColor: rectangle.color,
                }}
            >
                <img src="/icons/edit_icon.png"className="icon"/>
                <div className="title">note</div>

            </div>
            ))}
        </div>

      </div>
    </div>
  );
};

export default Home;