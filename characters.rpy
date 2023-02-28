
# Character definition for Player (Boo)

init -1 python:
    def boo_lip_flap(event, **kwargs):
        # Used to make boo speak

        # turn off if we're done speaking
        if event == "show":
            renpy.show("boo talking")
        # show the animated image
        elif event == "slow_done":
            renpy.show("boo -talking")
            renpy.restart_interaction()


image boo normal talking:
    "boo normal"
    pause 0.1
    "boo normal talk"
    pause 0.1

    repeat


define b = Character("Boo", callback=boo_lip_flap)
