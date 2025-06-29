import bpy
import socket
import threading

def start_server():
    server = socket.socket()
    server.bind(('localhost', 5600))
    server.listen(1)
    print("🔌 Waiting for connection...")

    while True:
        try:
            conn, addr = server.accept()
            print(f"✅ Connection from {addr}")
            data = conn.recv(1024).decode()
            if data:
                print(f"📦 Received: {data}")
                item, (x, y, z)  = str(data.split(",")[0]), map(float, data.split(",")[1:])
                bpy.data.objects[item].location = (x, y, z)
            conn.close()
        except Exception as e:
            print("Exception: ", e)
# Run in background thread to avoid blocking Blender
thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()
print("✅ Server is running in background...")