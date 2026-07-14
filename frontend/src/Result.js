import React from "react";

function Result({ data }) {
  return (
    <div className="result-card">
      <h2>Resultado</h2>

      {data.error ? (
        <p style={{ color: "red" }}>{data.error}</p>
      ) : (
        <>
          <p><strong>Nombre:</strong> {data.nombre}</p>
          <p><strong>Código:</strong> {data.codigo}</p>
          <p><strong>Carrera:</strong> {data.carrera}</p>
          <p><strong>Ciclo:</strong> {data.ciclo}</p>
          <p><strong>Confianza:</strong> {Math.round(data.confianza * 100)}%</p>
        </>
      )}
    </div>
  );
}

export default Result;
