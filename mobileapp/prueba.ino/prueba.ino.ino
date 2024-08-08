#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32_CAM", true);  // Configura el nombre del dispositivo y el canal RFCOMM por defecto
  randomSeed(analogRead(0));  // Inicializa el generador de números aleatorios
}

void loop() {
  // Generar números aleatorios
  int randomNumber1 = random(1, 20);
  int randomNumber2 = random(21, 30);
  int randomNumber3 = random(31, 40);
  int randomNumber4 = random(41, 50);

  // Crear una cadena JSON con los números aleatorios
  String jsonData = "{\"randomNumber1\":" + String(randomNumber1) + 
                    ", \"randomNumber2\":" + String(randomNumber2) + 
                    ", \"randomNumber3\":" + String(randomNumber3) + 
                    ", \"randomNumber4\":" + String(randomNumber4) + "}";

  // Imprimir la cadena JSON en el Monitor Serie y enviar por Bluetooth
  Serial.println(jsonData);
  SerialBT.println(jsonData);
  SerialBT.flush();  // Asegura que todos los datos se envíen

  delay(2000); 
}

