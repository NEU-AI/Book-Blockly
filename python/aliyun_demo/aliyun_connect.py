import network
import utime
import time
from simple import MQTTClient
import _thread
import ujson

def do_connect():
  sta_if = network.WLAN(network.STA_IF);
  ap_if = network.WLAN(network.AP_IF);
  if ap_if.active() == True:
    ap_if.active(False)
  sta_if.active(True)
  sta_if.connect('NEUI111','83766158')
  while sta_if.isconnected() == False:
    utime.sleep_ms(1000);
  print("wifi connect done")

#接收信息。接收到的信息是json格式，要进行解析。
def recvMessage(topic,msg):
  parsed=ujson.loads(msg)
  str=parsed["params"]
  print(str)
  print(type(parsed["params"]))
  print(str.get("powerstate"))
  global state
  state=str.get("powerstate")
  if state == 1:
    print("led on!") 
  if state == 0:
    print("led off!")

ProductKey   ='a1h68Ao3GZ7'
ClientId     = "123456|securemode=3,signmethod=hmacsha1|"
DeviceName   ='test1'
DeviceSecret ='1044ed1deba3f7ad33891d337e89f691'

#strBroker    = ProductKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"
strBroker    = '106.15.83.29'
Brokerport   = 1883

user_name      = DeviceName+"&"+ProductKey#用户名
user_password  = 'C037F3C23C0F580FE7C5D8E415E00A7783F9C48E'#用户密码

def mqtt_connect():
  print("clientid:",ClientId,"\n","Broker:",strBroker,"\n","User Name:",user_name,"\n","Password:",user_password,"\n")

  client = MQTTClient(client_id = ClientId,server= strBroker,port=Brokerport,user=user_name, password=user_password,keepalive=60) 
  client.set_callback(recvMessage)#设置回调函数
  #please make sure keepalive value is not 0
  client.connect()
  client.subscribe("/sys/"+ProductKey+"/test1/thing/service/property/set")#订阅主题

  while True:
    time.sleep(3)
  #client.disconnect()

def receiveMessage():
  while True:
    client.wait_msg()

do_connect()
#gc.collect()
mqtt_connect()
_thread.start_new_thread(receiveMessage,())#开启多线程
while True:
  time.sleep(2)

