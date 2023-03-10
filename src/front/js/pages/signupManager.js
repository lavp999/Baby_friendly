import React, { useState, useEffect, useContext } from "react";
import "../../styles/home.css";
import { useNavigate, Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const SignupManager = () => {
	const [formData, setFormData] = useState({tipo:"manager"});
	const [mensaje, setMensaje] = useState(null);
	const navigate = useNavigate();
	const { store, actions } = useContext(Context);

	const handleChange = (evento) =>{
		setFormData({...formData, [evento.target.name]: evento.target.value});
	}

	const handleSubmit = (evento)=>{
		evento.preventDefault(); // para evitar la recarga ya que cancela el evento

		fetch(process.env.BACKEND_URL + "/api/signup", 
			{method: 'POST',
			headers:{"Content-Type": "application/json"},
			body: JSON.stringify(formData),
			})
		.then(response => {
			if (response.status == 200){ 
				navigate("/login")
			}else{ 
				setMensaje(response["msg"])
			}
			return response.json();
		})
	}

	useEffect(()=>{
		if (store.token && store.token != "" && store.token != undefined) {
			navigate.push("/login");
		}
	  },[]);

	return (
		<div className="vh-100 gradient-custom">
		  <div className="container text-center">
			<div className="row d-flex justify-content-center align-items-center h-100">
			  <h3>¡Hola Gestor!</h3>
			  <p>Bienvenido a tu App para gestionar tus establecimientos</p>
				<div className="col-12 col-md-8 col-lg-6 col-xl-5">
				<div className="card px-3" id="card">
					<form onSubmit={handleSubmit}>
							<div className="form-group">
								<label className="alinear-izquierda mt-3" htmlFor="InputEmail1">Nombre y Apellidos</label>
								<input type="text" name="name" required className="form-control mb-2" id="InputName1" aria-describedby="nameHelp"  onChange={handleChange} />
							</div>
							<div className="form-group">
								<label className="alinear-izquierda" htmlFor="InputEmail1">Email</label>
								<input type="email" name="user" required className="form-control" id="InputEmail1" aria-describedby="emailHelp" onChange={handleChange} />
							</div>
							<div className="form-group">
								<label className="alinear-izquierda" htmlFor="InputPassword1">Contraseña</label>
								<input type="password" name="password" required className="form-control mt-2" id="InputPassword1" placeholder="Password" onChange={handleChange} />
							</div>
							
							<br/>
							<div>
                    		<p className="ms-3 me-3 mb-3 text-center">
                     		 ¿Ya tienes una cuenta?
							<Link to="/login">
                      		<strong className="strong">  Login</strong>
                      		</Link>
                    		</p>
                  			</div>
							<button className="mb-3 col-md-12 btn-lg px-5 mb-3 mt-3" type="submit"  id="button">Registrarme</button>
							{(mensaje != null) && <p>{mensaje}</p>}
					</form>	
						
				</div>							  
				</div>
			</div>
		  </div>
		</div>
	  );
};