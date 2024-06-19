import React from 'react'
import { useParams } from 'react-router-dom'

const Picture = () => {
    const { id } = useParams()

    return (
        <div>
            <h1>Picture: {id}</h1>
        </div>
    )
}

export default Picture