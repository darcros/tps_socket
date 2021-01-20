import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Optionale: permette di riavviare subito il codice,
# altrimenti bisognerebbe aspettare 2-4 minuti prima di poter riutilizzare(bindare) la stessa porta
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen()
print(f"[{HOST}] In ascolto su {PORT}")

clientsocket, address = s.accept()
with clientsocket as cs:
    print(f"Connessione da {address}")
    while True:
        dati = cs.recv(1024)
        dati.decode()
        if not dati:
            break
        dati = dati.decode()
        print(f"Ricevuto '{dati}' dal client")
        dati = "Ciao, " + str(address) + ". Ho ricevuto questo: '" + dati + "'"
        dati = dati.encode()
        cs.send(dati)
        print(f"Inviato al client: {dati}")
