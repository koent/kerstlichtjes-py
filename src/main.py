import machine
import socket
import network


with open('frontend.html', 'r') as f:
    frontend = f.read()

pin = machine.Pin(5, machine.Pin.OUT)

s = socket.socket()
s.bind(socket.getaddrinfo('0.0.0.0', 80)[0][-1])
s.listen(1)

wlan = network.WLAN(network.WLAN.IF_STA)
ip_address = wlan.ipconfig('addr4')[0]

print(f"Now listening for requests on http://{ip_address}:80/")

while True:
    cl, addr = s.accept()
    response_body = frontend
    print(addr[0], end=' ')
    cl_file = cl.makefile('rwb', 0)
    start_line = cl_file.readline().decode('utf-8')
    if start_line.startswith("GET ") or start_line.startswith("POST "):
        method, path, *_ = start_line.split()
        print(method, path, end=' ')
        if method == "POST" and path == "/on":
            pin.on()
            response_body = "on"
        elif method == "POST" and path == "/off":
            pin.off()
            response_body = "off"
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    
    print()
    _ = cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    _ = cl.send(response_body)
    cl.close()
