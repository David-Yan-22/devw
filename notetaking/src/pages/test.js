import React, { useEffect, useState } from 'react'

function test() {


    const [message, setMessage] = useState("Loading");

    useEffect(() => {
        fetch("http://127.0.0.1:3000/api/home").then(
            response => response.json()
        ).then(
            data => {
                setMessage(data.message);
            }
        );
    }, []);

    return (
    <h1>{message}</h1>
  )
}

export default test