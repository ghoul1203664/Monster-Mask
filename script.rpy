# The script of the game goes in this file.


# The game starts here.
# just having it jump in case we want to seperate the labels
# into different files later
label start:
    jump intro.city_walk


label intro:
    show cg one with dissolve
    "SpookyWeen | ENTRY:{w=0.25} 11/4/20XX"

    show cg two with dissolve
    "We just got the results back for the house decorations contest and we got 5th place."
    "I guess it's because we were on a limited budget compared to other houses. (ToT)/~~~ "

    show cg three with dissolve

    "Apparently the Haunted House event we hosted attracted a lot of visitors{w=0.25} and we were able to gain good revenue from it."
    "Maybe I'll attend Jumpscare Bootcamp next time."

    show cg four with dissolve
    "Then,{w=0.25} the Masquerade party,{w=0.25} I'd say that was the most memorable party ever!"
    "I met some very interesting ghouls that day.{p=0.25}Everyone was dressed so nicely,{w=0.25}  I honestly haven't felt so ecstatic in a while..."

    jump .city_walk


# the formal name for this label is intro.city_walk
# see https://www.renpy.org/doc/html/label.html#label-statement
label .city_walk:
    scene bg city_debug with fade

    show boo normal at center with easeinright: # custom transition instead of easeinright might be nice
        # we used the base image size * 0.4 for display in game
        # consider 560x880 the unaltered size for squash and stretch
        # PLEASE not that ANY floats in those paranthesis will cause renpy to
        # think we mean a percentage of the screen! Causes LOTS of graphical weirdness
        xysize ((1400*4/10), (2200*4/10))
        anchor (0.5, 1.0)
    b "I think this is the right area…{p=0.25}Where did the invitation say it was again?"
    
    show boo:
        xsize -560
        pause 0.5
        xsize 560
        pause 0.5
    b "..."

    show boo worried:
        ease 0.1 xysize ((1400*3/10), (2200*5/10))
        ease 0.1 xysize ((1400*4/10), (2200*4/10))
        
    b "H-{w=0.25}Huh!?!"
    b "Which way was I supposed to go!?"
    
    "MINIGAME GOES HERE"

    b happy "That wasn't so bad!"

    jump reception


label reception:
    scene bg reception_debug with fade

    show boo normal with easeinright:
        xysize ((1400*4/10), (2200*4/10))
        anchor (0.5, 1.0)
        pos(0.75, 0.95)

    b "Phew!{w=0.25} Made it!"

    return


