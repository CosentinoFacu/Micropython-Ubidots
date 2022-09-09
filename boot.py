import time
import network
import machine as m
from umqtt.robust import MQTTClient
import random


SSID = "WIFI Ledesma"
PASSWORD = "Faivjuge06101427"
flag=0

ubidotsToken = "BBFF-RnRewipPAzfA2WOHCflY59hcVdwLSh"
clientID = "FACU-PC" 
client = MQTTClient("clientID", "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken)

def conectar():
  
    print('Buscando red..')
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    lista=sta_if.scan()
    time.sleep(2)
    for i in range(len(lista)):
        reg=lista[i]
        red=str(reg[0])
        red=red.replace("'", '')
        red=red.replace("b", '')
        if red == SSID:
            print('Red encontrada')
            sta_if.connect(SSID, PASSWORD)
            while not sta_if.isconnected():
                print('Conectando..')
                time.sleep(1)
                pass
            print("Conectado a red:", SSID)
            flag=1
            time.sleep(3)
            break
        if i == (len(lista)-1):
            print('Red no encontrada')

conectar()

def publish(dato):
    client.connect()
    msg = b'{"valor": {"value":%s}}'%dato
    #print(msg)
    client.publish(b"/v1.6/devices/prueba_micropython", msg)
    print("Se publico valor = ", dato)
    time.sleep(20)
    client.disconnect()
    time.sleep(5)

while True:
    a=random.randrange(5, 27, 4)
    publish(a)
