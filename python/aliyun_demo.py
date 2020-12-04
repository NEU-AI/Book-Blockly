from machine import Pin
import dht
import time
import network
from umqtt import simple as mqtt
import _thread
import ujson

ALINK_PROP_SET_METHOD='thing.service.property.set'
led=Pin(2,Pin.OUT,value=0)
state = 0
def threadPublish():
  while True:
    time.sleep(2)
    d.measure()
    print(d.humidity())
    print(d.temperature())
    send_mseg={"params":{"Temperature":d.temperature(),"Humidity":d.humidity()},"method":"thing.service.property.set"}
    client.publish(topic=" ",msg=str(send_mseg),qos=1,retain=False)


def receiveMessage():
  while True:
    client.wait_msg()
#接收信息。接收到的信息是json格式，要进行解析。
def recvMessage(topic,msg):
  parsed=ujson.loads(msg)
  str=parsed["params"]
  print(str)
  print(type(parsed["params"]))
  print(str.get("PowerSwitch"))
  global state
  state=str.get("PowerSwitch")
  if state == 1:
    led.value(1)
    print("led on!") 
  if state == 0:
    led.value(0)
    print("led off!")
   
d=dht.DHT11(Pin(23))
wlan=network.WLAN(network.STA_IF)  
wlan.active(True)
wlan.connect('','')#连接WIFI
ProductKey=''
DeviceName=''
DeviceSecret=''
CLIENT_ID=''
user_name=''#用户名
user_password=''#用户密码
SERVER= ""#阿里云物联网平台地址
PORT=1883
client = mqtt.MQTTClient(client_id=CLIENT_ID, server=SERVER, port=PORT, user=user_name, password=user_password, keepalive=60)
client.connect()
client.set_callback(recvMessage)#设置回调函数
client.subscribe(" ")#订阅主题

while True:
  d.measure()
  print(d.humidity())
  print(d.temperature())
  send_mseg={"params":{"Temperature":d.temperature(),"Humidity":d.humidity()},"method":"thing.service.property.set"}
  client.publish(topic=" ",msg=str(send_mseg),qos=1,retain=False)
  time.sleep(2)
_thread.start_new_thread(receiveMessage,())#开启多线程
