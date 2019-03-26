# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define trev = Character("Trev")
define jade = Character("Jade")
define morgan = Character("Morgan Odell")
define blair = Character("Blair Bailey")
define freda = Character("Freda Robert")
define truman = Character("Truman Pierce")
define verner = Character("Verner Matthias")
define me = Character("Me")


# The game starts here.

label start:
   #scene 1
    scene black
    with fade

   # dialogue
    "Congratulations!"
    "Based on your application, you have been selected to be a summer intern at the Erstwhile House!"
    "Throughout this experience, you will be given both menial and substantially significant tasks that could affect the outcome of your internship."
    "Choose wisely, as each decision could have a devastating impact on your future."
    "But more importantly, don't forget to have fun!"
    
    #scene 2
    scene bg erstwhileoutside
    with fade

    "Ah, the Erstwhile House." 
    "A sprawling white mansion filled with the country’s most powerful diplomats, influential politicians, and juiciest gossip."

    scene bg erstwhilefoyer
    with fade
    show jade default

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
   show jade pleasant
   jade "Oh, Morgan mentioned that you were arriving today. Nice to meet you! My name is Jade."

   show jade default
   jade "I wish we had time to talk, but I have to run to a cabinet meeting. Actually, now that you’re here, do you mind doing me a favor?"
   jade "Trev mentioned that he needed some help in his father’s office, but I can’t help and be on time for this meeting. Would you mind going in my stead?"
   
   menu:
      "What should I say?"

      "Sure, I can do that.":
         jump helpJadePos

      "You sure are needy.":
         jump helpJadeNeg

      "Who's Trevor?":
         jump whosTrev

label helpJadePos:
   show jade pleasant

   jade "Okay, great! Thanks so much, you’re a big help!"
   jump helpTrevor

label helpJadeNeg:
   show jade annoyed
   jade "Well, you sure are rude. Listen, it shouldn’t take very long, please? I’ll owe you one."
   menu:
      "Fine.":
         jump helpJadePos #TODO: maybe make this not pos?

      "I'll hold you to that.":
         jump illHoldYouToThat

label illHoldYouToThat:
   show jade annoyed
   jade "... Sure, okay. Thanks for doing this."
   jump helpTrevor

label whosTrev:
   show jade flustered
   jade "Oh! I’m sorry, I guess you haven’t had a chance to go through introductions yet."
   show jade pleasant
   jade "Trevor is another intern here at the Erstwhile House. He can be a little... arrogant... but don’t let it get to you."

   menu: 
      jade "Well what do you say? Can you help me?"

      "I can do that.":
         jump helpJadePos

      "You sure are needy.":
         jump helpJadeNeg

label rudeintro:
   show jade annoyed

   jade "Ah, you must be the new intern. Looks like they should’ve picked someone else."
   jade "One of my colleagues, Trevor, has some work for you. I think he's in one of the offices down the hall on the left. Don't keep him waiting."
   jump helpTrevor

label whoareyou:
   show jade flustered
   jade "Ah, where are my manners? My apologies."
   show jade pleasant
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

   show trevor default
   trev "I don’t recognize you. Are you the new coffee runner?"
   menu:
      "Excuse me?":
         jump coffeeRunnerNeutral
      "Pardon me, are you Trevor?":
         jump coffeeRunnerNeg
      "Fuck yeah I am.":
         jump coffeeRunnerPos
      
label coffeeRunnerNeutral:
   trev "I’ll take that as a yes. Listen, my dad needs some coffee, and I have better things to do. Can you go get coffee?"
   menu:
      "Sure!":
         jump coffeeRunPos
      "I’m not going to do your work for you":
         jump coffeeRunNeg
      "Who's your dad?":
         jump whosYourDaddy

label coffeeRunPos:
   show trevor pleasant
   trev "Great. Thanks, I gotta go to the golf course now. See ya!"
   jump backToJade

label coffeeRunNeg:
   show trevor annoyed
   trev "Well, then You’re no help to me. Go bother someone else."
   jump backToJade

label whosYourDaddy:
   trev "Ah, So you're {i}new{/i} new."
   trev "My dad is Verner Matthias, the most senior cabinet member in the Erstwhile House."
   trev "Don’t mess with him. He bites."
   menu:
      trev "Well?"
      "Sure!":
         jump coffeeRunPos
      "I’m not going to do your work for you!":
         jump coffeeRunNeg

label coffeeRunnerNeg:
   show trevor annoyed
   trev "Ugh. Yes. Why? Do you need something? If not, go get my dad some coffee. He wants me to do it, but I've got better things to do."
   menu:
      "I guess I can do that.":
         jump coffeeRunPos
      "Wow, you're an ass.":
         jump youreAnAss
      "Who's your dad?":
         jump whosYourDaddy

label youreAnAss:
   show trevor pleasant
   trev "Thanks. Now go do your job, coffee runner."
   jump backToJade

label coffeeRunnerPos:
   show trevor pleasant
   trev "Great. I need someone to go get my dad coffee. He wants me to do it, but I've got better things to do."
   menu:
      "I guess I can do that.":
         jump coffeeRunPos
      "Wow, you're an ass.":
         jump youreAnAss
      "Who's your dad?":
         jump whosYourDaddy

label backToJade:
   scene bg erstwhilefoyer
   with fade
   show jade default
   jade "You’re back! Thanks so much for doing that for me, I would’ve never made that meeting in time otherwise. How was Trevor?"
   menu:
      "He's... nice.":
         jump blatantLies
      "He's kind of an asshole.":
         jump assholeBoy

label blatantLies:
   show jade pleasant
   jade "Haha, you don’t have to sugarcoat it! Trev is notoriously difficult to get along with."
   jump end

label assholeBoy:
   jade "Yeah, he can be a little hard to handle sometimes."
   jump end

label end:
   show jade default
   jade "Well, I’m sure Morgan needs to see you now. She’s the lady in charge of the intern program. Why don’t I take you to her office?"
   jump morganEndDayOne

label morganEndDayOne:
   scene bg 



   # This ends the game.
   return
