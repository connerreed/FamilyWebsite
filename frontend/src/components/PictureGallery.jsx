import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'

const Pictures = () => {
    const [loading, setLoading] = useState(false);

    const pictures = [
        {id: 1, imageSrc: "https://picsum.photos/200/300", user: "User 1"},
        {id: 2, imageSrc: "https://picsum.photos/200/300", user: "User 2"},
        {id: 3, imageSrc: "https://picsum.photos/200/300", user: "User 3"},
        {id: 4, imageSrc: "https://picsum.photos/200/300", user: "User 4"},
        {id: 5, imageSrc: "https://picsum.photos/200/300", user: "User 5"},
        {id: 6, imageSrc: "https://picsum.photos/200/300", user: "User 6"}
    ];



    useEffect(() => {
        setLoading(true);
        setTimeout(() => {
            setLoading(false);
        }, 1000);
    }, {pictures});

    if (loading) {
        return <h1>Loading...</h1>;
    }

    return (
        <Container>
            <Row>
                {pictures.map((picture) => (
                    <Col key={picture.id} md={4} className="mb-4">
                        <Link to={`/pictures/${picture.id}`} style={{textDecoration: "none"}}>
                        <Card bg="secondary">
                            <Card.Img variant="top" src={picture.imageSrc} />
                            <Card.Body>
                                <Card.Title>Uploaded by:<br/>{picture.user}</Card.Title>
                            </Card.Body>
                        </Card>
                        </Link>
                    </Col>
                ))}
            </Row>
        </Container>
    )
}

export default Pictures