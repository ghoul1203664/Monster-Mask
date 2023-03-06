# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    scene bg room
    show boo normal at center:
        # we need this line to display boo at the correct size
        # since they're much larger than the game window
        xysize(560, 880)

    b "testing normal"

    b "Quia dignissimos qui quo sequi sint aut debitis perspiciatis. Quia et minus quidem eum repellat provident delectus sint. Aut et sit maxime.."

    "Boo does not talk while we say this..."

    b "But I {i}DO{/i} talk when I say this!{p=0.25}Isn't that cool??"

    call .expression_test

    return


label .expression_test:

    menu:
        b "which expression should I test while talking?"

        "normal":
            b normal "Ok."
        "happy":
            b happy "Ok!"
        "worried":
            b worried"Ok..."

    b "Quia dignissimos qui quo sequi sint aut debitis perspiciatis. Quia et minus quidem eum repellat provident delectus sint. Aut et sit maxime.."

    menu:
        "see another expression?"
        "yes":
            jump .expression_test
        "no":
            pass
    
    "thanks for testing expressions!"

    return


