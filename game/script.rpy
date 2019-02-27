# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define trev = Character("Trev")
define jade = Character("Jade")
define me = Character("Me")


# The game starts here.

label start:
   #scene 1
    scene black
    with fade

   # dialogue
    "Congratulations!"
    "Based on your application, you have been selected to be a summer intern at the Erstwhile House!"
    "Throughout this experience you will be given both menial and substantially significant tasks that could effect the outcome of your internship"
    "Choose wisely, as each decision could have a devastating impact on your future."
    "But more importantly, don't forget to have fun!"
    
    #scene 2
    scene bg erstwhileoutside
    with fade

    "Ah, the Erstwhile House." 
    "A sprawling white mansion filled with the country’s most powerful diplomats, influential politicians, and juiciest gossip."

    scene bg erstwhilefoyer
    with fade
    show trevor annoyed

    jade "Hey, who are you?"

    menu:
         
      "What should I say?"
      
      "I’m the new intern!":

         jump friendlyintro
      
      "What’s it to you?":

         jump rudeintro
            
      "Well, who are you?":

         jump whoareyou

label friendlyintro:
   show trevor pleasant

   jade "Oh, Morgan mentioned that you were arriving today. Nice to meet you! My name is Jade."
   jade "I wish we had time to talk but I have to run to a cabinet meeting. Actually, now that you’re here, do you mind doing me a favor?"
   jade "Trev mentioned that he needed some help in his father’s office but I can’t help and be in time for this meeting. Would you mind going in my stead?"
   
   menu:
      "What should I say?"

      "Sure, I can do that.":
         jump helpJadePos

      "You sure are needy.":
         jump helpJadeNeg

      "Whose Trevor?":
         jump whoseTrev

label helpJadePos:
   show trevor pleasant

   jade "Okay, great! Thanks so much, you’re a big help!"
   jump helpTrevor

label helpJadeNeg:
   show trevor annoyed
   jade "Well, you sure are rude. Listen, it shouldn’t take very long, please? I’ll owe you one."
   menu:
      "Fine":
         jump helpJadePos

      "I'll hold you to that":
         jump illHoldYouToThat

label illHoldYouToThat:
   show trevor default
   jade "... Sure, okay. Thanks for doing this."
   jump helpTrevor

label whoseTrev:
   show trevor flustered
   jade "Oh! I’m sorry, I guess you haven’t had a chance to go through introductions yet."
   jade "Trevor is another intern here at the Erstwhile House. He can be a little... arrogant... but don’t let it get to you."

   menu: 
      "Well what do you say? Can you help me?"

      "Sure, I can do that.":
         jump helpJadePos

      "You sure are needy.":
         jump helpJadeNeg

label rudeintro:
   show trevor annoyed

   jade "Ah, you must be the new intern. Looks like they should’ve picked someone else."
   jade "Trevor has some work for you. I think he's in one of the offices down the hall on the left."
   jump end

label whoareyou:
   show trevor flustered

   jade "Ah, where are my manners? My apologies."
   
   show trevor pleasant
   jade "I’m Jade, a fellow intern. It's nice to meet you. You must be the new intern I’ve been hearing about."
   jade "While you’re here, do you mind helping me out? I have to run to a meeting, and my intern colleague, Trevor, mentioned needing some help in one of the offices down the hall. Do you mind helping him for me?"
   menu: 
      jade "Well what do you say? Can you help me?"

      "Sure, I can do that.":
         jump helpJadePos

      "You sure are needy.":
         jump helpJadeNeg


label helpTrevor:
   scene bg vernersoffice
   with fade

   "TBD"
   jump end

label end:
    # This ends the game.
    return
