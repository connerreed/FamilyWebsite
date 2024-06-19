import React from "react";
import { Link } from "react-router-dom";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";

const Recipes = () => {
    const recipes = [
        {
            id: 1,
            title: "Recipe 1",
            description:
                "Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora corporis iusto autem quibusdam magnam porro quisquam, aspernatur quaerat animi dicta quae perspiciatis optio nam dolores. Vitae quod doloremque incidunt accusantium?",
            imageSrc: "https://picsum.photos/200/300",
        },
        {
            id: 2,
            title: "Recipe 2",
            description: "This is recipe 2",
            imageSrc: "https://picsum.photos/200/300",
        },
        {
            id: 3,
            title: "Recipe 3",
            description: "This is recipe 3",
            imageSrc: "https://picsum.photos/200/300",
        },
        {
            id: 4,
            title: "Recipe 4",
            description: "This is recipe 4",
            imageSrc: "https://picsum.photos/200/300",
        },
        {
            id: 5,
            title: "Recipe 5",
            description: "This is recipe 5",
            imageSrc: "https://picsum.photos/200/300",
        },
        {
            id: 6,
            title: "Recipe 6",
            description: "This is recipe 6",
            imageSrc: "https://picsum.photos/200/300",
        },
    ];

    return (
        <Container>
            <Row>
                {recipes.map((recipe) => (
                    <Col key={recipe.id} md={4} className="mb-4">
                        <Link to={`/recipes/${recipe.id}`} style={{textDecoration: "none"}}>
                            <Card bg="secondary">
                                <Card.Img variant="top" src={recipe.imageSrc} />
                                <Card.Body>
                                    <Card.Title>{recipe.title}</Card.Title>
                                    <Card.Text>{recipe.description}</Card.Text>
                                </Card.Body>
                            </Card>
                        </Link>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default Recipes;
