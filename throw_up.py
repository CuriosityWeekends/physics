import socket
import numpy as np
import matplotlib.pyplot as plt
import time
plt.grid()
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
    z0 = 0

    v = 10
    dt = 0.1 # s        when the value increases the smoothness increase
    a = -1 # constant
    
    tStart = 0
    tStop = 30

    xaxis = []
    yaxis = []
    print(int(1 + ((tStop - tStart)/dt)))
    t = np.linspace(tStart, tStop, int(1 + ((tStop - tStart)/dt)))

    # t = range(0,10)
    

    z = []
    z.append(z0)

    for ti in t[1:]:
        v += a*dt
        dx = v * dt
        zi = z[-1] + dx
        MoveTo(item0,x0, y0, zi)
        xaxis.append(ti)
        yaxis.append(zi)
        plt.plot(xaxis, yaxis)
        
        plt.pause(dt)
        z.append(zi)
        #time.sleep(dt)
    
