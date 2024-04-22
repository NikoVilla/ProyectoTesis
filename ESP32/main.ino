#include "PulsoSensor.h"
#include "OximetroSensor.h"
#include "TemperaturaSensor.h"
#include "GiroscopioSensor.h"
#include "BluetoothComms.h"

PulsoSensor pulso;
OximetroSensor oximetro;
TemperaturaSensor temperatura;
GiroscopioSensor giroscopio;
BluetoothComms bluetooth;

void setup() {
  pulso.begin();
  oximetro.begin();
  temperatura.begin();
  giroscopio.begin();
  bluetooth.begin();
}

void loop() {
  int pulsoData = pulso.read();
  int oximetroData = oximetro.read();
  int temperaturaData = temperatura.read();
  int giroscopioData = giroscopio.read();

  bluetooth.send(pulsoData, oximetroData, temperaturaData, giroscopioData);
}
