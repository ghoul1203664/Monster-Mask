# Custom Transforms
# one for when characters go offscreen vertically
transform fall_offscreen:
    parallel:
        ease 0.3 yalign 1.0
    parallel:
        ease 0.3 yanchor 0.0

transform character_anchor:
    anchor (0.5, 1.0)

transform boo_size:
    character_anchor
    xsize (1500*3/10)
    ysize (2800*3/10)

transform boo_face_left:
    boo_size
    xsize -(1500*3/10)


transform tulip_size:
    character_anchor
    xsize (1500*3/10)
    ysize (2800*3/10)

transform tulip_face_left:
    tulip_size
    xsize -(1500*3/10)

transform daisy_size:
    character_anchor
    xsize (1500*3/10)
    ysize (2800*3/10)

transform daisy_face_left:
    daisy_size
    xsize -(1500*3/10)

transform cheddar_size:
    character_anchor
    xsize (1500*3/10)
    ysize (2800*3/10)

transform cheddar_face_left:
    cheddar_size
    xsize -(1500*3/10)

# got odd mummy image sizes in demo
# please don't question it
transform mummy_size:
    character_anchor
    xsize (301*2)
    ysize (427*2)

transform mummy_face_right:
    mummy_size
    xsize -(301*2)


transform talk_bob:
    linear 0.1 yoffset 0
    repeat

transform talk_low:
    linear 0.1 yoffset 0


# Character definition for Player (Boo)
init -1 python:
    # want to see if I can make this more generic later on
    def lip_flap(char_name, event, **kwargs):
        # turn off if we're done speaking
        if event == "show":
            renpy.show("%s talking" % char_name)
        # show the animated image
        elif event == "slow_done":
            renpy.show("%s -talking" % char_name)
            renpy.restart_interaction()
        
    # Used to make boo speak
    def boo_lip_flap(event, **kwargs):
        lip_flap("boo", event, **kwargs)

image boo normal talking:
    "boo normal"
    talk_low
    pause 0.3
    "boo normal talk"
    talk_bob
    pause 0.2

    repeat

image boo happy talking:
    "boo happy"
    talk_low
    pause 0.3
    "boo happy talk"
    talk_bob
    pause 0.2

    repeat

image boo worried talking:
    "boo worried"
    talk_low
    pause 0.3
    "boo worried talk"
    talk_bob
    pause 0.2

    repeat



default player_name = "Boo"
define b = Character("[player_name]", callback=boo_lip_flap, image="boo")

# mummy definition
init -1 python:
    # Used to make boo speak
    def mummy_lip_flap(event, **kwargs):
        lip_flap("mummy", event, **kwargs)

image mummy normal talking:
    "mummy normal"
    pause 0.3
    "mummy normal talk"
    pause 0.2

    repeat

image mummy happy talking:
    "mummy happy"
    pause 0.3
    "mummy happy talk"
    pause 0.2

    repeat

image mummy sad talking:
    "mummy worried"
    pause 0.3
    "mummy worried talk"
    pause 0.2

    repeat

define mum = Character("Host", callback=mummy_lip_flap, image="mummy")



init -1 python:
    def tulip_lip_flap(event, **kwargs):
        lip_flap("tulip", event, **kwargs)

image tulip normal talking:
    "tulip normal"
    talk_low
    pause 0.3
    "tulip normal talk"
    talk_bob
    pause 0.2

    repeat

image tulip happy talking:
    "tulip happy"
    talk_low
    pause 0.3
    "tulip happy talk"
    talk_bob
    pause 0.2

    repeat

image tulip worried talking:
    "tulip worried"
    talk_low
    pause 0.3
    "tulip worried talk"
    talk_bob
    pause 0.2

    repeat

define tul = Character("Tulip", callback=tulip_lip_flap, image="tulip")


init -1 python:
    def daisy_lip_flap(event, **kwargs):
        lip_flap("daisy", event, **kwargs)

image daisy normal talking:
    "daisy normal"
    talk_low
    pause 0.3
    "daisy normal talk"
    talk_bob
    pause 0.2

    repeat

image daisy happy talking:
    "daisy happy"
    talk_low
    pause 0.3
    "daisy happy talk"
    talk_bob
    pause 0.2

    repeat

image daisy worried talking:
    "daisy worried"
    talk_low
    pause 0.3
    "daisy worried talk"
    talk_bob
    pause 0.2

    repeat
define dsy = Character("Daisy", callback=daisy_lip_flap, image="daisy")


init -1 python:
    def cheddar_lip_flap(event, **kwargs):
        lip_flap("cheddar", event, **kwargs)

image cheddar normal talking:
    "cheddar normal"
    talk_low
    pause 0.3
    "cheddar normal talk"
    talk_bob
    pause 0.2

    repeat
define cdr = Character("Cheddar", callback=cheddar_lip_flap, image="daisy")


define lup = Character("Lupin", callback=cheddar_lip_flap, image="lupin")


define mor = Character("Lophii Morfs", callback=cheddar_lip_flap, image="lophii")