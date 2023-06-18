import './App.css';
import axios from 'axios'
import React, {useState} from "react";

function App() {
  const [text, setText] = useState("없음");

  const clicked = () => {
    axios.get("http://localhost:3000/testapi/member/")
    .then(response => console.log(response.data))
  }

  return (
    <div>
      <h1>{text}</h1>
      <button onClick={clicked}> 클릭 </button>
    </div>
  );
}

export default App;
