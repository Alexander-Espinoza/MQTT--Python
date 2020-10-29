import threading
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print()
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='MENSAJES', qos=2)

def on_message(client, userdata, msg):
    print()
    print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())+" "+msg.topic+" "+str(msg.payload))

def ingresa_datos():
    continuar=True
    while continuar:   
        datos = input("Ingresa 1 para encender/ 2 para apagar: ")
        client.publish("LED", datos)
        salir=input("Salir y/n: ")
        salir=salir.upper()
        if salir=='Y':
            continuar=False
        elif salir=='n':
            continuar=True
            print(continuar)
        else:
            pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

threading.Thread(target=ingresa_datos).start()

client.loop_forever()




