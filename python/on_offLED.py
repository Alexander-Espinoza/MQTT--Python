#Programa que nos permite publicar en el tópico LED para prender (1) o apagar (2) un led

import paho.mqtt.client as mqtt
import time

#Conexión y suscripción al tópico MENSAJES
def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe('MENSAJES')

#Mostrar mensajes que lleguen al tópico MENSAJES
def on_message(client, userdata, msg):
    print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())+" "+msg.topic+" "+str(msg.payload))

#Función que nos preguntará si continuar o salir del menú
def yes_or_no(question):
    reply = str(input(question)).lower().strip()
    if reply[0] == 'y':
        return 0
    elif reply[0] == 'n':
        return 1
    else:
        return yes_or_no("Por favor ingresa (y/n) ")

#En el menú nos permitirá ingresar 1 o 2 para poder prender o apagar el LED respectivamente
def ingresa_payload(question):
	reply = str(input(question)).upper().strip()
	if reply == '1':
		return reply
	elif reply == '2':
		return reply
	else:
		return ingresa_payload("Por favor ingresa (1 o 2): ")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#Nos conectamos al broker 
client.connect("mqtt.eclipse.org", 1883, 60)

#Menú
while True:
	try:
		datos = ingresa_payload("Ingresa 1 para encender/ 2 para apagar: ")
		#PUblicamos en el tópico LED
		client.publish("LED", datos)
		if(yes_or_no('Enviar de nuevo? (y/n): ')):
			break
		
	except:
		pass



