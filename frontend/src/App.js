import "./App.css";
import axios from "axios";
import { useState } from "react";

function App() {

  const [image, setImage] = useState(null);

  const [preview, setPreview] = useState("");

  const [caption, setCaption] = useState("");

  const [hashtags, setHashtags] = useState([]);

  const [loading, setLoading] = useState(false);


  const handleImageChange = (e) => {

    const file = e.target.files[0];

    setImage(file);

    setPreview(URL.createObjectURL(file));
  };


  const handleUpload = async () => {

    if (!image) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();

    formData.append("file", image);

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/upload-image",
        formData
      );

      setCaption(response.data.caption);

      setHashtags(response.data.hashtags);

    } catch (error) {

      console.log(error);

      alert("Error uploading image");
    }

    setLoading(false);
  };


  return (

    <div className="container">

      <div className="hero">
  <span className="badge">✨ AI Powered</span>

  <h1>Image Caption Generator</h1>

  <p>
    Generate Captions & Hashtags Instantly
  </p>
</div>

      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
      />

      {
        preview && (
          <img
            src={preview}
            alt="preview"
            className="preview-image"
          />
        )
      }

      <button onClick={handleUpload}>
        {
          loading ? "AI is generating..." : "Generate Caption"
        }
      </button>

      {
        caption && (
          <div className="result">

            <h2>Caption</h2>

            <p>{caption}</p>

            <h2>Hashtags</h2>

            <div className="hashtags">

              {
                hashtags.map((tag, index) => (
                  <span key={index}>{tag}</span>
                ))
              }

            </div>

          </div>
        )
      }

    </div>
  );
}

export default App;