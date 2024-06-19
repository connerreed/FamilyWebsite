import React from 'react'
import { Link } from 'react-router-dom'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'

const Pictures = () => {
    const pictures = [
        {id: 1, imageSrc: "https://picsum.photos/200/300", user: "Conner Reed"},
        {id: 2, imageSrc: "https://picsum.photos/200/300", user: "Lance Reed"},
        {id: 3, imageSrc: "https://picsum.photos/200/300", user: "Linda Reed"},
        {id: 4, imageSrc: "https://picsum.photos/200/300", user: "Kathryn Rosenberg"},
        {id: 5, imageSrc: "https://picsum.photos/200/300", user: "User 5"},
        {id: 6, imageSrc: "https://picsum.photos/200/300", user: "User 6"}

    ];
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