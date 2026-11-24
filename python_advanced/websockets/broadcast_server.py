#!/usr/bin/env python3

import asyncio
import websockets
import itertools


OK = "B:"
connected_clients = {}
next_id = itertools.count(1)


def valid_reply(reply):
    if not reply.strip():
        raise ValueError("ERR:EMPTY")


async def send_to(client_id, m):
    ws = connected_clients.get(client_id)
    if ws is None:
        return False
    try:
        await ws.send(m)
    except websockets.ConnectionClosed:
        return False
    return True


async def broadcast(m):
    for client_id in list(connected_clients):
        await send_to(client_id, m)


async def handler(websocket):
    client_id = next(next_id)
    connected_clients[client_id] = websocket
    try:
        async for message in websocket:
            try:
                valid_reply(message)
            except ValueError as error:
                await websocket.send(str(error))
            else:
                await broadcast(OK + message)
    finally:
        del connected_clients[client_id]


async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        print("Hello WebSocket")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
