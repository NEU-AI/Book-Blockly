import network
import utime
import time
from simple import MQTTClient
import ujson
from machine import Pin

led_red = Pin(17,Pin.OUT,Pin.PULL_UP);

def do_connect():
  sta_if = network.WLAN(network.STA_IF);
  ap_if = network.WLAN(network.AP_IF);
  if ap_if.active() == True:
    ap_if.active(False)
  sta_if.active(True)
  sta_if.connect('1-28-1','wifi密码******')
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
    led_red.value(0)
    print("led on!") 
  if state == 0:
    led_red.value(1)
    print("led off!")

# todo1
ProductKey   ='a1RYOMWrWvX'
ClientId     = "123456|securemode=3,signmethod=hmacsha1|"
# todo2
DeviceName   ='skids_led_test'
# todo3
DeviceSecret ='5c43c6a2098c9e5888dc3fcc841a00e8'

#strBroker    = ProductKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"
strBroker    = '106.15.83.29'
Brokerport   = 1883

user_name      = DeviceName+"&"+ProductKey#用户名
#todo 4
user_password  = '6F19164AB24898DA49DAD621C7F61590706E0995'#用户密码

def mqtt_connect():
  print("clientid:",ClientId,"\n","Broker:",strBroker,"\n","User Name:",user_name,"\n","Password:",user_password,"\n")

  client = MQTTClient(client_id = ClientId,server= strBroker,port=Brokerport,user=user_name, password=user_password,keepalive=60) 
  client.set_callback(recvMessage)#设置回调函数
  #please make sure keepalive value is not 0
  client.connect()
  client.subscribe("/sys/"+ProductKey+"/"+DeviceName+"/thing/service/property/set")#订阅主题
  print("mqtt connect done")
  
  while True:
    client.wait_msg()

do_connect()
mqtt_connect()
while True:
  time.sleep(2)

