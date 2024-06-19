import "./css/App.css";
import { HashRouter, Route, Routes } from "react-router-dom";
import CustomNavbar from "./components/CustomNavbar";
import Home from "./components/Home";
import Login from "./components/Login";
import PictureGallery from "./components/PictureGallery";
import Picture from "./components/Picture";
import RecipeGallery from "./components/RecipeGallery";
import Recipe from "./components/Recipe";
import VideoGallery from "./components/VideoGallery";
import Video from "./components/Video";

function App() {
    return (
        <HashRouter>
            <div className="App bg-dark">
                <CustomNavbar />
                <div className="content">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/recipes" element={<RecipeGallery />} />
                        <Route path="/recipes/:id" element={<Recipe />} />
                        <Route path="/pictures" element={<PictureGallery />} />
                        <Route path="/pictures/:id" element={<Picture />} />
                        <Route path="/videos" element={<VideoGallery />} />
                        <Route path="/videos/:id" element={<Video />} />
                        <Route path="/login" element={<Login />} />
                    </Routes>
                </div>
            </div>
        </HashRouter>
    );
}

export default App;
