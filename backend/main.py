from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Frame, Stem, Handlebar

app = FastAPI()

# ✅ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/components/frames")
def get_frames(db: Session = Depends(get_db)):
    return db.query(Frame).all()

@app.get("/components/stems")
def get_stems(db: Session = Depends(get_db)):
    return db.query(Stem).all()

@app.get("/components/handlebars")
def get_handlebars(db: Session = Depends(get_db)):
    return db.query(Handlebar).all()

@app.post("/geometry-image")
async def generate_comparison_image(request: Request):
    data = await request.json()
    bike1 = data.get("bike1")
    bike2 = data.get("bike2")

    if not bike1 or not bike2:
        return JSONResponse(status_code=400, content={"error": "Missing bike data"})

    def draw_bike(ax, color, head_angle, stack, stem_length, stem_angle, bar_reach, bar_drop, label):
        origin = np.array([0, 0])
        headtube_angle = 90 - head_angle
        headtube_rad = np.radians(headtube_angle)

        headtube_length = 100
        headtube_end = origin + headtube_length * np.array([-np.sin(headtube_rad), np.cos(headtube_rad)])
        ax.plot([origin[0], headtube_end[0]], [origin[1], headtube_end[1]], color=color, linewidth=2, label=f"{label} Headtube")

        stack_vector = (stack / headtube_length) * (headtube_end - origin)
        stack_end = headtube_end + stack_vector
        ax.plot([headtube_end[0], stack_end[0]], [headtube_end[1], stack_end[1]], color=color, linewidth=2)

        stem_rad = np.radians(stem_angle)
        stem_vector = np.array([stem_length * np.cos(stem_rad), stem_length * np.sin(stem_rad)])
        stem_end = stack_end + stem_vector
        ax.plot([stack_end[0], stem_end[0]], [stack_end[1], stem_end[1]], color=color, linewidth=2, label=f"{label} Stem")

        bar_end = stem_end + np.array([bar_reach, -bar_drop])
        ax.plot([stem_end[0], bar_end[0]], [stem_end[1], bar_end[1]], color=color, linestyle='dashed', linewidth=2, label=f"{label} Bars")

    fig, ax = plt.subplots(figsize=(8, 6))
    draw_bike(ax, 'blue', **bike1, label="Bike 1")
    draw_bike(ax, 'red', **bike2, label="Bike 2")

    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_aspect('equal')
    ax.set_title("Front-End Bike Geometry Comparison")
    ax.set_xlabel("Horizontal (mm)")
    ax.set_ylabel("Vertical (mm)")
    ax.legend()
    ax.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    return JSONResponse(content={"image_base64": img_base64})
