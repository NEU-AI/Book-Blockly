from umqtt.simple import MQTTClient
from machine import Pin
import network
import time
import machine
# import dht
from machine import Timer
 
# SSID="setting..."
# PASSWORD="loading...@"

SSID="NEUI111"
PASSWORD="83766158"
 
#SERVER ='a1h68Ao3GZ7.iot-as-mqtt.cn-shanghai.aliyuncs.com'  #MQTT Server: LGSODS81VJ.iotcloud.tencentdevices.com
SERVER='106.15.83.29'
CLIENT_ID = "123456|securemode=3,signmethod=hmacsha1|"   #设备ID
PORT=1883
username='test1&a1h68Ao3GZ7'
password='C037F3C23C0F580FE7C5D8E415E00A7783F9C48E'
 
publish_TOPIC = '/sys/a1h68Ao3GZ7/test1/thing/event/property/post'
subscribe_TOPIC ='/sys/a1h68Ao3GZ7/test1/thing/service/property/set'
 
client=None
mydht=None
 
def sub_cb(topic, msg):
    print("rx topic:\n",(topic, msg))
 
def connectWifi(ssid,passwd):
    global wlan
    wlan=network.WLAN(network.STA_IF)         #create a wlan object
    wlan.active(True)                         #Activate the network interface
    wlan.disconnect()                         #Disconnect the last connected WiFi
    wlan.connect(ssid,passwd)                 #connect wifi
    while wlan.isconnected() == False:
        time.sleep(1)
    print(wlan.ifconfig())

if __name__=='__main__':
    try:
        # mydht=dht.DHT11(machine.Pin(4))
        connectWifi(SSID,PASSWORD)
        client = MQTTClient(CLIENT_ID,SERVER,PORT,username,password,60)     #create a mqtt client
        print(client)
        client.set_callback(sub_cb)                         #set callback
        print("try connect to mqtt")
        client.connect()                                    #connect mqtt
        print("connect to mqtt done")                               #connect mqtt
        client.subscribe(subscribe_TOPIC)                   #client subscribes to a topic
        #mytimer=Timer(0)
        #mytimer.init(mode=Timer.PERIODIC, period=5000,callback=apptimerevent)
        while True:
            client.wait_msg()                            #wait message
            
    except Exception  as ex_results:
        print('exception1',ex_results)
    finally:
        #if(client is not None):
        #    client.disconnect()
        wlan.disconnect()
        wlan.active(False)
 