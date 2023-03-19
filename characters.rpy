
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
            renpy.show("boo talking")
        # show the animated image
        elif event == "slow_done":
            renpy.show("boo -talking")
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

define b = Character("Boo", callback=boo_lip_flap, image="boo")
