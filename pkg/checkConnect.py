from asyncio.subprocess import DEVNULL
import socket
import subprocess
from sys import stdout
from pkg.sendMessage import sendMessage


def checkConnect(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = (ip, 80)
    result = s.connect_ex(location)

    if result == 0:
        print(f"{ip}...ok")
    else:
        print(f"{ip}...failed")
        sendMessage(ip, 80)
