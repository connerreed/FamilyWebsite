import "./css/App.css";
import { HashRouter, Route, Routes } from "react-router-dom";
import CustomNavbar from "./components/CustomNavbar";
import Home from "./components/Home";
import Login from "./components/Login";
import Pictures from "./components/Pictures";
import Recipes from "./components/Recipes";
import Videos from "./components/Videos";
import "bootstrap/dist/css/bootstrap.min.css";


function App() {
    return (
        <HashRouter>
            <div className="App">
                <CustomNavbar />
                <div className="content">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/recipes" element={<Recipes />} />
                        <Route path="/pictures" element={<Pictures />} />
                        <Route path="/videos" element={<Videos />} />
                        <Route path="/login" element={<Login />} />
                    </Routes>
                </div>
            </div>
        </HashRouter>
    );
}

export default App;
