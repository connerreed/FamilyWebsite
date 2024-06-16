import "./css/App.css";
import { HashRouter, Route, Routes } from "react-router-dom";
import CustomNavbar from "./components/CustomNavbar";
import Home from "./components/Home";
import "bootstrap/dist/css/bootstrap.min.css";


function App() {
    return (
        <HashRouter>
            <div className="App">
                <CustomNavbar />
                <div className="content">
                    <Routes>
                        <Route path="/" element={<Home />} />
                    </Routes>
                </div>
            </div>
        </HashRouter>
    );
}

export default App;
