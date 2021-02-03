import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 65432

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((SERVER_ADDRESS, SERVER_PORT))
print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    try:
        dati = input(
            'Inserisci i dati da inviare ("exit" per terminare la connessione): ')
    except EOFError:
        print("Okay. Exit")
        break
    if not dati:
        print("Non puoi inviare una stringa vuota!")
        continue
    if dati == 'exit':
        print("Chiudo la connessione con il server!")
        break

    dati = dati.encode()

    socket.send(dati)

    risposta = socket.recv(2048)

    if not risposta:
        print("Server non risponde. Exit")
        break

    risposta = risposta.decode()

    print("Ricevuto dal server:")
    print(risposta)

socket.close()
