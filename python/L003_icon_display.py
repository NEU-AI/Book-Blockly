import ubitmap


wall = ubitmap.BitmapFromFile('L003_WALL_16X6');
while i:
  J = 0
  while J:
    wall.draw(i,J);
    J += 1
    if J > 7:
      J = 0
  i += 1
  if i > 9:
    i = 0
