import socket
import numpy as np
import time

msg = "5,0,0 " # Move to X=3, Y=2, Z=1


def MoveTo(x,y,z):
    msg = str(x) + "," + str(y) + "," + str(z)
    Send(msg)
    


def Send(msg):
    client = socket.socket()
    client.connect(('localhost', 9999))
    client.send(msg.encode())
    client.close()


if __name__ == "__main__":
    x0 = 0
    y0 = 0
    z0 = 0

    v = 1 # m/s
    dt = 1 # s

    tStart = 0
    tStop = 10

    t = np.linspace(tStart, tStop, int(1 + ((tStop - tStart)/dt)))

    # t = range(0,10)
    

    x = []
    x.append(x0)

    for ti in t[1:]:
        dx = v * dt
        zi = x[-1] + dx
        MoveTo(x0, y0, zi)
        x.append(zi)
        time.sleep(dt)