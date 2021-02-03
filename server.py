import socket

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Optionale: permette di riavviare subito il codice,
# altrimenti bisognerebbe aspettare 2-4 minuti prima di poter riutilizzare(bindare) la stessa porta
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind del socket alla porta
server_socket.bind((HOST, PORT))

# mette il socket in ascolto, con un backlog di 5 connessioni
server_socket.listen(5)
print(f"[{HOST}] In ascolto su {PORT}")

while True:
    socket, address = server_socket.accept()
    print("Connessione ricevuta da " + str(address))
    print("Aspetto di ricevere i dati ")

    counter = 0

    while True:
        dati = socket.recv(2048)
        if not dati:
            print("Fine dati dal client. Reset")
            break
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)

        if dati == '0':
            print("Chiudo la connessione con " + str(address))
            break

        counter += 1

        risposta = "Risposta a : " + \
            str(address) + ". Il valore del contatore è : " + str(counter)
        risposta = risposta.encode()

        socket.send(risposta)
