from database import SessionLocal, Frame

# Create a session
db = SessionLocal()

# List of new frames to insert
frames = [
    {"make": "Dolan DF5", "size": "51.5", "reach": 387.6, "stack": 475.3, "top_tube": 515, "head_angle": 72, "seat_angle": 75, "head_tube": 90, "chainstay": None, "wheelbase": None, "front_centre": None, "bb_drop": None, "fork_rake": None},
    {"make": "Dolan DF5", "size": "53", "reach": 400.1, "stack": 484.9, "top_tube": 530, "head_angle": 72.5, "seat_angle": 75, "head_tube": 100, "chainstay": None, "wheelbase": None, "front_centre": None, "bb_drop": None, "fork_rake": None},
    {"make": "Dolan DF5", "size": "55", "reach": 417.5, "stack": 494.5, "top_tube": 550, "head_angle": 73.5, "seat_angle": 75, "head_tube": 110, "chainstay": None, "wheelbase": None, "front_centre": None, "bb_drop": None, "fork_rake": None},
    {"make": "Dolan DF5", "size": "57", "reach": 435, "stack": 504.1, "top_tube": 570, "head_angle": 74, "seat_angle": 75, "head_tube": 120, "chainstay": None, "wheelbase": None, "front_centre": None, "bb_drop": None, "fork_rake": None},
    {"make": "Dolan DF5", "size": "59", "reach": 449.4, "stack": 524.7, "top_tube": 590, "head_angle": 74.5, "seat_angle": 75, "head_tube": 140, "chainstay": None, "wheelbase": None, "front_centre": None, "bb_drop": None, "fork_rake": None},
    {"make": "Dolan DF5", "size": "61", "reach": 453.6, "stack": 545.5, "top_tube": 610, "head_angle": 75, "seat_angle": 74, "head_tube": 160, "chainstay": None, "wheelbase": None, "front_centre": None, "bb_drop": None, "fork_rake": None}
]

# Insert frames into the database
for frame_data in frames:
    frame = Frame(**frame_data)
    db.add(frame)

# Commit changes
db.commit()
db.close()

print("✅ Dolan DF5 frames inserted successfully!")
