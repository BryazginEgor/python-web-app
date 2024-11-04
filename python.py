from flask import Flask
import psutil
import socket

app = Flask(__name__)

@app.route('/')
def get_server_info():
  cpu_load = psutil.cpu_percent()
  ram_load = psutil.virtual_memory()
  hostname = socket.gethostname()
  ip_address = socket.gethostbyname(hostname)

  return (f"CPU load (%): {cpu_load} RAM load (%): {ram_load.percent}, Hostname: {hostname}, IP address: {ip_address}")

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)
