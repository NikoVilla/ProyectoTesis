#ifndef BLUETOOTHCOM_H
#define BLUETOOTHCOM_H

#include "BluetoothSerial.h"

class BluetoothCom {
public:
    BluetoothCom(BluetoothSerial* btSerial);
    virtual void begin() = 0;
    virtual void readAndSend() = 0;

protected:
    BluetoothSerial* SerialBT;
    void sendData(const String& data);
};

#endif
