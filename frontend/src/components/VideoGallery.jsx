import React from "react";
import { Link } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";

const VideoGallery = () => {
    const videos = [
        {
            id: 1,
            videoSrc: "https://picsum.photos/200/300",
            user: "Conner Reed",
        },
        {
            id: 2,
            videoSrc: "https://picsum.photos/200/300",
            user: "Lance Reed",
        },
        {
            id: 3,
            videoSrc: "https://picsum.photos/200/300",
            user: "Linda Reed",
        },
        {
            id: 4,
            videoSrc: "https://picsum.photos/200/300",
            user: "Kathryn Rosenberg",
        },
        { id: 5, videoSrc: "https://picsum.photos/200/300", user: "User 5" },
        { id: 6, videoSrc: "https://picsum.photos/200/300", user: "User 6" },
    ];
    return (
        <Container>
            <Row>
                {videos.map((video) => (
                    <Col key={video.id} md={4} className="mb-4">
                        <Link
                            to={`/videos/${video.id}`}
                            style={{ textDecoration: "none" }}
                        >
                            <Card bg="secondary">
                                <Card.Img variant="top" src={video.videoSrc} />
                                <Card.Body>
                                    <Card.Title>
                                        Uploaded by:
                                        <br />
                                        {video.user}
                                    </Card.Title>
                                </Card.Body>
                            </Card>
                        </Link>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default VideoGallery;
