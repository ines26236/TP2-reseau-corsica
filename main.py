from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
counter = 0


# Dossier static
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("static/index.html")

@app.get("/counter")
def get_counter():
    return {"counter": counter}

@app.post("/counter/{action}")
def update_counter(action: str):
    global counter
    if action == "inc":
        counter += 1
    elif action == "dec":
        counter -= 1
    return {"counter": counter}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
