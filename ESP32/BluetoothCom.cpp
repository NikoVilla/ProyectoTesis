#include "BluetoothCom.h"

BluetoothCom::BluetoothCom(BluetoothSerial* btSerial) : SerialBT(btSerial) {}

void BluetoothCom::sendData(const String& data) {
    Serial.println(data);
    SerialBT->println(data);
}
