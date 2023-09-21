label chapter_1:
    scene black with fade
    centered "{color=#fff}Chapter 1{/color}"

    scene bg floor

    tul normal "Hey!{w=0.25} How it goin’ girl?{w=0.25} Glad that you made it."
    
    dsy worried "Yeah,{w=0.25} we were getting worried!"
    
    b "Sorry for the wait!{w=0.25} I got lost on the way,{w=0.25} and almost dropped a piece of the map!"
    
    tul "Well,{w=0.25} good thing you solved the puzzle! {w=0.25}You made it just in time to see Daisy perform!{w=0.25} Ohhh,{w=0.25} she's going to be wonderful!"

    dsy "Speaking of that,{w=0.25} I gotta check on the boys.{w=0.25} Marrow isn’t here yet and we’re running out of time.{w=0.25} I’ll see you all later!"

    b "Alright,{w=0.25} break a leg!"

    dsy "Hello,{w=0.25} hope you’re all having a spoOOOooOOOoktacular night!{w=0.25} We're the Prime-Ribs{w=0.25} and we’ll be presenting a very fun set called Fruity Call!"

    tul "So, {w=0.25}whatcha been up to lately?"
    
    menu:
        "Tulip picks up the menu and scans for any dishes she might want to try.{w=0.25} She glances at you,{w=0.25} awaiting your reply."
        
        "Not much.":
            b "Just getting ready for the ball."
            b "I did hear a strange noise today{w=0.25} and I thought it was another exterminator on the hunt."
            
            tul "Oh no!{w=0.25} You just moved to this mansion."
           
            b "It was a false alarm,{w=0.25} just some kids in  costumes looking for a spooky place to check out."
           
            tul "I bet you decked out your place real nice for the season."
            
            b " Haha..."
        
        "A lot.":
            b "I had sooo much to do today.{w=0.25} You should see how I decorated the mansion!"
            b "It's so homey that it's sure to deter any thrill-seeking kids looking for haunted houses this season."
            b "Some of them actually came at the worst time,{w=0.25} right when I was scrambling to get ready!{w=0.25} Good thing I found these new shoes!"
            b "Oh,{w=0.25} and my blog also just reached it’s first anniversary!"
            
            tul "You should write about us after,{w=0.25} you busy bee!{w=0.25} I’m happy to see you buzzing with excitement over all the thing things you do."
            tul "But take a break sometimes.{w=0.25} Who knows,{w=0.25} you might die twice because of stress!"
            b "Haha,{w=0.25} yeah."
            "[player_name]" "{i}YOU CAN DIE TWICE??{/i}" # hard coded name so mouth doesn't move

            tul "It’s been kinda wild on my side too,{w=0.25} preparing for the holidays."
            tul "I know,{w=0.25} I know.{w=0.25} It’s still spooky season{w=0.25} but we musicians need to get ready EARLY for the biggest event of the year. "
            tul "It’s never too early to start learning new holiday jingles and to rehearse the classics!"

            b "Oooh,{w=0.25} sounds exciting!"

    cdr "Excuse me!{w=0.25} Are you two ladies ready to order?"
   
    b "O-{w=0.25}oh!{w=0.25} Yeah,{w=0.25} I’m ready!"
    "[player_name]" "{i}Oh no… {w=0.25}I didn’t even pick up the menu…{w=0.25} what do I do?!?!{/i}"

    tul "I’ll get the spaghetti and eyeballs."

    # TODO: make cheddar turn to look at boo's sprite here
    cdr "Alright,{w=0.25} and how about you?"

    b "{cps=30}Uh...{w=0.25} I'll have...{/cps}"
    "[player_name]" "{i}These all look so tasty!{w=0.25} I wish I could order them all!{w=0.25} But I still get phantom fullness when I eat too much...{/i}"

    menu:
        "Chef’s Recommendation":
            b "H-{w=0.25}Hm…{w=0.25} I don’t know what to choose exactly…{w=0.25} There’s just so many options!{w=0.25} Do you have a,{w=0.25} um…{w=0.25} favorite dish perhaps??"

            cdr " Why yes we do!{w=0.25} I highly suggest the Witches Brew.{w=0.25} with has potatoes,{w=0.25} carrots,{w=0.25} broccoli,{w=0.25} and marigolds."

            b "Ohh,{w=0.25} That sounds wonderful.{w=0.25} I’d love to have that!"

            cdr "Alrighty-o!{w=0.25} Coming right up."


        "Make something up":
            b "ummmm… {w=0.25}Can I get the…{w=0.25} Cheddar Goblin meal?"

            cdr "…"

            cdr "{i}The kids menu one?{/i}{w=0.25} The one that comes with the Mac n’cheese,{w=0.25} shark drink,{w=0.25} and ghost nuggets?"

            b "Yes."
            "[player_name]" "That's a real dish?!"

            cdr "Perfect!!"

            # add some sort of shsake to show shock here

            cdr "That’s one of my many recommendations!{w=0.25} I’ll get your food ready soon!"


        "Quickly glance at the menu":
            b "Lemme get the um-"
            
            "{i}You pick up the menu and skim through the dishes as quickly as possible,{w=0.25} not wanting to keep the others waiting.{/i}"

            cdr "Do you,{w=0.25} uh,{w=0.25} do you need more time?"

            tul "Yeah,{w=0.25} no rush Boo,{w=0.25} it’s okay!"

            "{i}But you're determined to order at once.{/i}"

            b "Nono!{w=0.25} I got it!{w=0.25} I got it!{w=0.25} I’ll get the Spider-Pan Pizza and the Bloody Mary to drink."

            cdr "Okay!{w=0.25} Your food will be ready shortly!"
    
    b "Thank you!"
    "[player_name]" "Phew… Close call."