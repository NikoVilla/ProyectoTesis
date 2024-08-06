#include "BluetoothSerial.h"
#include "DHT.h"

#define DHTPIN 4        // Pin IO4 en ESP32-CAM
#define DHTTYPE DHT11   // Definimos el tipo de sensor DHT
// #define ECGPIN 34       // Pin de entrada analógica para el AD8232

BluetoothSerial SerialBT;
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32_SENSORS");
  dht.begin();
//   pinMode(ECGPIN, INPUT); --
}

void loop() {
  // Leer la temperatura en Celsius
  float tempC = dht.readTemperature();
  
  // Verificar si la lectura es válida
  if (isnan(tempC)) {
    Serial.println("¡Error al leer del sensor DHT11!");
    SerialBT.println("¡Error al leer del sensor DHT11!");
  } else {
    // Imprimir la temperatura en el Monitor Serie y enviar por Bluetooth
    Serial.print("Temp: ");
    Serial.println(tempC);
    SerialBT.print("Temp: ");
    SerialBT.println(tempC);
  }
  
  // Leer el valor analógico del sensor AD8232
//   int ecgValue = analogRead(ECGPIN);
  // float --
  
  // Imprimir el valor en el Monitor Serie y enviar por Bluetooth --
//   Serial.print("ECG: ");
//   Serial.println(ecgValue);
//   SerialBT.print("ECG: ");
//   SerialBT.println(ecgValue);
  
  delay(2000); // Esperar 2 segundos entre lecturas
}