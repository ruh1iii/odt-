from machine import Pin,PWM
import neopixel
import random
import time

np = neopixel.NeoPixel(Pin(4),16)
alive_players = [0, 1, 2, 3]
brightness=0.5
player_colors = [

    (int(255*brightness), int(80*brightness), int(80*brightness)),

    (int(80*brightness), int(160*brightness), int(255*brightness)),

    (int(80*brightness), int(255*brightness), int(160*brightness)),

    (int(255*brightness), int(200*brightness), int(80*brightness))

]

servo = PWM(19, freq=50)
servo_positions=[43,60,77,94]
button = Pin(15, Pin.IN, Pin.PULL_UP)



player_led_pins = [21, 22, 23, 25]
player_leds = [Pin(pin, Pin.OUT) for pin in player_led_pins]
for p in alive_players:
    player_leds[p].value(1)
bullet_pos = random.randint(0, 5)
chambers = [0, 0, 0, 0, 0, 0]
chambers[bullet_pos] = 1

#spin neopixel
while True:
    segment_size = 16 // len(alive_players)
    spin_cycles = random.randint(20, 40)
    for i in range(spin_cycles):
        selected_player = alive_players[i % len(alive_players)]
        for j in range(16):
            np[j] = (0, 0, 0)
        start = alive_players.index(selected_player) * segment_size
        end = start + segment_size

        
        for j in range(start, end):
            np[j] = player_colors[selected_player]

        np.write()

        time.sleep(0.05)
        

#     for j in range(NUM_PIXELS):
#         np[j] = (0, 0, 0)
#     start = alive_players.selected_player* segment_size
#     end = start + segment_size
# 
#     for j in range(start, end):
#         np[j] = player_colors[selected_player]
# 
#     np.write()

    print(selected_player)
    while button.value() == 1:
        pass

    print("Trigger pressed")
    #if button.value() == 0:
        #duty = servo_positions[selected_player]
        #duty = int((angle / 180) * 102 + 26)
    servo.duty(servo_positions[selected_player])
    print("Servo pointing at Player", selected_player)
    time.sleep(1)
        
        
    result = chambers.pop(0)
    if result == 1:

        for i in range(5):
            player_leds[selected_player].value(0)
            time.sleep(0.1)
            player_leds[selected_player].value(1)
            time.sleep(0.1)

        player_leds[selected_player].value(0)

        alive_players.remove(selected_player)

        bullet_pos = random.randint(0, 5)

        chambers = [0, 0, 0, 0, 0, 0]
        chambers[bullet_pos] = 1

    else:

        player_leds[selected_player].value(1)
