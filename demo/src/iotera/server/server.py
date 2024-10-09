import asyncio
import websockets

from const import consts
import json



async def handle_connection(websocket, path):
    async for message in websocket:
        print(f"WebSocket Server Incoming Message: {message}, {path}")
        if message == "ping":
            await websocket.send("Hello World")
        # if the need be for conditional message processing.
        # elif message == "map":
        #     await websocket.send(json.dumps({
        #         "head": "map",
        #         "body": map_entities,
        #     }))
        # elif message == "energy_prefs":
        #     await websocket.send(json.dumps({
        #         "head": "energy_prefs",
        #         "body": energy_prefs,
        #     }))
        else:
            # assume two level object.

            levels = message.split("/")
            level_count = len(levels)
            retval = None
            if level_count == 2:
                retval = {
                    "code": "success",
                    "level_count": level_count,
                    "data": consts[levels[0]][levels[1]],
                }
            elif level_count == 1:
                retval = {
                    "code": "success",
                    "level_count": level_count,
                    "data": consts[levels[0]],
                }
            else:
                retval = {"code": "error", "data": f"message `{message}` not recognized."}
            await websocket.send(json.dumps(retval))
        

host = "localhost"
port = 8321

async def main():
    async with websockets.serve(handle_connection, host, port):
        print(f"website server running at {host}:{port}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

