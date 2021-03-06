#!/usr/bin/env python
#https://bbs.archlinux.org/viewtopic.php?id=174773
import asyncio
import websockets
import datetime
import temp
import leds

tempSensorLeft = 15
tempSensorRight = 45
pumpBool = False

async def hello(websocket, path):
    command = await websocket.recv()
    print("< {}".format(command))
    sendData = "NaN"
    if(command == "tempLeft"):
        sendData = (str(tempSensorLeft))
    elif(command == "tempRight"):
        sendData = (str(tempSensorRight))
    elif(command == "date"):
        sendData = (str(datetime.datetime.now()))
    elif(command == "pump"):
        sendData = (str(pumpBool))
    await websocket.send(sendData)
    print("> {}".format(sendData))

@asyncio.coroutine
def periodic():
    while True:
        print('periodic')
        measureTemp()
        yield from asyncio.sleep(1)

def measureTemp():
    global tempSensorLeft
    global tempSensorRight
    global pumpBool
    #if (tempSensorLeft < 45): tempSensorLeft += 1
    #else: tempSensorLeft = 15
    #if (tempSensorRight > 15): tempSensorRight -= 1
    #else: tempSensorRight = 45
    tempSensorLeft = temp.read_temp_left()
    tempSensorRight = temp.read_temp_right()
    pumpBool = (tempSensorLeft > tempSensorRight) && (tempSensorLeft < 35)
    leds.setLed(pumpBool)
    leds.setRelay(pumpBool)


def stop():
    task.cancel()

start_server = websockets.serve(hello, '0.0.0.0', 8765)

task = asyncio.Task(periodic())
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(start_server)
    loop.run_until_complete(task)
    loop.run_forever()
except websockets.exceptions.ConnectionClosed:
    print("koji fail")
