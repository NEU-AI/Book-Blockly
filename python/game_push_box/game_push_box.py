from machine import Pin
import ubitmap
import screen
import utime
import text


def boy_move(x, y, x_step, y_step):
  global map_list
  global map_draw
  global target_list
  map_list[(y + y_step)][(x + x_step)] = map_list[y][x]
  tmp = 0
  for target in target_list:
    if target[0] == x and target[1] == y:
      tmp = 2
  map_list[y][x] = tmp
  image_disp(x, y)
  image_disp(x + x_step, y + y_step)

def key_scan():
  global key_state
  global key_last_value
  key_current_value = [1,1,1,1]
  i = 0
  for key in key_list:
    key_current_value[i] = key.value();

    i += 1
  i = 0
  for value in key_current_value:
    if value == 0 and key_last_value[i] == 1:
      key_state[i] = 1
    i += 1
  key_last_value = key_current_value

def lcd_refresh():
  global map_list
  global map_draw
  x = 210
  for l in map_list:
    y = 0
    for data in l:
      map_draw[data].draw(x,y);
      y += 30
    x -= 30

def image_disp(x, y):
  px = 210 - y * 30
  py = x * 30
  map_draw[map_list[y][x]].draw(px,py);

def boy_move_xy(x, y, x_step, y_step):
  global map_list
  ret = -1
  next2 = map_list[(y + y_step)][(x + x_step)]
  if next2 == 0 or next2 == 2:
    boy_move(x, y, x_step, y_step)
    ret = 0
  if next2 == 3:
    next_next = map_list[(y + (y_step + y_step))][(x + (x_step + x_step))]
    if next_next == 0 or next_next == 2:
      boy_move(x + x_step, y + y_step, x_step, y_step)
      boy_move(x, y, x_step, y_step)
      ret = 0
  return ret

def target_list_init():
  global map_list
  global target_list
  y = 0
  for line in map_list:
    x = 0
    for data in line:
      if data == 2:
        temp_list = [x, y]
        target_list.append(temp_list)
      x += 1
    y += 1
  print(target_list)

def state_check():
  global target_list
  global map_list
  game_state = 0
  for point_xy in target_list:
    x = point_xy[0]
    y = point_xy[1]
    a = map_list[y][x]
    if a != 3:
      game_state = 1
  return game_state


s1 = Pin(36,Pin.IN,Pin.PULL_UP);
s2 = Pin(39,Pin.IN,Pin.PULL_UP);
s3 = Pin(34,Pin.IN,Pin.PULL_UP);
s4 = Pin(35,Pin.IN,Pin.PULL_UP);
key_list = [s1, s2, s3, s4]
key_state = [0,0,0,0]
key_last_value = [1,1,1,1]
screen.clear();
utime.sleep_ms(1000);
qiang = ubitmap.BitmapFromFile('L003_WALL_30X30');
white = ubitmap.BitmapFromFile('L003_white_30X30');
boy = ubitmap.BitmapFromFile('L003_BOY_30X30');
box = ubitmap.BitmapFromFile('L003_BOX_30X30');
star = ubitmap.BitmapFromFile('L003_STAR_30X30');
map_draw = [white, qiang, star, box, boy]
l0 = [0,0,1,1,1,1,0,0]
l1 = [0,0,1,2,2,1,0,0]
l2 = [0,1,1,0,2,1,1,0]
l3 = [0,1,0,0,3,2,1,0]
l4 = [1,1,0,3,0,0,1,1]
l5 = [1,0,0,1,3,3,0,1]
l6 = [1,0,4,0,0,0,0,1]
l7 = [1,1,1,1,1,1,1,1]
map_list = [l0, l1, l2, l3, l4, l5, l6, l7]
target_list = []
target_list_init()
p_step = 1
boy_x = 2
boy_y = 6
x_step = 0
y_step = 0
step_count = 0
lcd_refresh()
while True:
  utime.sleep_ms(30);
  key_scan()
  i = 0
  x_step = 0
  y_step = 0
  for state in key_state:
    if state == 1:
      key_state[i] = 0
      if i == 0:
        x_step = 1
      elif i == 1:
        y_step = 1
      elif i == 2:
        x_step = -1
      elif i == 3:
        y_step = -1
    i += 1
  if x_step != 0 or y_step != 0:
    if boy_move_xy(boy_x, boy_y, x_step, y_step) == 0:
      boy_x += x_step
      boy_y += y_step
      step_count += 1
      text.draw(str(step_count),0,250,0xff0000,0xffffff);
      if state_check() == 0:
        print('胜利！')
        text.draw('胜利！',0,280,0xff0000);
