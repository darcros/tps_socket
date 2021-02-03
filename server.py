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

operazioni = {
    "somma": lambda a, b: a + b,
    "sottrazione": lambda a, b: a - b,
    "moltiplicazione": lambda a, b: a * b,
    "divisione": lambda a, b: a / b,
}


def try_float(n):
    try:
        return float(n)
    except ValueError:
        return None


while True:
    socket, address = server_socket.accept()
    print("Connessione ricevuta da " + str(address))
    print("Aspetto di ricevere i dati ")

    while True:
        dati = socket.recv(2048)
        if not dati:
            print("Fine dati dal client. Reset")
            break
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)

        if dati == 'exit':
            print("Chiudo la connessione con " + str(address))
            break

        op_code, a, b = dati.split(";")
        op = operazioni.get(op_code)
        a = try_float(a)
        b = try_float(b)

        ris = ""
        if not op:
            ris = f'"{op_code}" operazione non riconosciuta'
        elif not a:
            ris = f'"{a}" non è un numero valido'
        elif not b:
            ris = f'"{b}" non è un numero valido'
        else:
            ris = f'Risposta a : {str(address)} il risultato dell\'opereazione "{op_code} tra {a} e {b} è {op(a, b)}'

        ris = ris.encode()
        socket.send(ris)
