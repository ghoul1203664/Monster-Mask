define talked_to_lupin = "Lu"
define talked_to_lophii = "Lo"
default talked_to_at_table = ""

define foodChoice_brew = "Brew"
define foodChoice_cheddar = "Cheddar"
define foodChoice_spider = "Spider"
default foodChoice = ""


label chapter_1:
    scene black with fade
    centered "{color=#fff}Chapter 1{/color}"

    scene bg stairs_debug with fade

    show tulip normal at left, tulip_size, tulip_face_left with dissolve:

        tulip_size
        tulip_face_left
        pos(0.3, 1.0)

    #No voice lines
    voice"audio/Tulip_1_2.mp3"
    tul "How it goin’ girl?{w=0.25} Glad that you made it."

 
        

    show daisy worried at right, daisy_size, daisy_face_left with dissolve: 
        daisy_size    
        pos(0.7, 1.0)
    
    voice "audio/Daisy_1_1.mp3"       
    dsy worried "Yeah, we were getting worried!"
    
    show boo normal at center, boo_size with dissolve:
        boo_size
        pause 0.5
        boo_face_left
        pause 0.5
    
    voice "audio/Boo_1_1.mp3"
    b "Sorry for the wait!{w=0.25} I got lost on the way,{w=0.25} and almost dropped a piece of the map!" 
    voice "audio/Tulip_1_3.mp3" 
    tul "It’s chill.{w=0.25} You made it just in time to see Daisy perform!{w=0.25}Ooo I’m so excited to see what she’s been cookin all these months!"

    show boo:
        boo_size

    voice "audio/Daisy_1_2_2.mp3"       
    dsy happy "Speaking of that,{w=0.25} I gotta check on the boys.{w=0.25} Marrow isn’t here yet and we’re running out of time.{w=0.25} I’ll see you all later!"
  
    voice "audio/Boo_1_2.mp3"
    b "Alright,{w=0.25} break a leg!"
    voice "audio/Daisy_1_2.mp3"
    dsy happy "Thanks!"

    hide daisy with dissolve
    show bg stairs2_debug with fade

    show boo:
        pos(0.7, 1.0)
        boo_face_left
    show tulip:
        pos(0.3, 1.0)
    with ease

     
    voice "audio/Daisy_1_3.mp3"
    "Daisy" "Hello,{w=0.25} hope you’re all having a spooktacular time tonight night!"
    voice "audio/Daisy_1_4.mp3"
    "Daisy" "We're the Prime-Ribs and we’ll be presenting a very fun set called: {w=0.25}  Fruit Phone!"
    play music "audio/FruitPhone1.mp3" loop
    pause 1.5

    show boo:
        pos(0.6, 1.0)
        boo_face_left
    show tulip:
        pos(0.4, 1.0)
    with ease

    voice "audio/Tulip_1_4.mp3"
    tul normal "So, {w=0.25}whatcha been up to lately?"


    
    menu:
        "Tulip picks up the menu and scans for any dishes she might want to try.{w=0.25} She glances at you,{w=0.25} awaiting your reply."
        
        "Not much.":
            voice "audio/Boo_1_3.mp3"
            b normal "Just getting ready for the ball."
            voice "audio/Boo_1_4.mp3"
            b worried "I did hear a strange noise today {w=0.25} and I thought it was another exterminator on the hunt."
            voice "audio/Tulip_1_5.mp3"
            tul worried "Oh no!"
            voice "audio/Boo_1_5.mp3"
            b normal "It was a false alarm,{w=0.25} just some kids in  costumes looking for a spooky place to check out."
            voice "audio/Tulip_1_6.mp3"
            tul normal "Betcha they were just- {w=0.25} too scared of how awesome you are. Ya know?"
            voice "audio/Boo_1_6.mp3"           
            b worried "Haha..."
        
        "A lot.":
            voice "audio/Boo_1_7.mp3" 
            b normal "I had sooo much to do today. You should see how I decorated the mansion!"
            voice "audio/Boo_1_8.mp3"
            b happy "I really tried to work on my jumscare face this season, but it was a total flop…"
            voice "audio/Boo_1_9.mp3" 
            b normal "I’ve just been up to so many last-minute things!!  I wish Biggs and Buggs had planned better.."
            voice "audio/Boo_1_10.mp3" 
            b happy "But!{w=0.25}  Good thing I found these new shoes just in time for the party"
            voice "audio/Boo_1_11.mp3"
            b happy "Oh,{w=0.25} and my blog also just reached it’s first anniversary!"
            voice "audio/Tulip_1_7.mp3"             
            tul happy "Yeah!{w=0.25} You should write about us after,{w=0.25} you busy bee!{w=0.25} I’m happy to see you buzzing with excitement over all the thing things you do."
            voice "audio/Tulip_1_8.mp3"
            tul "But take a break sometimes.{w=0.25} Who knows,{w=0.25} you might die twice because of stress!"
            voice "audio/Boo_1_12.mp3"
            b happy "Haha,{w=0.25} yeah."
            voice "audio/Boo_1_12_2.mp3"
            "[player_name]" "{i}YOU CAN DIE TWICE??{/i}" # hard coded name so mouth doesn't move
            voice "audio/Tulip_1_9.mp3"
            tul normal "It’s been kinda wild on my side too,{w=0.25} preparing for the holidays."
            voice "audio/Tulip_1_10.mp3"
            tul worried "I know,{w=0.25} I know.{w=0.25} It’s still spooky season{w=0.25} but we musicians need to get ready EARLY for the biggest event of the year. "
            voice "audio/Tulip_1_11.mp3"  
            tul happy "It's like I always say. It's never too early to learn new jingles but never too late to relearn old classics!"
            voice "audio/Tulip_1_12.mp3"
            tul normal "And that was supposed to rhyme but ya know, that's okay."
            voice "audio/Boo_1_13.mp3"
            b happy "Oooh,{w=0.25} sounds exciting!"

    show boo:
        pos(0.8, 1.0)
    show tulip:
        pos(0.2, 1.0)
    with ease
    
    show cheddar normal at center, cheddar_size, cheddar_face_left with dissolve:
    voice "audio/Cheddar_1_1.mp3"
    cdr "Excuse me!{w=0.25} Are you two ladies ready to order?"
  
    voice "audio/Boo_1_14.mp3"
    b normal "O-{w=0.25}oh!{w=0.25} Yeah,{w=0.25} I’m ready!"
    pause 1
    b worried "..."
    voice "audio/Boo_1_14_2.mp3"
    "[player_name]" "{i}Oh no… {w=0.25}I didn’t even pick up the menu…{w=0.25} what do I do?!?!{/i}"
    voice "audio/Tulip_1_13.mp3"
    tul normal "I’ll get the spaghetti and eyeballs."

    # TODO: make cheddar turn to look at boo's sprite here
    voice"audio/Cheddar_1_2.mp3"
    cdr "Alright,{w=0.25} and how about you?"

    voice "audio/Boo_1_15.mp3"
    b normal "{cps=30}Uh...{w=0.25} I'll have...{/cps}"
    voice "audio/Boo_1_15_2.mp3"
    "[player_name]" "{i}These all look so tasty!{w=0.25} I wish I could order them all!{w=0.25} But I still get phantom fullness when I eat too much...{/i}"

    menu:
        "Chef’s Recommendation":
            $ foodChoice = foodChoice_brew 
   
            voice "audio/Boo_1_16.mp3"
            b "Hmmm…{w=0.25} I don’t know what to choose exactly…{w=0.25} There’s just so many options!{w=0.25} Do you have a,{w=0.25} um…{w=0.25} favorite dish perhaps??"
            voice"audio/Cheddar_1_3.mp3"
            cdr " Why yes we do!{w=0.25} I highly suggest the Witches Brew.{w=0.25} with has potatoes,{w=0.25} carrots,{w=0.25} broccoli,{w=0.25} and marigolds."
            voice"audio/Boo_1_17.mp3"
            b "Ohh,{w=0.25} That sounds wonderful.{w=0.25} I’d love to have that!"
            voice"audio/Cheddar_1_4.mp3"
            cdr "Alrighty-o!{w=0.25} Coming right up."


        "Make something up":
            $ foodChoice = foodChoice_cheddar 
            voice"audio/Boo_1_18.mp3"

            b "ummmm… {w=0.25}Can I get the…{w=0.25} Cheddar Goblin meal?"

            cdr "…"
            voice"audio/Cheddar_1_5.mp3"
            cdr "{i}The kids menu one?{/i}{w=0.25} The one that comes with the Mac n’cheese,{w=0.25} shark drink,{w=0.25} and ghost nuggets?"
            voice"audio/Boo_1_19.mp3"
            b "Yes."
            voice"audio/Boo_1_19_2.mp3"
            "[player_name]" "That's a real dish?!"
            voice"audio/Cheddar_1_6.mp3"
            cdr "Perfect!!"

            # add some sort of shsake to show shock here
            voice"audio/Cheddar_1_7.mp3"
            cdr "That’s one of my many recommendations!{w=0.25} I’ll get your food ready soon!"


        "Quickly glance at the menu":
            $ foodChoice = foodChoice_spider 
            voice"audio/Boo_1_20.mp3"
            b "Lemme get the um-"
            
            "{i}You pick up the menu and skim through the dishes as quickly as possible,{w=0.25} not wanting to keep the others waiting.{/i}"
            voice"audio/Cheddar_1_8.mp3"

            cdr "Do you,{w=0.25} uh,{w=0.25} do you need more time?"
            voice "audio/Tulip_1_14.mp3"
            tul "Yeah,{w=0.25} no rush Boo,{w=0.25} it’s okay!"
            "{i}But you're determined to order at once.{/i}"
            voice"audio/Boo_1_21.mp3"
            b "Nono!{w=0.25} I got it!{w=0.25} I got it!{w=0.25} I’ll get the Spider-Pan Pizza and the Bloody Mary to drink."
            voice"audio/Cheddar_1_9.mp3"
            cdr "Okay!{w=0.25} Your food will be ready shortly!"
    voice "audio/Boo_1_22.mp3"    
    b "Thank you!"
    voice "audio/Boo_1_22_2.mp3"    
    #invisable version 
    "[player_name]" "Phew… Close call."

    scene black with dissolve

    voice "audio/Lupin_1_1.mp3"
    "????" "Heya,{w=0.25} mind if I sit here?"
    
    voice "audio/Lophii_1_1.mp3"
    "???" "Room for one more?"

    scene bg tabletalk with fade

    
    
    #Make a tag: to have the game load here
    
    "[player_name]" "{i}I guess I'll have to start making conversation.{/i}"

    menu:
        "It's time to make conversation!"
        
        "Wolf Guy":
            # check the top of the chapter 1 file for definitions
            $ talked_to_at_table = talked_to_lupin
            
            "{i}You attempt to start a conversation but static fuzz fills your mind.{/i}"  
            "Tulip" "I love your cape. {w=0.25}What's the inspiration for your outfit?"
            "??" "Oh, {w=0.25} Uh- {w=0.25} Well, my theme is \"Shadow Tuxedos\" which is based on 80s anime and a famous opera."
            "Tulip" "Are you a Sailing Crescent fan?"
            "??" "Yeah… {w=0.25}it holds a special place in my big meaty heart."
            "Tulip" "Hmmm.. {w=0.25}if it's not too intruding. {w=0.25}Are you going for a silent solitary hiding in the dark persona?"
            "??" "I don't know.{w=0.25}But I do like to sing at night."
            "Tulip" "That’s nice! {w=0.25}I like to sing in the shower..."
            "??" "That's so real. {w=0.25}The acoustics in there are great. But nothing is letting yourself go in an open space where you can see the stars..."
            "{i}You overcome your static fuzz and your mind clears{/i}"  
            "[player_name]" "What's uh-'{w=0.25}what's your name? Not your real one... {w=0.25} Unless that's the name you chose for the night."
            "[player_name]" "{i}Why am I being so awkward??{/i}"
            "Lupin" "Call me Lupin."
            "[player_name]" "Like the amime?"
            "Lupin" "Yeah. Thought I'd try it on for the night. How 'bout you? "
            menu:
                "[player_name]" "it's uhhh.."
                "Forgot":
                    "[player_name]" "um- call me Boo!"
                    "[player_name]" "Call me Boo!"
                    "Lupin" "is that your name for the night?"
                    "[player_name]" "Nah, I just forgot my own name haha."


                "Forgar":
                    "[player_name]" "uh-"
                    "{i}Oh bother, seems like you don't know weather you changed your name for the night or not. '{/i}" 
                    "{i}You attempt to look for your tag but can't find it for the life of you'{/i}"  
                    "{i}Well, the Unlife of you...{/i}"  
                    "[player_name]" "It's Boo!"
                    "Lupin" "is that your name for the night?"
                    "[player_name]" "Nah, I just forgot my own name haha." 
            "[player_name]" "{i}Wait- Did I just break some unspoken rule by asking his name??. Am I ruining the masqurade mystery??{/i}"

        "Sea Monster":
            $ talked_to_at_table = talked_to_lophii
            "{i}You attempt to start a conversation but static fuzz fills your mind.{/i}"  
            "{i}However- you overcome it.{/i}"  
            "[player_name]" "Hey- um! {w=0.25} I just wanted to say, that I love your outfit! " 
            "???" "Thank you, it represents the depths of the sea and its many layers, thrumming with life... "
            "[player_name]" "How poetic! I love that you put so much thought into it." 
            "[player_name]" "I call my outfit \“Clear Night\” which is based on a classical piece called \“Starlight Solitude\”." 
            "???" "What a lovely spin. You are a fan of music, then?"
            "[player_name]" "Yes, {w=0.25}I'm here to support my friends! They are performing!"
            "???" "I see. I am a student of the arts myself. {w=0.25}The name's Lophii by the way"
            "[player_name]" "Mine's Boo! So {w=0.25}who made your dress?"
            "Lophii" "I designed this dress myself to capture the beauty and feeling of the sea. I was born there and still think of it as home."
            "[player_name]" "Wow… {w=0.25}that is wonderful! I did an ocean cleanup once."
            "[player_name]" "{i}Wait- WHY DID I JUST SAY THAT?!{/i}"
            "[player_name]" "{i}She probably doesn't want to be reminded of all the pollution...{/i}"
            "[player_name]" "{i}Oh no she's looking... {w=0.25} I should say something!{/i}"
            "[player_name]" "I uh!-" 

    show boo normal at boo_size, boo_face_left, with dissolve:
        pos (0.5, 1.0)
        ease 0.2 pos (0.5, 0.75)
        ease 0.2 pos (0.5, 1.0)

    b "!!!"
    scene black with dissolve
    #Crowd applud Soud effect and have it go back to the 
    show bg daisy1 with fade
    "Daisy" "We hope you enjoyed our first set!"
    "Daisy" "We'll be back in 10 minutes."
    #Walking sfx
    scene bg stairs_debug with fade


    show tulip normal at tulip_size, tulip_face_left:
        pos (0.4, 1.0)
    show boo normal at boo_size, boo_face_left:
        pos (0.6, 1.0)
    with dissolve
    # this above dissolve is on a seperate line so they both fade in at the same time, instead of one after the other
    
    tul normal "Omg, You did SO good."
    b happy "Yeah!!" 
        
    # this is how you show dialog only on certain conditions. you can also use boolean operators (and, or, etc.)
    # and parenthesis to combine conditional operators
    if talked_to_at_table == talked_to_lupin:
        "{i}You take a glance at the sea monster and see a name tag{/i}"
        "{i}'Lophii'{/i}"
    elif talked_to_at_table == talked_to_lophii:
        "{i}You take a glace at the werewolf and see his name tag{/i}"
        "{i}'Lupin'{/i}"
         

    show lophii happy at left, lophii_size with dissolve:
        pos(0.3, 1.0)
    show lupin normal at left, lupin_size with dissolve:
        pos(0.4, 1.0)
 
    show daisy normal at center, daisy_size, daisy_face_left with dissolve: 


    lup normal "It's Really You! Daisy Bell in the Flesh! Hi {w=0.25}I am such a big fan of your work!! I still watch Sea Pirate Boogie (Anime Soundtrack 2000)"
    lup normal "Your work is absolutely phenomenal!"
    tul happy  "Oooo~ hello miss popular!"
    dsy normal "Haha It was nothing"
    lophii happy "I must say Miss Daisy, you''re incrediblly skilled a the violin. Which school did you attend?"
    lophii happy "Which school did you attened?"
    dsy normal "When I was alive? I got my bachlors at Yulevard School of Music but never got to finish my masters."
    lophii happy "Oh my stars...what an achievement"
    dsy normal "I gotta head back now, hope you guys enjoy the next set!"
    b "wooo!"
    tul happy "You go girl! YEAH!!"
    b "{i}Phew...{w=0.25}Saved by the bell...{/i}"

    scene black with dissolve

    show bg daisy2 with fade
    "Daisy" "And we’re back! I don't have a cool segway for this, but I think Kiwis are pretty nice! Don’t ya think?"
    
    scene black with dissolve
#The crowd cheers sfx
    "The next song begins with the next song being called Kiwis"
    "You gain a slow realization that the entire set is based off the rainbow"
    "Strawberry, Mango, Banana, Kiwi all correlate to the first four colors of the rainbow."
    "It was brilliant! {w=0.25}You begin to critically think about the next song... what could the names possibly be?"
    "You are lost deep in thought"
   
    show bg chef with fade
    "[Chef]" "Here are your dishes!"
    "[player_name]" "ACK!" 
    "[Chef]" "Oh, {w=0.25}But who has which plate…{w=0.25} Hmm…"
    "[Lupin]" "I forgot already. I don’t think I ordered anything."
    "[Tulip]" "I think I had Spaghetti and meatballs?"

#Second Minigame (Pancakes) Plays



    show bg stairs2_debug with fade

    scene black with dissolve


    if foodChoice == foodChoice_brew:
        "{i}Brew{/i}"
        show bg brew with fade

    elif foodChoice == foodChoice_cheddar:
        "{i}cheddar{/i}"
        show bg mac with fade

    elif foodChoice == foodChoice_spider:
        "{i}spider{/i}"
        show bg pizza with fade


#daisy talking
          
   
    return