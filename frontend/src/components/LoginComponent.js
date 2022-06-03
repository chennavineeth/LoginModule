import React from "react";
import { useState } from "react";
import './css/LoginComponent.css';
import  Register from './RegisterComponent';
import { useNavigate } from 'react-router-dom';
import bg from '../components/bg.png';

function Login() {
    const [username,setUsername]=useState("");
    const [password,setPassword]=useState("");

    let navigate = useNavigate();
    //comment

    function goToRegister(e) {
        e.preventDefault();
        navigate("/register");
    };

    function Display(e){
        e.preventDefault();
        const url='http://127.0.0.1:8000/token/';
        const res= fetch(url,{method:"POST" , headers : { 'Content-Type':'application/json' ,'Accept':'application/json' },body:JSON.stringify({username:username,password:password}) } )
        .then(response => response.json()).then(data => { console.log(data)});
        console.log({username:username,password:password});
    };


    return (
            <div style={{ backgroundImage:'url('+bg+')' , backgroundSize: "cover",position: "absolute",width:'100%',height: '100%',left: '0%',top: '0%'}} >
                <div>
                    <p style={{color: "white", left: "15%" ,top: "8%",position: "absolute",fontSize: "250%"}}>APRIL AI Image</p>
                    <p style={{color: "white", left: "15%" ,top: "15%",position: "absolute",fontSize: "250%"}}>Analysis Software</p>
                    <input type="text"  name="username" value={username} onChange={(e) => setUsername(e.target.value)} className="input" placeholder="&#xF002;  Username Name" style={{top:'17%'}} /> <br></br>
                    <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}  className="input"  placeholder='&#xF002;  Password' style={{ top:'25%'}}/>
                    
                    <div  
                        style={{ color:'white',position:'absolute',top:'30%',left:'67%',maxWidth:'100%' }}>
                        <p ><a style={{color: "white",fontSize:'90%'}} href='http://127.0.0.1:8000/register/'>Forget Password?</a></p>
                    </div> 
                    <button className="btn"  onClick={Display} >LOG IN</button>
                    <button  className="btn" style={{top: "50%"}} onClick={goToRegister}>REGISTER</button>      
                </div>
            </div>
    )
};
export default Login;