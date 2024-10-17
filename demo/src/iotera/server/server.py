import asyncio
import websockets

from const import consts
import json

class IoteraResponse:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", -1)
        self.type = kwargs.get("type", "none")
        self.message = kwargs.get("message", "none")
        self.result = kwargs.get("result", [])
        self.success = kwargs.get("success", False)
        self.error = kwargs.get("error", False)

    def __str__(self):
        return json.dumps(self)

class IoteraRequest:
    def __init__(self, id, type, message):
        self.id = id
        self.type = type
        self.message = message

def as_iotera_request(json_obj: dict) -> IoteraRequest:
    return IoteraRequest(json_obj.get("id", None), json_obj.get("type", None), json_obj.get("message", None))

IOTERA_RESPONSE_TYPE_EVENT = "event"
IOTERA_RESPONSE_TYPE_RESULT = "result"

async def handle_connection(websocket, path):
    async for message in websocket:
        msg_object = as_iotera_request(json.loads(message))
        print(f"WebSocket Server Incoming Message: {message}, {path}")
        if msg_object.type == "ping":
            await websocket.send(IoteraResponse(
                id=msg_object.id,
                type=msg_object.type,
                message="pong",
                success=True
            ))
        else:
            levels = msg_object.type.split("/")
            level_count = len(levels)
            retval = None

            if levels[0] == "update":
                """
                TODO:
                e.g. update/sensor.lightroom_guest_room
                    levels[0] = update
                    levels[1] = sensor.lightroom_guest_room

                new value: parse from message, or something.
                """
                print(f"Websocket Server Update: {message}, {path}")
            else:
                if level_count == 2:
                    retval = IoteraResponse(
                        id      = msg_object.id,
                        type    = IOTERA_RESPONSE_TYPE_RESULT,
                        success = True,
                        result  = consts[levels[0]][levels[1]]
                    )
                elif level_count == 1:
                    retval = IoteraResponse(
                        id      = msg_object.id,
                        type    = IOTERA_RESPONSE_TYPE_RESULT,
                        success = True,
                        result  = consts[levels[0]]
                    )
                else:
                    retval = IoteraResponse(
                        id      = msg_object.id,
                        type    = IOTERA_RESPONSE_TYPE_RESULT,
                        error   = True,
                        message = f"Unknown message type `{msg_object.type}`"
                    )
            
            await websocket.send(json.dumps([retval.__dict__]))
        

host = "localhost"
port = 8321

async def main():
    async with websockets.serve(handle_connection, host, port):
        print(f"website server running at {host}:{port}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

