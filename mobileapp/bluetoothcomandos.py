# Archivo: bluetooth_comms.py
import bluetooth

# Función para recibir datos
def receive_data():
    # Crea un nuevo socket Bluetooth
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # Asigna el socket al puerto 1
    port = 1
    server_sock.bind(("", port))
    # Escucha las conexiones entrantes
    server_sock.listen(1)

    # Acepta una conexión entrante
    client_sock, address = server_sock.accept()
    print(f"Accepted connection from {address}")

    # Recibe datos del cliente
    data = client_sock.recv(1024)
    print(f"Received: {data}")

    # Cierra los sockets del cliente y del servidor
    client_sock.close()
    server_sock.close()

    # Devuelve los datos recibidos
    return data


# Archivo: main.py
# import bluetooth_comms

# Recibe datos a través de Bluetooth
# data = bluetooth_comms.receive_data()

# Procesa los datos recibidos...
