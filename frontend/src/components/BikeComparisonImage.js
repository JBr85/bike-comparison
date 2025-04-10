import React, { useEffect, useState } from "react";

const BikeComparisonImage = ({ bike1, bike2 }) => {
    const [imageBase64, setImageBase64] = useState(null);

    useEffect(() => {
        if (!bike1 || !bike2) return;

        // IMPORTANT: Use backticks around process.env!
        fetch(`${process.env.REACT_APP_API_URL}/geometry-image`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ bike1, bike2 }),
        })
            .then((res) => res.json())
            .then((data) => {
                setImageBase64(data.image_base64);
            })
            .catch((err) => console.error("Error fetching geometry image:", err));
    }, [bike1, bike2]);

    return (
        <div style={{ textAlign: "center", marginTop: "30px" }}>
            <h3>Front-End Geometry Visual</h3>
            {imageBase64 ? (
                <img
                    // Use backticks + interpolation:
                    src={`data:image/png;base64,${imageBase64}`}
                    alt="Geometry Comparison"
                    style={{ maxWidth: "100%", border: "1px solid #ccc" }}
                />
            ) : (
                <p>Loading geometry image...</p>
            )}
        </div>
    );
};

export default BikeComparisonImage;
