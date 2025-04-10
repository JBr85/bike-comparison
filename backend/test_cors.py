from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

print("DEBUG: We are in test_cors.py")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
def read_test():
    return {"message": "CORS test successful!"}

if __name__ == "__main__":
    print("DEBUG: Starting uvicorn directly from test_cors.py")
    uvicorn.run(app, host="127.0.0.1", port=8000)
