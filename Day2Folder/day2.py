# Write all your codes for Day 2 here.
# COMMENT out the previous task before going on to the next task
print("hello from day2")

########################################################################
# Task 1

for count in range(5):
    print("Neck Hurts")
########################################################################
# Task 2:

name="Apu"

for potato in name:
    print("Give me a "+potato)
print(name)


########################################################################
# Task 3:
for counter in range(9):
    print(counter)


########################################################################
# Task 4:
for count in range(1,11):
    print(count)


########################################################################
# Task 5:
for count in range(2,101,2):
    print(count)


########################################################################
# Task 6:
for count in range(100,0,-1):
    print(count)


########################################################################
# Additional exercises:
for count in range(0,67):
    print(count)
    
for count in range(0,101):
    print(count)

for count in range(7,33):
    print(count)

for count in range(65,100):
    print(count)

for count in range(2,33,2):
    print(count)

for count in range(5,101,5):
    print(count)

for count in range(100,0,-1):
    print(count)

def Teleport():
    agent.teleport_to_player()

player.on_chat("come", Teleport)


def move_forward(steps):
    agent.move(FORWARD, steps)
player.on_chat("forward", move_forward)
def move_back(steps):
    agent.move(BACK,steps)
player.on_chat("back", move_back)
def move_up(steps):
    agent.move(UP,steps)
player.on_chat("up", move_up)
def move_down(steps):
    agent.move(DOWN,steps)
player.on_chat("down", move_down)
def turn_left():
    agent.turn(LEFT)
player.on_chat("left", turn_left)
def turn_right():
    agent.turn(RIGHT)
player.on_chat("right", turn_right)

def bomb():
    agent.set_item(TNT, 64, 1)
    agent.place(FORWARD)
player.on_chat("place_tnt", bomb)

def chop_wood(mine):
    for destroy_wood in range(mine):
        agent.destroy(FORWARD)
        agent.move(FORWARD,1)
    agent.move(BACK,mine)
    agent.collect_all()
player.on_chat("destroy", chop_wood)
