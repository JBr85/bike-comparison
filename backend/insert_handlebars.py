from database import SessionLocal, Handlebar

db = SessionLocal()

handlebars_data = [
    {"make": "Koga Kinsei Sprint", "width": 350, "reach": 90, "drop": 115},
]

for bar in handlebars_data:
    db.add(Handlebar(**bar))

db.commit()
db.close()

print("✅ Handlebars inserted successfully!")
