# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Boo")


# The game starts here.
# just having it jump in case we want ot seperate the stuff out later
label start:

    jump intro


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
    "Then, the Masquerade party,{w=0.25} I'd say that was the most memorable party ever!"
    "I met some very interesting ghouls that day.{p=0.25}Everyone was dressed so nicely,{w=0.25}  I honestly haven't felt so ecstatic in a while..."

    jump .city_walk


# the formal name for this label is intro.city_walk
# see https://www.renpy.org/doc/html/label.html#label-statement
label .city_walk:
    scene bg city_debug with fade

    show boo normal with dissolve
    b "I think this is the right area…{p=0.25}Where did the invitation say it was again?"
    
    show boo worry with dissolve
    b "..."
    b "H-Huh!?!"
    
    "MINIGAME GOES HERE"


    return


