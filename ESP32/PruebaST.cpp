#include "PruebaST.h"

DHTSensor::DHTSensor(int pin, int type, BluetoothSerial* btSerial, const String& name) 
    : BluetoothCom(btSerial), dht(pin, type), sensorName(name) {}

void DHTSensor::begin() {
    dht.begin();
}

void DHTSensor::readAndSend() {
    float tempC = dht.readTemperature();
    float humidity = dht.readHumidity();
    if (isnan(tempC) || isnan(humidity)) {
        handleError();
    } else {
        sendData(sensorName + " - Temp: " + String(tempC) + "°C, Hum: " + String(humidity) + "%");
    }
}

void DHTSensor::handleError() {
    sendData(sensorName + " - ¡Error al leer del sensor DHT11!");
}
