#ifndef DHTSENSOR_H
#define DHTSENSOR_H

#include "BluetoothCom.h"
#include "DHT.h"

class DHTSensor : public BluetoothCom {
public:
    DHTSensor(int pin, int type, BluetoothSerial* btSerial, const String& name);
    void begin() override;
    void readAndSend() override;

private:
    DHT dht;
    String sensorName;
    void handleError();
};

#endif
