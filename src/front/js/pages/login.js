import React, { useContext, useState, useEffect } from "react";
import { Context } from "../store/appContext";
import { useNavigate, Link } from "react-router-dom";
import "../../styles/home.css";
import CustomModal from "../component/customModal";
import { useModal } from "../hooks/UseModal";

const Login = () => {
  const { store, actions } = useContext(Context);
  const [data, setData] = useState({});
	const [mensaje, setMensaje] = useState(null); 
  const navigate = useNavigate();
  const [isModalOpened, setIsModalOpened, toggleModal] = useModal(false);

  const handleClick = () => {
    actions.login(data.email, data.password).then((response) => {
    if (response) navigate("/");
    else{ setMensaje("Las credenciales no son correctas");
          toggleModal();
        } 
    })
  };

  useEffect(() => {
    if (store.token && store.token != "" && store.token != undefined) {
      navigate("/");
    }
  }, []);

  const handleChange = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };
    
  return (
    <div className="vh-100 gradient-custom">
      <div className="container text-center">
        <h1>¡Hola de nuevo!</h1>
        <h5 className="mb-5">Bienvenido de nuevo a tu app.</h5>
        <div className="row d-flex justify-content-center align-items-center h-100">
          <div className="col-12 col-md-8 col-lg-6 col-xl-5">
            <div className="card" id="card">
              <div className="card-body text-center">
              </div>
              <div className="form-outline">
                <div className="row d-flex justify-content-center align-items-center h-100">
                    <div className="col-md-11">
                      <label className="form-label alinear-izquierda" htmlFor="typeEmailX">
                        Dirección de correo electrónico
                      </label>
                      <input
                        type="text"
                        id="typeEmailX-2"
                        className="form-control mb-2 me-2"
                        name="email"
                        onChange={handleChange}
                      />
                      <label className="form-label alinear-izquierda" htmlFor="typeEmailX">
                        Contraseña
                      </label>
                      <input
                        type="password"
                        id="typePasswordX-2"
                        name="password"
                        className="form-control mb-2 me-2"
                        onChange={handleChange}
                      />
                      <p className="small mt-2 alinear-izquierda2">
                      <a href="#!">¿Olvidaste la contraseña?</a>
                      </p>
                      <div className="form-check alinear-izquierda2">
                      <input  className="form-check-input"
                              type="checkbox"
                              value=""
                              id="invalidCheck"
                              required
                      />
                      <label className="form-check-label alinear-izquierda2"> Confirmo que he leido y acepto la Política de Privacidad y Aviso Legal.</label>
                      <div className="invalid-feedback">Por favor, confirma que has leido y aceptas la Política de Privacidad y Aviso Legal.</div>
                      </div>
                      <button
                        className="col-md-12 btn-lg px-5 mb-3 mt-3"
                        onClick={handleClick}
                        id="button"
                      >
                        Iniciar Sesión
                      </button>
                    </div>
                  <div>
                      <p className="ms-3 me-3 mb-3 text-center">
                      ¿No tienes una cuenta?
                      <p className="ms-3 me-3 mt-3 text-center">
                      <Link to="/signupUser">
                      <strong className="strong "> Registrate </strong>
                      </Link>
                      para descubrir lo mejor de Baby Friendly</p>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <CustomModal  show={isModalOpened}
                    titulo="Login en BabyFriendly"
                    handleClose={() => setIsModalOpened(false)}>
        <div>{mensaje}</div>
      </CustomModal>
    </div>
  );
};

export default Login;
