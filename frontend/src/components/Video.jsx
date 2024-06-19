import React from 'react'
import { useParams } from 'react-router-dom'

const Video = () => {
    const { id } = useParams()

    return (
        <div>
            <h1>Video: {id}</h1>
        </div>
    )
}

export default Video