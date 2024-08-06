#include "PulsoSensor.h"
#include "OximetroSensor.h"
#include "TemperaturaSensor.h"
#include "GiroscopioSensor.h"
#include "PruebaST.h"
#include "BluetoothCom.h"

BluetoothSerial SerialBT;
PruebaST tempSensor(4, DHT11, &SerialBT, "Temperatua");

// PulsoSensor pulso (5, AD..., &SerialBT, "Pulso");
// OximetroSensor oximetro;
// TemperaturaSensor temperatura;
// GiroscopioSensor giroscopio;
// BluetoothCom bluetooth;

void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32_CAM");
  tempSensor.begin();
  // pulso.begin();
  // oximetro.begin();
  // temperatura.begin();
  // giroscopio.begin();
  // bluetooth.begin();
}

void loop() {
    tempSensor.readAndSend();
    // pulso.readAndSend();
    delay(2000);
}

// #include "BluetoothSerial.h"
// #include "esp_adc_cal.h"
// #include "Wire.h" // Para la comunicación I2C
// #include "MAX30102.h" // Para el sensor de oxímetro de sangre
// #include "MPU6050.h" // Para el acelerómetro/ giroscopio
// #include "AD8232.h" // Para el módulo de medición ECG
// #define ADC_VREF_mV    5000.0 // en milivoltios
// #define ADC_RESOLUTION 4096.0
// #define PIN_LM35       35
// #define PIN_BATTERY    34 // Pin para la lectura del nivel de batería

// #if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
// #error Bluetooth no está habilitado! Por favor, ejecuta `make menuconfig` para habilitarlo
// #endif
 
 
// BluetoothSerial SerialBT;

// int Led = 33; // El pin del LED en el ESP32-CAM es generalmente el 33

// // Inicializa los sensores aquí
// MAX30102 oximetro;
// MPU6050 mpu6050(Wire);
// AD8232 ecg;
// LM35 lm35(PIN_LM35);

// void setup() {
//   Serial.begin(9600);
//   SerialBT.begin("ESP32CAM_LABVIEW");
//   pinMode(Led, OUTPUT);

//   // Configura los sensores aquí
//   oximetro.begin();
//   mpu6050.begin();
//   ecg.begin();
//   lm35.begin();
// }

// void loop() {
//   // Lee los valores de los sensores aquí
//   int adcVal = analogRead(PIN_LM35);
//   float milliVolt = adcVal * (ADC_VREF_mV / ADC_RESOLUTION);
//   float tempC = milliVolt / 10;
 
//   // Imprime los valores de los sensores aquí
//   Serial.println(tempC);   
//   SerialBT.println (tempC);

//   // Lee el nivel de la batería
//   int batteryLevel = analogRead(PIN_BATTERY);
//   // Convierte el nivel de batería a porcentaje aquí
//   // ...
//   Serial.println(batteryLevel);
//   SerialBT.println(batteryLevel);

//   delay(1000);
//   if (SerialBT.available()) {
//     char Mensaje = SerialBT.read();
//     if (Mensaje == 'A') {
//       digitalWrite(Led, HIGH);
//     }
//     else if (Mensaje == 'B') {
//       digitalWrite(Led, LOW);
//     }
//   }
// }