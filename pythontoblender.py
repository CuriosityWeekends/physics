import socket
import numpy as np
import time

msg = "5,0,0 " # Move to X=3, Y=2, Z=1

item0 = "Cube"

def MoveTo(item,x,y,z):
    msg = str(item) + "," + str(x) + "," + str(y) + "," + str(z)
    Send(msg)
    



def Send(msg):
    client = socket.socket()
    client.connect(('localhost', 5600))
    print("Socket connected")
    client.send(msg.encode())
    print("Sent msg: ", msg)
    client.close()



if __name__ == "__main__":
    x0 = 0
    y0 = 0
    z0 = 10

    v = -1 # m/s
    dt = 1 # s

    tStart = 0
    tStop = 10

    t = np.linspace(tStart, tStop, int(1 + ((tStop - tStart)/dt)))

    # t = range(0,10)
    

    z = []
    z.append(z0)

    for ti in t[1:]:
        dx = v * dt
        zi = z[-1] + dx
        MoveTo(item0,x0, y0, zi)
        z.append(zi)
        time.sleep(dt)
    
