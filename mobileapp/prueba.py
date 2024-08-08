import serial

# Configura el puerto serial y la velocidad de baudios
port = "COM5"  # Cambia esto al puerto correcto en tu sistema
baudrate = 9600

ser = serial.Serial(port, baudrate)

try:
    while True:
        if ser.in_waiting > 0:
            # Leer la línea recibida
            line = ser.readline().decode('utf-8').rstrip()
            # Mostrar la información en tiempo real en la consola
            print(f"Received: {line}")
            # Guardar la línea en un archivo
            with open("received_data.txt", "a") as file:
                file.write(line + "\n")
except KeyboardInterrupt:
    print("Programa terminado")
finally:
    ser.close()
