from fastapi import FastAPI
app=FastAPI(
    title="My memory os",
    version="1.0.0",
)
@app.get("/")
def home():
    return {"Server is running": "Welcome to My memory os!"}