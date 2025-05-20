from database import SessionLocal, Frame

# Create a session
db = SessionLocal()

# List of new frames to insert
frames = [
    {"make": "Stromm Track", "size": "Small", "reach": 400, "stack": 480, "top_tube": None, "head_angle": 73.5, "seat_angle": 74, "head_tube": None, "chainstay": None, "wheelbase": 940.7, "front_centre": 565.7, "bb_drop": None, "fork_rake": 40},
    {"make": "Stromm Track", "size": "Medium", "reach": 425, "stack": 500, "top_tube": None, "head_angle": 73.5, "seat_angle": 74, "head_tube": None, "chainstay": None, "wheelbase": 971.6, "front_centre": 596.6, "bb_drop": None, "fork_rake": 40},
    {"make": "Stromm Track", "size": "Large", "reach": 450, "stack": 520, "top_tube": None, "head_angle": 73.5, "seat_angle": 74, "head_tube": None, "chainstay": None, "wheelbase": 1002.6, "front_centre": 627.6, "bb_drop": None, "fork_rake": 40},
    {"make": "Stromm Track", "size": "Extra Large", "reach": 466, "stack": 540, "top_tube": None, "head_angle": 73.5, "seat_angle": 74, "head_tube": None, "chainstay": None, "wheelbase": 1024.5, "front_centre": 649.5, "bb_drop": None, "fork_rake": 40}
]

# Insert frames into the database
for frame_data in frames:
    frame = Frame(**frame_data)
    db.add(frame)

# Commit changes
db.commit()
db.close()

print("✅ Stromm frames inserted successfully!")
