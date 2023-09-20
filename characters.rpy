# Custom Transforms
# one for when characters go offscreen vertically
transform fall_offscreen:
    parallel:
        ease 0.3 yalign 1.0
    parallel:
        ease 0.3 yanchor 0.0



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
    pause 0.1
    "boo normal talk"
    pause 0.1

    repeat

image boo happy talking:
    "boo happy"
    pause 0.1
    "boo happy talk"
    pause 0.1

    repeat

image boo worried talking:
    "boo worried"
    pause 0.1
    "boo worried talk"
    pause 0.1

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
    pause 0.1
    "mummy normal talk"
    pause 0.1

    repeat

image mummy happy talking:
    "mummy happy"
    pause 0.1
    "mummy happy talk"
    pause 0.1

    repeat

image mummy sad talking:
    "mummy worried"
    pause 0.1
    "mummy worried talk"
    pause 0.1

    repeat

define mum = Character("Host", callback=mummy_lip_flap, image="mummy")



init -1 python:
    def tulip_lip_flap(event, **kwargs):
        lip_flap("tulip", event, **kwargs)


define tul = Character("Tulip", callback=tulip_lip_flap, image="tulip")


init -1 python:
    def daisy_lip_flap(event, **kwargs):
        lip_flap("daisy", event, **kwargs)

define dsy = Character("Daisy", callback=daisy_lip_flap, image="daisy")



define cdr = Character("Cheddar")