import socket

HOST = '127.0.0.1'
PORT = 65432

# server echo.
# - ascolta
# - accetta una connessione
# - legge tutti i dati
# - fa echo dei dati
# - termina.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()
    print(f"[{HOST}] In ascolto su {PORT}")
    clientsocket, address = socket.accept()
    with clientsocket as cs:
        print('Connessione da', address)
        while True:
            data = cs.recv(1024)
            if not data:
                break
            cs.sendall(data)
