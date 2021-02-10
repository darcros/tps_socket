import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 65432


def input_utente():
    while True:
        try:
            dati = input(
                'Inserisci i dati da inviare ("exit" per terminare la connessione): ')
        except EOFError:
            print("Okay. Exit")
            return "exit", None

        if not dati:
            print("Non puoi inviare una stringa vuota!")
            continue

        if dati == 'exit':
            print("Chiudo la connessione con il server!")
            return "exit", None

        return "command", dati


def invia_comando(sock, comando):
    dati = comando.encode()
    sock.send(dati)
    risposta = sock.recv(2048)
    return risposta.decode()


def connessione_server(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    return s


def main():
    sock = connessione_server(SERVER_ADDRESS, SERVER_PORT)
    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))

    while True:
        type, comando = input_utente()
        if type == "exit":
            break
        print(f'Invio comando "{comando}"')

        risposta = invia_comando(sock, comando)
        if not risposta:
            print("Server non risponde. Exit")
            break
        print(f'Ricevuta risposta: {risposta}')

    print("Programma terminato.")
    sock.close()


if __name__ == '__main__':
    main()
