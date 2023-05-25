import time
import network
import socket
import json
from machine import Pin

# ssid = ''
# password = ''

# Load Wi-Fi credentials from .secret.env
with open('.secret.env') as f:
    for line in f:
        key, value = line.strip().split('=')
        if key == 'SSID':
            ssid = value
        elif key == 'PASSWORD':
            password = value

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Status</title>
    <style>
        head {
            display: none;
        }
        body {
            font-family: sans-serif;
            margin: 0 auto;
            padding: 1em;
            background-color: #282828;
            color: #ebdbb2;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        h1 {
            margin-bottom: 1em;
        }

        form {
            margin-bottom: 1em;
        }
        
        label {
            display: block;
            margin-bottom: 0.5em;
            color: #ebdbb2;
        }
        
        input[type="number"] {
            padding: 0.5em;
            border-radius: 4px;
            border: 1px solid #ebdbb2;
            background-color: #282828;
            color: #ebdbb2;
        }
        
        input[type="submit"] {
            padding: 0.5em 1em;
            border-radius: 4px;
            border: none;
            background-color: #ebdbb2;
            color: #282828;
            cursor: pointer;
        }
        button {
            padding: 0.5em 1em;
            border-radius: 4px;
            border: none;
            background-color: #ebdbb2;
            color: #282828;
            cursor: pointer;
        }
        
        h2 {
            margin-bottom: 0.5em;
        }
        
        table {
            width: 95vw;
            border-collapse: collapse;
        }
        
        th, td {
            padding: 0.5em;
            border: 1px solid #ebdbb2;
        }

        #inputCntr {
            display: flex;
            flex-direction: row;
            justify-content: space-evenly;
            align-items: last baseline;
            width: 100%;
        }
    </style>
</head>
<body>
    <h1>Wi-Fi Status Detector and Logger</h1>
    <div id="inputCntr">
        <div>
            <form method="POST">
                <label for="refresh_rate">Refresh Rate (seconds):</label>
                <input type="number" id="refresh_rate" name="refresh_rate" min="1" max="60" value="%s">
                <input type="submit" value="Set">
            </form>
        </div>
        <div>
            <form action="POST">

            </form>
        </div>
        <div>
            <form action="POST">
                <button type="submit">
                    Download Log
                </button>
                <button type="submit">
                    Clear Log
                </button>
            </form>
        </div>
    </div>
    <h2>Status Log</h2>
    <table>
        <tr>
            <th>Date/Time</th>
            <th>Status</th>
        </tr>
        %s
    </table>
</body>
</html>
"""

# Load Wi-Fi credentials from .secret.env
with open('.secret.env') as f:
    for line in f:
        key, value = line.strip().split('=')
        if key == 'SSID':
            ssid = value
        elif key == 'PASSWORD':
            password = value

log_row = "<tr><td>%s</td><td>%s</td></tr>"
status_log = []

def log_status(dtg, status):
    status_log.append(log_row % (dtg, status))

def get_status():
    return "Up" if wlan.isconnected() else "Down"

def save_log():
    with open('log.json', 'w') as f:
        json.dump(status_log, f)

def load_log():
    try:
        with open('log.json', 'r') as f:
            return json.load(f)
    except:
        return []

status_log = load_log()

def serve_client(cl):
    request = cl.recv(1024)
    print("request:")
    print(request)

    refresh_rate = 5  # Default refresh rate
    if "refresh_rate" in request:
        try:
            refresh_rate = int(request.split(b'refresh_rate=')[1].split(b' ')[0])
        except:
            pass

    dtg = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    status = get_status()
    log_status(dtg, status)
    save_log()

    log_rows = "\n".join(status_log[-10:])  # Show the last 10 status logs

    # Create and send response
    response = html % (refresh_rate, log_rows)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

# Listen for connections, serve client
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        serve_client(cl)
    except OSError as e:
        cl.close()
        print('connection closed')
