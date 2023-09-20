label chapter_1:
    scene black with fade
    centered "{color=#fff}Chapter 1{/color}"

    scene bg floor

    tul normal "Hey!{w=0.25} How it goin’ girl?{w=0.25} Glad that you made it."
    
    dsy worried "Yeah,{w=0.25} we were getting worried!"
    
    b "Sorry for the wait!{w=0.25} I got lost on the way,{w=0.25} and almost dropped a piece of the map!"
    
    tul "Well,{w=0.25} good thing you solved the puzzle! {w=0.25}You made it just in time to see Daisy perform!{w=0.25} Ohhh,{w=0.25} she's going to be wonderful!"

    dsy "Speaking of that,{w=0.25} I gotta check on the boys.{w=0.25} Marrow isn’t here yet and we’re running out of time.{w=0.25} I’ll see you all later!"

    b "Alright, break a leg!"

    dsy "Hello, hope you’re all having a spoOOOooOOOoktacular night! We're the Prime-Ribs and we’ll be presenting a very fun set called Fruity Call!"

    tul "So, whatcha been up to lately?"
    
    menu:
        "Tulip picks up the menu and scans for any dishes she might want to try. She glances at you, awaiting your reply."
        
        "Not much.":
            b "Just getting ready for the ball."
            b "I did hear a strange noise today and I thought it was another exterminator on the hunt."
            
            tul "Oh no! You just moved to this mansion."
           
            b "It was a false alarm, just some kids in  costumes looking for a spooky place to check out."
           
            tul "I bet you decked out your place real nice for the season."
            
            b " Haha..."
        "A lot.":
            b "I had sooo much to do today. You should see how I decorated the mansion!"
            b "It's so homey that it's sure to deter any thrill-seeking kids looking for haunted houses this season."
            b "Some of them actually came at the worst time, right when I was scrambling to get ready! Good thing I found these new shoes!"
            b "Oh, and my blog also just reached it’s first anniversary!"
            
            tul "You should write about us after, you busy bee! I’m happy to see you buzzing with excitement over all the thing things you do."
            tul "But take a break sometimes. Who knows, you might die twice because of stress!"
            b "Haha, yeah"
            "[player_name]" "{i}YOU CAN DIE TWICE??{/i}" # hard coded name so mouth doesn't move

            tul "It’s been kinda wild on my side too, preparing for the holidays."
            tul "I know, I know. It’s still spooky season but we musicians need to get ready EARLY for the biggest event of the year. "
            tul "It’s never too early to start learning new holiday jingles And to rehearse the classics!"

            b "Oooh, sounds exciting!"

    cdr "Excuse me! Are you two ladies ready to order?"
   
    b "O-oh! Yeah, I’m ready!"
    "[player_name]" "{i}Oh no… I didn’t even pick up the menu… what do I do?!?!{/i}"

    tul "I’ll get the spaghetti and eyeballs."

    # TODO: make cheddar turn to look at boo's sprite here
    cdr "Alright, and how about you?"

    b "Uh... I'll have..."
    "[player_name]" "{i}These all look so tasty! I wish I could order them all! But I still get phantom fullness when I eat too much...{/i}"

    menu:
        "Chef’s Recommendation":
            b "H-Hm… I don’t know what to choose exactly… There’s just so many options! Do you have a, um… favorite dish perhaps??"

            cdr " Why yes we do! I highly suggest the Witches Brew. with has potatoes, carrots, broccoli, and marigolds."

            b "Ohh, That sounds wonderful. I’d love to have that!"

            cdr "Alrighty-o! Coming right up."


        "Make something up":
            b "ummmm… Can I get the… Cheddar Goblin meal?"

            cdr "…"

            cdr "The kids menu one? The one that comes with the Mac n’cheese, shark drink, and ghost nuggets?"

            b "Yes."
            "[player_name]" "That's a real dish?!"

            cdr "Perfect!!"

            # add some sort of shsake to show shock here

            cdr "That’s one of my many recommendations! I’ll get your food ready soon!"


        "Quickly glance at the menu":
            b "Lemme get the um-"
            
            "{i}You pick up the menu and skim through the dishes as quickly as possible, not wanting to keep the others waiting.{/i}"

            cdr "Do you, uh, do you need more time?"

            tul "Yeah, no rush Boo, it’s okay!"

            "{i}But you're determined to order at once.{/i}"

            b "Nono! I got it! I got it! I’ll get the Spider-Pan Pizza and the Bloody Mary to drink."

            cdr "Okay! Your food will be ready shortly!"
    
    b "Thank you!"
    "[player_name]" "Phew… Close call."