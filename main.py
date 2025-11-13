from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json

app = FastAPI()
counter = 0
connections = []


# Dossier static
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("static/index.html")


async def broadcast():
    global counter
    for connection in connections:
        try:
            await connection.send_text(json.dumps({"counter": counter}))
        except:
            connections.remove(connection)

@app.websocket("/ws")
async def ws(websocket: WebSocket):
    global counter
    await websocket.accept()
    connections.append(websocket)
    await websocket.send_text(json.dumps({"counter": counter}))
    try:
        while True:
            data = json.loads(await websocket.receive_text())
            if "counter" in data: counter = data["counter"] ; await broadcast()
    except WebSocketDisconnect: connections.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
