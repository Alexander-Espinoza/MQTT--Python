const char* ssid     = "papa";
const char* password = "alexander23";
const char* mqtt_server = "mqtt.eclipse.org";

IPAddress ip(192, 168, 1, 200);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;
int pinLed = 5;//D1
