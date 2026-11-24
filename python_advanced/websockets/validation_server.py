#!/usr/bin/env python3

import asyncio
import websockets


OK = "OK: "


def valid_reply(reply):
    if not reply.strip():
        raise ValueError("ERR:EMPTY")


async def connect_and_send(uri: str, text: str) -> str:
    async with websockets.connect(uri) as ws:
        await ws.send(text)
        reply = await ws.recv()
        return OK + reply


async def main():
    response = await connect_and_send("ws://127.0.0.1:8765", "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
