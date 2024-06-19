import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const Video = () => {
    const { id } = useParams();
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        setLoading(true);
        setTimeout(() => {
            setLoading(false);
        }, 1000);
    }, [id]);

    if (loading) {
        return <h1>Loading...</h1>;
    }

    return (
        <div>
            <h1>Video: {id}</h1>
        </div>
    );
};

export default Video;
