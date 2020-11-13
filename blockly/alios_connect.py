from simple import MQTTClient
from machine import Pin
import network
import time
import machine
# import dht
from machine import Timer
 
SSID="setting..."
PASSWORD="loading...@"
 
SERVER ='a1h68Ao3GZ7.iot-as-mqtt.cn-shanghai.aliyuncs.com'  #MQTT Server: LGSODS81VJ.iotcloud.tencentdevices.com
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
    while(wlan.ifconfig()[0]=='0.0.0.0'):
        time.sleep(1)
    print(wlan.ifconfig())
 
def apptimerevent(mytimer):
    try:
        # sensordata=ReadTemHum()
        sensordata=(10,10)
        mymessage='{"CurrentTemperature": %d ,"CurrentHumidity": %d }'%(sensordata[0],sensordata[1])
        client.publish(topic=publish_TOPIC,msg= mymessage, retain=False, qos=0)
    except Exception as ex_results2:
        print('exception',ex_results2)
        mytimer.deinit()
    finally:
        machine.reset()

#Catch exceptions,stop program if interrupted accidentally in the 'try'
# def ReadTemHum():
#     mydht.measure()
#     tem=mydht.temperature()
#     hum=mydht.humidity()
#     data=[tem,hum]
#     print(data)
    
#     return data
    
if __name__=='__main__':
    try:
        # mydht=dht.DHT11(machine.Pin(4))
        connectWifi(SSID,PASSWORD)
        client = MQTTClient(CLIENT_ID,SERVER,PORT,username,password,60)     #create a mqtt client
        print(client)
        client.set_callback(sub_cb)                         #set callback
        client.connect()                                    #connect mqtt
        client.subscribe(subscribe_TOPIC)                   #client subscribes to a topic
        mytimer=Timer(0)
        mytimer.init(mode=Timer.PERIODIC, period=5000,callback=apptimerevent)
        while True:
            client.wait_msg()                            #wait message
            
    except Exception  as ex_results:
        print('exception1',ex_results)
    finally:
        if(client is not None):
            client.disconnect()
        wlan.disconnect()
        wlan.active(False)
 