import { useState } from "react";
import React from "react";
import './css/LoginComponent.css';
import bg from '../components/bg.png';

function Register()
{
    const [username,setUsername]=useState("");
    const [password,setPassword]=useState("");
    const [firstname,setFirstname]=useState("");
    const [lastname,setLastname]=useState("");

    function add(e) {
        e.preventDefault();
        console.log({username:username});
        const url = 'http://127.0.0.1:8000/register/';
        const res = fetch(url,{method:"POST", headers : { 'Content-Type':'application/json' ,'Accept':'application/json' },body:JSON.stringify({username:username,password:password,first_name:firstname,last_name:lastname})});
    }


    return(
        <body style={{ backgroundImage: 'url('+bg+')' , backgroundSize: "cover",position: "absolute",width:'100%',height: '100%',left: '0%',top: '0%'}}>
            <div>
                <div className="input">
                <p style={{color: "white", left: "15%" ,top: "8%",position: "absolute",fontSize: "250%"}}>APRIL AI Image</p>
                    <p style={{color: "white", left: "15%" ,top: "15%",position: "absolute",fontSize: "250%"}}>Analysis Software</p>
                    <input type="text" placeholder="Username" name="username" value={username} onChange={(e) => setUsername(e.target.value)} style={{top: "17%"}} /><br></br>
                    <input type="password" placeholder="Password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} style={{top: "25%"}} /><br></br>
                    <input type="text" placeholder="Firstname" name="firstname" value={firstname} onChange={(e) => setFirstname(e.target.value)} style={{top: "33%"}} /><br></br>
                    <input type="text" placeholder="Lastname" name="lastname" value={lastname} onChange={(e) => setLastname(e.target.value)} style={{top: "41%"}} /><br></br>
                </div>
                <button className="btn" onClick={add} style={{top:"53%"}}>REGISTER</button>
                
            </div>
        </body>
    )

}
export default Register;