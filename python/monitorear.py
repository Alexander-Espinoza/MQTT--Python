#Monitoreo del tópico MENSAJES
import paho.mqtt.client as mqtt

#Conexión y suscripción al tópico MENSAJES
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("MENSAJES")
    
#Recepción del mensaje del tópico al cual estamos suscritos
def on_message(client, userdata, msg):
    pay=msg.payload.decode('utf-8')
    print(msg.topic+": "+pay)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#Nos conectamos al broker
client.connect("mqtt.eclipse.org", 1883, 60)
#Nos permite recibir los mensajes de los tópicos suscritos
client.loop_forever()

