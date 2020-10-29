WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(pinLed, HIGH);   
    client.publish("MENSAJES","LED ENCENDIDO");  
    Serial.println("LED ENCENDIDO");
  } else if (((char)payload[0] == '2')){
    digitalWrite(pinLed, LOW);
    client.publish("MENSAJES","LED APAGADO");
    Serial.println("LED APAGADO");
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += "1";
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("Connected");
      // Once connected, publish an announcement...
      clientId+=" Conectado";
      client.publish("MENSAJES",clientId.c_str());
      // ... and resubscribe
      client.subscribe("LED");
    } else {
      
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
