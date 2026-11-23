#!/usr/bin/env python3

import asyncio
import websockets


async def handler(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
