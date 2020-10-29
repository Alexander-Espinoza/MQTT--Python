#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#include "config.h"  // Sustituir con datos de su red
#include "ESP8266_Utils.hpp"
#include "MQTT.hpp"

void setup()
{
  Serial.begin(115200);
  ConnectWiFi_STA();
  pinMode(pinLed, OUTPUT);     
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop()
{
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
