#!/usr/bin/env python3

import asyncio
import websockets


OK = "OK: "


def valid_reply(reply):
    if not reply.strip():
        raise ValueError("ERR:EMPTY")


async def handler(websocket):
    async for message in websocket:
        try:
            valid_reply(message)
        except ValueError as error:
            await websocket.send(str(error))
        else:
            await websocket.send(OK + message)


async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        print("Hello WebSocket")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
