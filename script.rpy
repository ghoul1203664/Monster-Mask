﻿# The script of the game goes in this file.


# The game starts here.
# just having it jump in case we want to seperate the labels
# into different files later
label start:
    jump intro


label intro:
    $renpy.movie_cutscene("Splashscreen.mpg")

    scene black with dissolve
    play music "audio/StarlightSolitude.mp3" loop
    
    #show cg one with dissolve
    #Note to self: Show ghosts and ghouls dancing in the city
    voice "audio/Narrator_0_1.wav"
    "{i}Legends whisper of a Monster Masquerade, held every Halloween eve in the heart of Spectre city.{/i}"
    voice "audio/Narrator_0_2.wav"
    "{i}It welcomes lost souls of every kind, living or dead.{/i}"

    #show cg two with dissolve
    #Note to self: Show Boo getting an inviation 
    voice "audio/Narrator_0_3.wav"
    "{i}Strangers share secrets over drinks, as music stirs their spirits and sets their inhibitions free.{/i}"
    voice "audio/Narrator_0_4.wav"
    "{i}Under a mask, {w=0.25}any creature can bare its soul without fear of retribution.{w=0.25} This ball is said to change your undead life forever!{/i}"

    #show cg three with dissolve
    #Note to self: Show Boo walking in the night
    # "[player_name]" "Uh, {w=0.25}I'm just looking for a fun night out to support my girl, Daisy.{p=0.25}She's performing!"
    voice "audio/Narrator_0_5.wav"
    "But will it change the fate of our phantom protagonist for better{w=0.25} or for worse?"

    jump .city_walk


# the formal name for this label is intro.city_walk
# see https://www.renpy.org/doc/html/label.html#label-statement
label .city_walk:
    scene bg city_debug with fade

    play music "audio/NightWalk.mp3" loop

    show boo normal at boo_size, boo_face_left with dissolve: #combining preset anims and sizes
        pos (1.5, 0.0)
        ease 1.0 center
    # play sound "walk.ogg"
    voice "audio/Boo_0_1.mp3"
    b "I think this is the right place…"
 
    show boo: #one time animations
        boo_size
        pause 0.5
        boo_face_left
        pause 0.5
    voice "audio/Boo_0_1_1.mp3"
    b "Who sends a broken map in an invitation?"
    "{i}The map pieces fall out and scatter on the floor,{w=0.25} you pick up each piece and begin to solve the puzzle.{/i}"
    "{i}With careful effort,{w=0.25} you are able to re-construct the map to find the location of the party!{/i}"

    call screen scr_map_minigame

    voice "audio/Boo_0_3.mp3"
    b happy "Phew,That wasn't so bad!"
    
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
        xpos 450
        ypos 965
        action Jump("reception.checking_in")
        idle "pnc/pnc_reception_mummy.png"
        hover "pnc_reception_mummy_hover"
        focus_mask True
screen reception_point_n_click_painting:
    imagebutton:
        xanchor 0.5
        yanchor 0.5

        xpos 420
        ypos 480
        action Jump("reception.inspecting_painting")
        idle "pnc/pnc_reception_painting.png"
        hover "pnc_reception_painting_hover"
        focus_mask True
screen reception_point_n_click_door:
    imagebutton:
        xanchor 0.5
        yanchor 1.0
        xpos 1108
        ypos 880
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

    play music "audio/BeautifulBoy.mp3" loop

    scene bg reception_debug with fade:
        blur 15
        matrixcolor TintMatrix("#808080ff")

    show boo normal at boo_size, boo_face_left:
        pos(0.75, 1.0)
    with dissolve


    b "Now,{w=0.25} where should I go next?" # this line is supposed to cue the player to click on something, can be changed
    
    # make boo dissapear
    hide boo with dissolve
    show bg reception_debug with dissolve:
        blur 0
        matrixcolor TintMatrix("#ffffffff")

label .inspect:
    call screen reception_point_n_click with dissolve

label .inspecting_painting:
    "[player_name]" "Ooh!{w=0.25} What a lovely painting!"
    "[player_name]" "I'll have to show it to Daisy later on!"
    jump .inspect

label .inspecting_door:
    if checked_in:
        "[player_name]" "Time to go in!"
        jump enter_party
    else:
        "[player_name]" "Oops!{w=0.25} I have to check in first!"
        jump .inspect

label .checking_in:
    if checked_in:
        "[player_name]" "I've already checked in."
        jump .inspect


    scene bg reception_debug:
        blur 15
        matrixcolor TintMatrix("#808080ff")

    show boo normal at boo_size, boo_face_left:
        pos(0.75, 1.0)
    show mummy normal at mummy_size, mummy_face_right:
        pos(0.25, 1.0)
    with dissolve
    voice "audio/Boo_0_4.mp3"   
    b "Hello,{w=0.25} I’m Boo and...{w=0.25} I’m here for the party?"
    voice "audio/Maat_0_1.mp3"   
    mum "You're our first Boo of the night."
    voice "audio/Maat_0_2.mp3"   
    mum happy "Ah!{w=0.25} Yes, I see your name,{w=0.25} and may I see your invitation?"
    voice "audio/Boo_0_5.mp3"  
    b "Sure thing!"

label .rename:
    voice "audio/Maat_0_3.mp3" 
    mum normal "Did you want to go by a different name?{w=0.25} Boo is a bit vanilla."
    voice "audio/Maat_0_4.mp3" 
    mum "You know the saying:{w=0.25} Whatever happens at the Monster Masquerade{w=0.25} stays at the Monster Masquerade.{w=0.25} Haha!"
    voice "audio/Maat_0_5.mp3" 
    mum "But, that’s just an oldfolk’s tale.{w=0.25} You’re free to share your experiences on social media and whatnot!{w=0.25} This is the 21st century for crying out loud!"


    menu:

        "Would you like to change your name?"

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
    $ invalid_name = False
#Add audio files in for the next update
    if player_name.lower() == "booo":
        mum "Hm.{w=0.25} I suppose you never know where an extra o will take you."
    elif player_name.lower() == "boooo":
        mum "Oo. {w=0.25}That does sound better."
    elif player_name.lower() == "booooo":
        mum "Ooo. {w=0.25}It's spookier now than before."
    elif player_name.lower() == "boooooo":
        mum "A lovely idea to extend your name. {w=0.25}It's much more mysterious."
    elif player_name.lower() == "booooooo":
        mum "Booooooo is fine, {w=0.25}as long as you're not booing our performers."
    elif player_name.lower() == "boooooooo":
        mum "Boooooooo is rather long, {w=0.25}don't you think? {w=0.25}Suit yourself"
    elif player_name.lower() == "booooooooo":
        mum "BooOOOOooo!{w=0.25} It's quite a lungful.{w=0.25}  Very bold."
    elif player_name.lower() == "Lophii":
        mum "Someone already has that name!"
        $invalid_name = True
    elif player_name.lower() == "tulip":
        mum "Someone already has that name!{w=0.25} She has such a pretty dress…"
        $ invalid_name = True
    elif player_name.lower() == "spaghetti":
        mum "Someone already has that name!{w=0.25} Kind of an odd name if you ask me…"
        $ invalid_name = True
    elif player_name.lower() == "cheddar":
        mum "I'm afraid that name is already taken by our goblin chef."
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
        mum "She’s one of the performers. {w=0.25}Oh{w=0.25} I’m such a big fan!"
        $ invalid_name = True
    elif player_name.lower() == "host":
        mum "That’s…{w=0.25} my name?"
        $ invalid_name = True
    elif player_name.lower() == "lotus":
        mum "Someone already has that name!"
        $ invalid_name = True
    elif player_name.lower() == "lupin":
        mum "I wonder if he’s seen the anime…"
        $ invalid_name = True
    elif player_name.lower() == "moth":
        mum "Apologies, {w=0.25}that name has already been taken!"
        $ invalid_name = True
    elif player_name.lower() == "princess":
        mum "Oh, {w=0.25}that’s a special guest. {w=0.25}Unfortunately she already RSVPd with that name."
        $ invalid_name = True
    elif player_name.lower() == "aranea":
        mum "Sorry!{w=0.25} We have a special guest attending with that chosen name. {w=0.25}Apparently, {w=0.25}she’s an influencer."
        $ invalid_name = True
    elif player_name.lower() == "wish":
        mum "When you wish upon a star! {w=0.25}Oh! {w=0.25}That’s a copyrighted song, {w=0.25}I shouldn’t sing it. {w=0.25}Yeah, {w=0.25}that name has already been taken."
        $ invalid_name = True
    elif player_name.lower() == "lagoon" or player_name.lower() == "lagoon man":
        mum "Ocean man, {w=0.25}take it by the hand {w=0.25}don’t you understand?? {p=0.25}That name is taken"
        $ invalid_name = True
    elif player_name.lower() == "peacock":
        mum "A peculiar fellow came in with that name... {w=0.25}They signed up last minute!"
        $ invalid_name = True
    elif player_name.lower() == "tom":
        mum "Honk Honk! {w=0.25}Hehe... {w=0.25}Oh! {w=0.25}My apologies, {w=0.25}that name was already taken"
        $ invalid_name = True
    elif player_name.lower() == "grim":
        mum "I heard Grim Reapers is an occupation title and not really a singular character. {w=0.25}That is what the guest told me when RSVPing into the party."
        $ invalid_name = True
    elif player_name.lower() == "peppy":
        mum "Someone already has that name! {w=0.25}Her magic tricks are out of this world! "
        $ invalid_name = True

    if invalid_name:
        jump .rename_input


    "You'd prefer [player_name] tonight then?"

    menu:
        "Yes":
            if player_name.lower() == "boo":
                mum "Sticking with the classic I see~"
            jump .rename_finished
        "No":
            jump .rename_input


label .rename_finished:
    voice "audio/Maat_0_35.mp3"  
    mum "Everything checks out!{w=0.25} The entrance is the door to your right.{w=0.25} Have fun!"
    voice "audio/Boo_0_6.mp3"   
    b "Thank you!"
    # mum "Oh!{w=0.25} One more thing.{w=0.25} Take this."

    # "CHEST KIT TUTORIAL GOES HERE."

    $ checked_in = True    
    # make boo dissapear

    hide boo
    hide mummy
    show bg reception_debug:
        blur 0
        matrixcolor TintMatrix("fff")
    with dissolve

    jump .inspect
    
    
    
label enter_party:
    scene bg stairs_debug with fade
    play sound "audio/crowd.mp3" loop


    "{i}Finally, we made it to the party. All manner of monsters meanders about. It's a night for meeting new souls—{/i}"
    voice "audio/Tulip_0_1.mp3"
    "Tulip" "Hey Boo! Over here!"
    "{i}Ah! It’s your friend Tulip.{/i}"
    jump chapter_1