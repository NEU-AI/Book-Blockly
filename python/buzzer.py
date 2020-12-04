from pyb import Pin, Timer
import time
from time import sleep_ms

#
#C 1 do 256 Hz
#D 2 re 288 Hz
#E 3 mi 320 Hz
#F 4 fa 341又1/3
#G 5 so 384 
#A 6 la 426又2/3
#B 7 si 480

_L_DO = const(256)
_L_RE = const(288)
_L_MI = const(320)
_L_FA = const(341)
_L_SO = const(384)
_L_LA = const(426)
_L_SI = const(480)

_M_DO = const(523)
_M_RE = const(587)
_M_MI = const(659)
_M_FA = const(698)
_M_SO = const(784)
_M_LA = const(880)
_M_SI = const(988)

_H_DO = const(1046)
_H_RE = const(1175)
_H_MI = const(1318)
_H_FA = const(1397)
_H_SO = const(1568)
_H_LA = const(1760)
_H_SI = const(1976)



class BUZZER:
    def  __init__(self, pin,timer, timer_ch):
        # self.timer=Timer(2,freq=freq)
        # self.timer.channel(3,Timer.PWM,pin=Pin('X3'),pulse_width_percent=50)
        self.pin = pin
        self.timer = timer
        self.timer.channel(timer_ch, Timer.PWM, pin=self.pin, pulse_width_percent=50)

    def buzzer(self,ms,freq):
        self.timer.freq(freq)
        print(freq)
        sleep_ms(ms)

    def note(self,ms,lmh,note):
        if lmh==1:
            if note==1:
                self.timer.freq(_L_DO)
            elif note==2:
                self.timer.freq(_L_RE)
            elif note==3:
                self.timer.freq(_L_MI)
            elif note==4:
                self.timer.freq(_L_SO)
            elif note==5:
                self.timer.freq(_L_FA)
            elif note==6:
                self.timer.freq(_L_LA)
            elif note==7:
                self.timer.freq(_L_SI)
        elif lmh==2:
            if note==1:
                self.timer.freq(_M_DO)
            elif note==2:
                self.timer.freq(_M_RE)
            elif note==3:
                self.timer.freq(_M_MI)
            elif note==4:
                self.timer.freq(_M_SO)
            elif note==5:
                self.timer.freq(_M_FA)
            elif note==6:
                self.timer.freq(_M_LA)
            elif note==7:
                self.timer.freq(_M_SI)
        elif lmh==3:
            if note==1:
                self.timer.freq(_H_DO)
            elif note==2:
                self.timer.freq(_H_RE)
            elif note==3:
                self.timer.freq(_H_MI)
            elif note==4:
                self.timer.freq(_H_SO)
            elif note==5:
                self.timer.freq(_H_FA)
            elif note==6:
                self.timer.freq(_H_LA)
            elif note==7:
                self.timer.freq(_H_SI) 
        sleep_ms(ms)

def buzzer_test():
    # mytest=BUZZER(1000)
    mypwm_x3 = BUZZER(pin = Pin('X3'), timer=Timer(3,freq=1000), timer_ch = 3)
    mypwm_x4 = BUZZER(pin = Pin('X4'), timer=Timer(2,freq=1000), timer_ch = 4)
    while 1:
        print("test")
        mypwm_x3.buzzer(1,_L_DO)
        mypwm_x4.buzzer(1,_L_DO)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_RE)
        mypwm_x4.buzzer(1,_L_RE)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_FA)
        mypwm_x4.buzzer(1,_L_FA)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_SO)
        mypwm_x4.buzzer(1,_L_SO)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_LA)
        mypwm_x4.buzzer(1,_L_LA)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_SI)
        mypwm_x4.buzzer(1,_L_SI)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_SO)
        mypwm_x4.buzzer(1,_L_SO)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_FA)
        mypwm_x4.buzzer(1,_L_FA)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_MI)
        mypwm_x4.buzzer(1,_L_MI)
        sleep_ms(1000)
        mypwm_x3.buzzer(1,_L_RE)
        mypwm_x4.buzzer(1,_L_RE)
        sleep_ms(1000)

buzzer_test()