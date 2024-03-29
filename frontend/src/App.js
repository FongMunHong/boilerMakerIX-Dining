import './App.css';
import HomepageDataHandler from './homepageDataHandler'
import 'bootstrap/dist/css/bootstrap.min.css';
import React, {useState, useEffect} from 'react';
import FullMenuItem from './components/fullMenuItem';

function App() {

  const [articles, setArticles] = useState([])

  useEffect(() => {
    fetch("http://127.0.0.1:5000/get/01-22-2022/wiley/top3", {
      'methods':'GET',
      headers: {
        'Content-Type':'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    })
    .then(resp => resp.json())
    .then(resp => setArticles(resp))
    .catch(error => console.log(error))
  },[])

  return (
    <React.Fragment>
      <HomepageDataHandler 
        wileyData={articles.filter(c => c.court === 'wiley')} 
        earhartData={articles.filter(c => c.court === 'earhart')} 
        windsorData={articles.filter(c => c.court === 'windsor')}
        fordData={articles.filter(c => c.court === 'ford')}
        hillenbrandData={articles.filter(c => c.court === 'hillenbrand')}
      >
      </HomepageDataHandler>
    </React.Fragment>
  );
}

export default App;