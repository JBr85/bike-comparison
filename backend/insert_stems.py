from database import SessionLocal, Stem

db = SessionLocal()

stems_data = [
    {"make": "Velobike Longboi", "length": 120, "angle": 6},
    {"make": "Velobike Longboi", "length": 120, "angle": 12},
    {"make": "Velobike Longboi", "length": 120, "angle": 16},
    {"make": "Velobike Longboi", "length": 130, "angle": 6},
    {"make": "Velobike Longboi", "length": 130, "angle": 12},
    {"make": "Velobike Longboi", "length": 130, "angle": 16},
    {"make": "Velobike Longboi", "length": 140, "angle": 6},
    {"make": "Velobike Longboi", "length": 140, "angle": 12},
    {"make": "Velobike Longboi", "length": 140, "angle": 16},
    {"make": "Velobike Longboi", "length": 150, "angle": 6},
    {"make": "Velobike Longboi", "length": 150, "angle": 12},
    {"make": "Velobike Longboi", "length": 150, "angle": 16},
    {"make": "Velobike Longboi", "length": 160, "angle": 6},
    {"make": "Velobike Longboi", "length": 160, "angle": 12},
    {"make": "Velobike Longboi", "length": 160, "angle": 16},
    {"make": "Velobike Longboi", "length": 170, "angle": 6},
    {"make": "Velobike Longboi", "length": 170, "angle": 12},
    {"make": "Velobike Longboi", "length": 170, "angle": 16},
    {"make": "Velobike Longboi", "length": 180, "angle": 6},
    {"make": "Velobike Longboi", "length": 180, "angle": 12},
    {"make": "Velobike Longboi", "length": 180, "angle": 16},
    {"make": "Velobike Longboi", "length": 190, "angle": 6},
    {"make": "Velobike Longboi", "length": 190, "angle": 12},
    {"make": "Velobike Longboi", "length": 190, "angle": 16},
    {"make": "Velobike Longboi", "length": 200, "angle": 6},
    {"make": "Velobike Longboi", "length": 200, "angle": 12},
    {"make": "Velobike Longboi", "length": 200, "angle": 16},
    {"make": "Koga Kinsei Integrated", "length": 160, "angle": 16},
]

for stem_data in stems_data:
    db.add(Stem(**stem_data))

db.commit()
db.close()

print("✅ Stems inserted successfully!")
