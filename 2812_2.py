import board, neopixel, time

action_blue={}
action_blue[0] = (205,90,90)
action_blue[1] = (8,8,8)
action_blue[2] = (16,16,16)
action_blue[3] = (32,32,32)
action_blue[4] = (64,64,64)
action_blue[5] = (128,128,128)

blue={}
blue[0] = (205,90,90)
blue[1] = (205,90,90)
blue[2] = (205,90,90)
blue[3] = (205,90,90)
blue[4] = (205,90,90)

white={}
white[0] = (8,8,8)
white[1] = (16,16,16)
white[2] = (32,32,32)
white[3] = (64,64,64)
white[4] = (128,128,128)

np = neopixel.NeoPixel(board.D21, 46)

for i in range(46):
    np[i] = white[0]
time.sleep(0.01)

for i in range(46):
    np[i] = white[3]
time.sleep(0.01)

for i in range(46):
    np[i] = white[4]
time.sleep(0.01)

for i in range(46):
    np[i] = white[3]
time.sleep(0.01)

for i in range(46):
    np[i] = blue[0]
time.sleep(0.01)

for i in range(46):
    np[i] = blue[1]
time.sleep(0.01)

for i in range(46):
    np[i] = blue[2]
time.sleep(0.01)

for i in range(46):
    np[i] = blue[3]
time.sleep(0.01)

for i in range(46):
    np[i] = blue[4]
time.sleep(0.01)

for k in range(3):
    for i in range(46):
        for j in range(6):
            if (i + j) >= 46:
                np[i+j-46] = action_blue[j]
            else:
                np[i+j] = action_blue[j]
        time.sleep(0.02)

for i in range(46):
    np[i] = white[3]
time.sleep(0.1)

for i in range(46):
    np[i] = white[0]
time.sleep(0.1)

for i in range(46):
    np[i] = (0,0,0)
time.sleep(0.01)

