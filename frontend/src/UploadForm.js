import React, { useState } from "react";

function UploadForm({ setResult, setLoading }) {
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file); 

    const res = await fetch("http://127.0.0.1:5000/upload", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <form onSubmit={handleSubmit} className="upload-form">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button type="submit">Subir Foto</button>
    </form>
  );
}

export default UploadForm;
