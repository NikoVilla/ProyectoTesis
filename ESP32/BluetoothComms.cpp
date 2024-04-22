// Archivo: BluetoothComms.cpp
#include "BluetoothComms.h"
#include "BluetoothSerial.h" // Esta es una biblioteca común para ESP32

BluetoothSerial SerialBT;

void BluetoothComms::begin() {
  // Inicializa la comunicación Bluetooth
  SerialBT.begin("ESP32test"); // Nombre del dispositivo Bluetooth
}

void BluetoothComms::send(int pulsoData, int oximetroData, int temperaturaData, int giroscopioData) {
  // Envia los datos a través de Bluetooth
  String dataToSend = String(pulsoData) + "," + String(oximetroData) + "," + String(temperaturaData) + "," + String(giroscopioData);
  SerialBT.println(dataToSend);
}
