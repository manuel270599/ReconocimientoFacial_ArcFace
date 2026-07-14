import React, { useState } from "react";
import "./App.css";  
import "./styles.css";
import UploadForm from "./UploadForm";
import Result from "./Result";
import LoadingBar from "./LoadingBar";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <>
  
        <div className="app-container">
          <h1 className="titulo-principal">ArcFace UNI</h1>
        </div>
        <img src="/FacultaddeCienciasUNI.png" alt="UNI" />
        <div className="features">
        <div >
             Reconocimiento Facial
        </div>

        <div>
             Procesamiento Rápido
        </div>

        <div>
             Alta Precisión
        </div>
          </div>
        <div className="form">
          <UploadForm setResult={setResult} setLoading={setLoading} />
          {loading && <LoadingBar />}
          {result && <Result data={result} />}
        </div>
        <div className="app-container2">
          <h2>Acerca del Proyecto</h2>
        <div>
          <p className="creditos2">
            ArcFace UNI es una plataforma de reconocimiento facial basada en
            Inteligencia Artificial que permite identificar y comparar rostros
            mediante técnicas avanzadas de Visión por Computadora.
          </p>
        </div>

          <p className="creditos2">
            Desarrollado con React, Python y ArcFace como proyecto académico
            orientado a la investigación y aplicación de tecnologías biométricas como parte del curso Proyecto de tesis I.
          </p>
        </div>

        <footer className="footer">
        <div className="footer-container">
          
          {/* Columna 1: Sobre Nosotros */}
          <div className="footer-column">
            <h3>Facultad de Ciencias</h3>
            <p>Escuela de Ciencia de la computación</p>
          </div>

          {/* Columna 2: Contacto Directo */}
          <div className="footer-column">
            <h3>Contacto</h3>
            <p> Lima, Perú</p>
            <p> <a href="tel:+51980986446">+51 980986446</a></p>
            <p> <a href="mailto:josemontalvo659@gmail.com">josemontalvo659@gmail.com</a></p>
          </div>

          {/* Columna 3: Enlaces Rápidos */}
          <div className="footer-column">
            <h3>Enlaces</h3>
            <ul>
              <li><a href="#inicio">Inicio</a></li>
              <li><a href="#servicios">Servicios</a></li>
              <li><a href="#privacidad">Política de Privacidad</a></li>
            </ul>
          </div>

        </div>
        
        {/* Barra Inferior de Derechos */}
        <div className="footer-bottom">
          <p>&copy; {new Date().getFullYear()} ArcFace. Todos los derechos reservados.</p>
        </div>
      </footer>

      <div  className="creditos">
          <footer>
              <p><small>Creditos a la Escuela de Ciencia de la computación de la Facultad de Ciencias de la <a href="https://portal.uni.edu.pe/">Universidad Nacional de Ingeniería</a></small> </p>
          </footer>

      </div>
    </>


  );
}

export default App;
