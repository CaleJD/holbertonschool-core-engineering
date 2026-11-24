#!/usr/bin/env python3

from starlette.websockets import WebSocketDisconnect
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


HTML = """
<!DOCTYPE html>
<html>
<body>
  <h1>WebSocket Echo</h1>
  <input id="msg" placeholder="Type a message">
  <button onclick="send()">Send</button>
  <p id="log"></p>
  <script>
    const ws = new WebSocket(`ws://${location.host}/ws`);
    ws.onmessage = (event) => {
      document.getElementById("log").textContent += event.data + "\\n";
    };
    function send() {
      const input = document.getElementById("msg");
      ws.send(input.value);
      input.value = "";
    }
  </script>
</body>
</html>
"""

async def homepage(request):
    return HTMLResponse(HTML)


async def websocket_endpoint(websocket):
    await websocket.accept()
    try:
        while True:
            m = await websocket.receive_text()
            await websocket.send_text(m)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
