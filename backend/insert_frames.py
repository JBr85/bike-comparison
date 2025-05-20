from database import SessionLocal, Frame

# Create a session
db = SessionLocal()

# List of Hope HBT Paris frames to insert
frames = [
    {"make": "Hope HBT Paris", "size": "XS1", "reach": 416.5, "stack": 462, "top_tube": 532, "head_angle": 74, "seat_angle": 76, "head_tube": 72, "chainstay": None, "wheelbase": None, "front_centre": 551.5, "bb_drop": None, "fork_rake": None},
    {"make": "Hope HBT Paris", "size": "S1", "reach": 436.5, "stack": 468, "top_tube": 553.5, "head_angle": 74, "seat_angle": 76, "head_tube": 78, "chainstay": None, "wheelbase": None, "front_centre": 473, "bb_drop": None, "fork_rake": None},
    {"make": "Hope HBT Paris", "size": "L1", "reach": 467, "stack": 478, "top_tube": 586, "head_angle": 75, "seat_angle": 76, "head_tube": 86, "chainstay": None, "wheelbase": None, "front_centre": 602.5, "bb_drop": None, "fork_rake": None},
    {"make": "Hope HBT Paris", "size": "L2", "reach": 467, "stack": 478, "top_tube": 586, "head_angle": 75, "seat_angle": 76, "head_tube": 86, "chainstay": None, "wheelbase": None, "front_centre": 602.5, "bb_drop": None, "fork_rake": None},
    {"make": "Hope HBT Paris", "size": "XL1", "reach": 487, "stack": 486.5, "top_tube": 608, "head_angle": 75, "seat_angle": 76, "head_tube": 95, "chainstay": None, "wheelbase": None, "front_centre": 620, "bb_drop": None, "fork_rake": None},
    {"make": "Hope HBT Paris", "size": "XXL1", "reach": 516, "stack": 486, "top_tube": 637, "head_angle": 75, "seat_angle": 76, "head_tube": 95, "chainstay": None, "wheelbase": None, "front_centre": 649, "bb_drop": None, "fork_rake": None},
    {"make": "Hope HBT Paris", "size": "XXL2", "reach": 516, "stack": 486, "top_tube": 637, "head_angle": 75, "seat_angle": 76, "head_tube": 95, "chainstay": None, "wheelbase": None, "front_centre": 649, "bb_drop": None, "fork_rake": None},
]

# Insert frames into the database
for frame_data in frames:
    frame = Frame(**frame_data)
    db.add(frame)

# Commit changes
db.commit()
db.close()

print("✅ Hope HBT Paris frames inserted successfully!")
