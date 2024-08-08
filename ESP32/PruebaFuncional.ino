// Preferencias -> link
// Gestor de placas -> esp32 ul. -v


#include "BluetoothSerial.h"
#include "DHT.h"

#define DHTPIN 4        // Pin IO4 en ESP32-CAM
#define DHTTYPE DHT11   // Definimos el tipo de sensor DHT

BluetoothSerial SerialBT;
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32_CAM");
  dht.begin();
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
    Serial.println(tempC);
    SerialBT.println(tempC);
  }
  
  delay(2000); // Esperar 2 segundos entre lecturas
}
