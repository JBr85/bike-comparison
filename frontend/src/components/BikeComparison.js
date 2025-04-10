import React, { useState, useEffect } from "react";
import axios from "axios";
import BikeVisualization from "./BikeVisualization";
import BikeComparisonImage from "./BikeComparisonImage";

const BikeComparison = () => {
    const [frames, setFrames] = useState([]);
    const [stems, setStems] = useState([]);
    const [handlebars, setHandlebars] = useState([]);

    // Bike 1 State
    const [selectedFrame1, setSelectedFrame1] = useState(null);
    const [selectedStem1, setSelectedStem1] = useState(null);
    const [invertStem1, setInvertStem1] = useState(false);
    const [selectedHandlebar1, setSelectedHandlebar1] = useState(null);
    const [stackHeight1, setStackHeight1] = useState("");

    // Bike 2 State
    const [selectedFrame2, setSelectedFrame2] = useState(null);
    const [selectedStem2, setSelectedStem2] = useState(null);
    const [invertStem2, setInvertStem2] = useState(false);
    const [selectedHandlebar2, setSelectedHandlebar2] = useState(null);
    const [stackHeight2, setStackHeight2] = useState("");

    // Fetch data from FastAPI
    // Fetch data from FastAPI
    useEffect(() => {
        axios.get(`${process.env.REACT_APP_API_URL}/components/frames`)
            .then(res => setFrames(res.data))
            .catch(error => console.error("Error fetching frames:", error));

        axios.get(`${process.env.REACT_APP_API_URL}/components/stems`)
            .then(res => setStems(res.data))
            .catch(error => console.error("Error fetching stems:", error));

        axios.get(`${process.env.REACT_APP_API_URL}/components/handlebars`)
            .then(res => setHandlebars(res.data))
            .catch(error => console.error("Error fetching handlebars:", error));
    }, []);


    return (
        <div>
            <h2>Bike Setup Comparison</h2>

            <div style={{ display: "flex", justifyContent: "space-around" }}>
                {/* Bike 1 */}
                <div>
                    <h3>Bike 1 (Blue)</h3>
                    <label>Frame: </label>
                    <select onChange={(e) => setSelectedFrame1(frames.find(f => f.id === parseInt(e.target.value)))} >
                        <option value="">Select a frame</option>
                        {frames.map((frame) => (
                            <option key={frame.id} value={frame.id}>
                                {frame.make} - {frame.size}
                            </option>
                        ))}
                    </select>

                    <br />

                    <label>Stem: </label>
                    <select onChange={(e) => {
                        const selectedStem = stems.find(s => s.id === parseInt(e.target.value));
                        setSelectedStem1(selectedStem);
                    }}>
                        <option value="">Select a stem</option>
                        {stems.map((stem) => (
                            <option key={stem.id} value={stem.id}>
                                {stem.make} - {stem.length}mm, {invertStem1 ? -stem.angle : stem.angle}°
                            </option>
                        ))}
                    </select>

                    <label>
                        <input
                            type="checkbox"
                            checked={invertStem1}
                            onChange={() => setInvertStem1(!invertStem1)}
                        /> Invert Stem
                    </label>

                    <br />

                    <label>Handlebar: </label>
                    <select onChange={(e) => setSelectedHandlebar1(handlebars.find(h => h.id === parseInt(e.target.value)))}>
                        <option value="">Select a handlebar</option>
                        {handlebars.map((bar) => (
                            <option key={bar.id} value={bar.id}>
                                {bar.make} - {bar.width}mm, Reach {bar.reach}mm, Drop {bar.drop}mm
                            </option>
                        ))}
                    </select>

                    <br />

                    <label>Stack Height (mm): </label>
                    <input
                        type="number"
                        value={stackHeight1}
                        onChange={(e) => setStackHeight1(e.target.value)}
                        placeholder="Enter stack height"
                    />
                </div>

                {/* Bike 2 */}
                <div>
                    <h3>Bike 2 (Red)</h3>
                    <label>Frame: </label>
                    <select onChange={(e) => setSelectedFrame2(frames.find(f => f.id === parseInt(e.target.value)))} >
                        <option value="">Select a frame</option>
                        {frames.map((frame) => (
                            <option key={frame.id} value={frame.id}>
                                {frame.make} - {frame.size}
                            </option>
                        ))}
                    </select>

                    <br />

                    <label>Stem: </label>
                    <select onChange={(e) => {
                        const selectedStem = stems.find(s => s.id === parseInt(e.target.value));
                        setSelectedStem2(selectedStem);
                    }}>
                        <option value="">Select a stem</option>
                        {stems.map((stem) => (
                            <option key={stem.id} value={stem.id}>
                                {stem.make} - {stem.length}mm, {invertStem2 ? -stem.angle : stem.angle}°
                            </option>
                        ))}
                    </select>

                    <label>
                        <input
                            type="checkbox"
                            checked={invertStem2}
                            onChange={() => setInvertStem2(!invertStem2)}
                        /> Invert Stem
                    </label>

                    <br />

                    <label>Handlebar: </label>
                    <select onChange={(e) => setSelectedHandlebar2(handlebars.find(h => h.id === parseInt(e.target.value)))}>
                        <option value="">Select a handlebar</option>
                        {handlebars.map((bar) => (
                            <option key={bar.id} value={bar.id}>
                                {bar.make} - {bar.width}mm, Reach {bar.reach}mm, Drop {bar.drop}mm
                            </option>
                        ))}
                    </select>

                    <br />

                    <label>Stack Height (mm): </label>
                    <input
                        type="number"
                        value={stackHeight2}
                        onChange={(e) => setStackHeight2(e.target.value)}
                        placeholder="Enter stack height"
                    />
                </div>
            </div>

            {/* Bike Visualization */}
            <BikeVisualization
                frame1={selectedFrame1}
                stem1={selectedStem1 ? { ...selectedStem1, angle: invertStem1 ? -selectedStem1.angle : selectedStem1.angle } : null}
                handlebar1={selectedHandlebar1}
                stackHeight1={stackHeight1}
                frame2={selectedFrame2}
                stem2={selectedStem2 ? { ...selectedStem2, angle: invertStem2 ? -selectedStem2.angle : selectedStem2.angle } : null}
                handlebar2={selectedHandlebar2}
                stackHeight2={stackHeight2}
            />
            
            <BikeComparisonImage
    bike1={
        selectedFrame1 && selectedStem1 && selectedHandlebar1
            ? {
                  head_angle: selectedFrame1.head_angle,
                  stack: parseFloat(stackHeight1 || 0),
                  stem_length: selectedStem1.length,
                  stem_angle: invertStem1 ? -selectedStem1.angle : selectedStem1.angle,
                  bar_reach: selectedHandlebar1.reach,
                  bar_drop: selectedHandlebar1.drop,
              }
            : null
    }
    bike2={
        selectedFrame2 && selectedStem2 && selectedHandlebar2
            ? {
                  head_angle: selectedFrame2.head_angle,
                  stack: parseFloat(stackHeight2 || 0),
                  stem_length: selectedStem2.length,
                  stem_angle: invertStem2 ? -selectedStem2.angle : selectedStem2.angle,
                  bar_reach: selectedHandlebar2.reach,
                  bar_drop: selectedHandlebar2.drop,
              }
            : null
    }
/>



        </div>
    );
};

export default BikeComparison;
