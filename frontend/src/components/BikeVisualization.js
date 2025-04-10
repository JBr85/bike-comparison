import React, { useCallback } from "react";

const BikeVisualization = ({
    frame1, stem1, handlebar1, stackHeight1,
    frame2, stem2, handlebar2, stackHeight2}) => {

    const degToRad = (angle) => (angle * Math.PI) / 180;

    const calculateBarPosition = useCallback((frame, stem, handlebar, stackHeight) => {
        if (!frame || !stem || !handlebar) {
            return {
                effectiveReach: 0,
                totalDrop: 0,
                stemEnd: [0, 0],
                barEnd: [0, 0]
            };
        }

        const headTubeAngle = 90 - frame.head_angle;
        const fullStemAngle = degToRad(headTubeAngle + stem.angle);
        const stemLength = stem.length;
        const handlebarReach = handlebar.reach;
        const handlebarDrop = handlebar.drop;
        const adjustedStackHeight = parseFloat(stackHeight || 0);

        // Effective reach calculation
        const effectiveStemReach = stemLength * Math.cos(fullStemAngle);
        const effectiveReach = Math.round(frame.reach + effectiveStemReach + handlebarReach);

        // Effective drop calculation
        const effectiveStemStack = stemLength * Math.sin(fullStemAngle);
        const effectiveStack = Math.round(frame.stack + adjustedStackHeight + effectiveStemStack);
        const handlebarVerticalShift = handlebar.reach * Math.tan(degToRad(headTubeAngle));
        const totalDrop = Math.round(effectiveStack - handlebarDrop - handlebarVerticalShift);

        // Positions for drawing (if you need them)
        const stemEnd = [
            stemLength * Math.cos(fullStemAngle),
            adjustedStackHeight + stemLength * Math.sin(fullStemAngle)
        ];
        const barEnd = [stemEnd[0] + handlebarReach, stemEnd[1] - handlebarDrop];

        return { effectiveReach, totalDrop, stemEnd, barEnd };
    }, []);

    const bike1 = calculateBarPosition(frame1, stem1, handlebar1, stackHeight1);
    const bike2 = calculateBarPosition(frame2, stem2, handlebar2, stackHeight2);

    return (
        <div style={{ textAlign: "center", marginTop: "20px" }}>
            <h3><strong>Bike Geometry Comparison</strong></h3>
            <table style={{ width: "60%", margin: "0 auto", borderCollapse: "collapse" }}>
                <thead>
                    <tr>
                        <th style={tableHeaderStyle}></th>
                        <th style={tableHeaderStyle}>Bike 1</th>
                        <th style={tableHeaderStyle}>Bike 2</th>
                        <th style={tableHeaderStyle}>Difference</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style={tableCellStyle}><strong>Reach</strong></td>
                        <td style={tableCellStyle}>{bike1.effectiveReach} mm</td>
                        <td style={tableCellStyle}>{bike2.effectiveReach} mm</td>
                        <td style={tableCellStyle}>
                            <strong>{bike2.effectiveReach - bike1.effectiveReach} mm</strong>
                        </td>
                    </tr>
                    <tr>
                        <td style={tableCellStyle}><strong>Total Drop</strong></td>
                        <td style={tableCellStyle}>{bike1.totalDrop} mm</td>
                        <td style={tableCellStyle}>{bike2.totalDrop} mm</td>
                        <td style={tableCellStyle}>
                            <strong>{bike2.totalDrop - bike1.totalDrop} mm</strong>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
};

const tableHeaderStyle = {
    padding: "10px",
    borderBottom: "2px solid black",
    fontWeight: "bold",
    textAlign: "center",
    backgroundColor: "#f4f4f4"
};

const tableCellStyle = {
    padding: "10px",
    borderBottom: "1px solid #ddd",
    textAlign: "center"
};

export default BikeVisualization;
