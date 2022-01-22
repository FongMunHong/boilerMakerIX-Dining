import './App.css';
import{useState, useEffect} from 'react';

function App() {

  const [articles, setArticles] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1/get', {
      'methods':'GET',
      headers: {
        'Content-Type': 'applications/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => console.log(resp))
    .catch(error => console.log(error))

  },[])

  return (
    <div className="App">
      <h1>Purdue Dining Menu</h1>
    </div>
  );
}

export default App;
