import bpy
import socket
import threading

def start_server():
    server = socket.socket()
    server.bind(('localhost', 9999))
    server.listen(1)
    print("🔌 Waiting for connection...")

    while True:
        try:
            conn, addr = server.accept()
            print(f"✅ Connection from {addr}")
            data = conn.recv(1024).decode()
            if data:
                print(f"📦 Received: {data}")
                x, y, z = map(float, data.split(","))
                bpy.data.objects["Cube"].location = (x, y, z)
            conn.close()
        except:
            print("Exception")
# Run in background thread to avoid blocking Blender
thread = threading.Thread(target=start_server)
thread.daemon = True
thread.start()
print("✅ Server is running in background...")