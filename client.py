import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 65432

# - si collega
# - invia un messaggio chiesto all'utente
# - legge 2048 byte e li stampa

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_ADDRESS, SERVER_PORT))
dati = input("Inserisci messaggio per il server: ")
dati = dati.encode()
s.send(dati)
dati = s.recv(2048)
if dati:
    dati = dati.decode()
    print("Ho ricevuto dal server: ")
    print(dati + '\n')
