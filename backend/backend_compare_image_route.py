
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/compare-image")
async def generate_comparison_image(payload: dict):
    def draw_bike(ax, label, head_angle, stack, stem_length, stem_angle, bar_reach, bar_drop, color):
        headtube_length = 100
        head_angle_rad = np.radians(90 - head_angle)

        head_start = np.array([0, 0])
        head_end = head_start + np.array([-headtube_length * np.cos(head_angle_rad), headtube_length * np.sin(head_angle_rad)])

        head_dir = (head_end - head_start) / np.linalg.norm(head_end - head_start)
        stack_top = head_end + head_dir * stack

        stem_rad = np.radians(stem_angle)
        stem_end = stack_top + np.array([stem_length * np.cos(stem_rad), stem_length * np.sin(stem_rad)])

        bar_end = stem_end + np.array([bar_reach, -bar_drop])

        ax.plot([head_start[0], head_end[0]], [head_start[1], head_end[1]], color='black', lw=3, label='Headtube' if label == "Bike 1" else "")
        ax.plot([head_end[0], stack_top[0]], [head_end[1], stack_top[1]], color='gold', lw=3, label='Stack' if label == "Bike 1" else "")
        ax.plot([stack_top[0], stem_end[0]], [stack_top[1], stem_end[1]], color=color, lw=3, label=f'{label} Stem')
        ax.plot([stem_end[0], bar_end[0]], [stem_end[1], bar_end[1]], color=color, lw=2, linestyle='dashed', label=f'{label} Bars')

        return bar_end

    b1 = payload["bike1"]
    b2 = payload["bike2"]

    fig, ax = plt.subplots(figsize=(8, 6))

    bar1 = draw_bike(ax, "Bike 1", **b1, color='blue')
    bar2 = draw_bike(ax, "Bike 2", **b2, color='red')

    ax.plot([bar1[0], bar2[0]], [bar1[1], bar2[1]], color='gray', linestyle='dotted')
    ax.text((bar1[0]+bar2[0])/2, (bar1[1]+bar2[1])/2,
            f"Δ Reach: {round(bar2[0]-bar1[0], 1)} mm\nΔ Drop: {round(bar2[1]-bar1[1], 1)} mm",
            fontsize=10, ha='center', va='bottom', bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray"))

    ax.set_aspect('equal')
    ax.set_xlim(-300, 300)
    ax.set_ylim(-200, 250)
    ax.axis('off')
    ax.set_title("Bike Handlebar Position Comparison")
    ax.legend()

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    return JSONResponse(content={"image_base64": img_base64})
