﻿# The script of the game goes in this file.


# The game starts here.
# just having it jump in case we want to seperate the labels
# into different files later
label start:
    jump reception


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


# screen for reception point and click, as well as it's different states
image pnc_reception_mummy_hover:
    "pnc/pnc_reception_mummy.png"
    zoom 1.1
    matrixcolor TintMatrix("DDDDDDFF")

image pnc_reception_painting_hover:
    "pnc/pnc_reception_painting.png"
    zoom 1.1
    matrixcolor TintMatrix("DDDDDDFF")

image pnc_reception_door_hover:
    "pnc/pnc_reception_door.png"
    zoom 1.1
    matrixcolor TintMatrix("DDDDDDFF")

screen reception_point_n_click_mummy:
    imagebutton:
        xanchor 0.5
        yanchor 1.0
        xpos 574
        ypos 813
        action Jump("reception.checking_in")
        idle "pnc/pnc_reception_mummy.png"
        hover "pnc_reception_mummy_hover"
        focus_mask True
screen reception_point_n_click_painting:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 259 + 639 / 2 # adjusted based on image width
        ypos 57 + 413 / 2
        action Jump("reception.inspecting_painting")
        idle "pnc/pnc_reception_painting.png"
        hover "pnc_reception_painting_hover"
        focus_mask True
screen reception_point_n_click_door:
    imagebutton:
        xanchor 0.5
        yanchor 1.0
        xpos 1248 + 517 / 2 # adjusted based on image width
        ypos 234 + 519
        action Jump("reception.inspecting_door")
        idle "pnc/pnc_reception_door.png"
        hover "pnc_reception_door_hover"
        focus_mask True
screen reception_point_n_click:
    use reception_point_n_click_painting
    use reception_point_n_click_mummy
    use reception_point_n_click_door

default checked_in = False

label reception:
    scene bg reception_debug with fade:
        blur 15
        matrixcolor TintMatrix("#808080ff")

    show boo normal with easeinright:
        xysize ((1400*4/10), (2200*4/10))
        anchor (0.5, 1.0)
        pos(0.75, 0.95)

    b "Phew!{w=0.25} Made it!"

    b "Now, where should I go next?" # this line is supposed to cue the player to click on something, can be changed
    
    # make boo dissapear
    show boo at fall_offscreen
    show bg reception_debug with dissolve:
        blur 0
        matrixcolor TintMatrix("#ffffffff")

label .inspect:
    call screen reception_point_n_click with dissolve

label .inspecting_painting:
    b "Ooh!{w=0.25} That's a nice painting!"
    jump .inspect

label .inspecting_door:
    if checked_in:
        b "time to go in!"
        jump .inspect # TODO: Make this take you to the next scene
    else:
        b "Oops!{w=0.25} I have to check in first!"
        jump .inspect

label .checking_in:
    if checked_in:
        b "I've already checked in."
        jump .inspect

    show boo normal with easeinright:
        xysize ((1400*4/10), (2200*4/10))
        anchor (0.5, 1.0)
        pos(0.75, 0.95)
    show mummy normal with easeinleft:
        xysize ((1400*4/10), (2200*4/10))
        anchor (0.5, 1.0)
        pos(0.25, 0.95)

    b "Hello,{w=0.25}  I’m Boo and...{w=0.25} I’m here for the party?"
    mum "Let’s see here.."
    mum happy "Ah!{w=0.25} Yes, I see your name,{w=0.25} and may I see your invitation?"
    b "Sure thing!"
    "Boo hands the invitation to The Host."

label .rename:

    mum normal "And did you want to change your name for the night?"

    menu:
        "Yes":
            jump .rename_input            
        "No":
            mum "Very well then!"
    
    jump .rename_finished

label .rename_input:
    python:
        player_name = renpy.input("(Enter your name)")
        player_name = player_name.strip()

        if not player_name:
            player_name = "Boo"

    default invalid_name = False

    if player_name.lower() == "heart":
        mum "Someone already has that name!"
        $ invalid_name = True
    elif player_name.lower() == "tulip":
        mum "Someone already has that name!{w=0.25} She has such a pretty dress…"
        $ invalid_name = True
    elif player_name.lower() == "spaghetti":
        mum "Someone already has that name!{w=0.25} Kind of an odd name if you ask me…"
        $ invalid_name = True
    elif player_name.lower() == "cheddar":
        mum "I'm afraid that name is already taken by our Goblin Chef."
        $ invalid_name = True
    elif player_name.lower() == "rind":
        mum "Can’t take one of the performer’s names!"
        $ invalid_name = True
    elif player_name.lower() == "marrow":
        mum "That’s one of the performers!{w=0.25} He’s not here yet{w=0.25} but, did RSVP it so we can’t have you take it. "
        $ invalid_name = True
    elif player_name.lower() == "t-bone" or player_name.lower() == "t bone " or player_name.lower() == "tbone":
        mum "Can’t take one of the performer’s names!"
        $ invalid_name = True
    elif player_name.lower() == "daisy" or player_name.lower() == "daisy bell":
        mum "She’s one of the performers. {w=0.25}Oh {0.25}I’m such a big fan!"
        $ invalid_name = True
    elif player_name.lower() == "fresca":
        mum "Someone already has that name!"
        $ invalid_name = True
    elif player_name.lower() == "lupin":
        mum "I wonder if he’s seen the anime…"
        $ invalid_name = True



    if invalid_name:
        jump .rename_input


    "You'd prefer [player_name] tonight then?"

    menu:
        "Yes":
            if player_name.lower() == "boo":
                "Sticking with the classic I see~"
            jump .rename_finished
        "No":
            jump .rename_input


label .rename_finished:
    mum "Everything checks out!{w=0.25} The entrance is the door to your right.{w=0.25} Have fun!"
    b "Thank you!"
    mum "Oh!{w=0.25} One more thing.{w=0.25} Take this."

    "CHEST KIT TUTORIAL GOES HERE."

    $ checked_in = True    
    # make boo dissapear
    show boo at fall_offscreen
    show mummy at fall_offscreen
    show bg reception_debug with dissolve:
        blur 0
        matrixcolor TintMatrix("#ffffffff")
    jump .inspect