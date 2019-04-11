# The script of the game goes in this file.

#Characters
define trev = Character("Trev")
define jade = Character("Jade")
define morgan = Character("Morgan Odell")
define blair = Character("Blair Bailey")
define freda = Character("Freda Robert")
define truman = Character("Truman Pierce")
define verner = Character("Verner Matthias")
define me = Character("[povname]")

define day = 1
define completedTasks = False

#Scores
define morganScore = 0
define vernerScore = 0
define fredaScore = 0
define trumanScore = 0
define blairScore = 0
define trevorScore = 0

#Visited
define visitedBlair = False
define visitedFreda = False
define visitedTruman = False
define visitedVerner = False

#Rejected
define rejectedBlair = False
define rejectedFreda = False
define rejectedTruman = False
define rejectedVerner = False

#Freda/Truman Romance Flags
define trumanFredaRomance = 0
define trumanNote = False

label start:
    scene black
    with fade

   # LETTER Opening Scene
    "Congratulations!"
    "Based on your application, you have been selected to be a summer intern at the Erstwhile House!"
    "Throughout this experience, you will be given both menial and substantially significant tasks that could affect the outcome of your internship."
    "Choose wisely, as each decision could have a devastating impact on your future."
    "But more importantly, don't forget to have fun!"
    
    #Internal Monologue
    scene bg erstwhileoutside
    with fade

    "Ah, the Erstwhile House." 
    "A sprawling mansion filled with the country’s most powerful diplomats, influential politicians, and juiciest gossip."

   #Introduction of Jade
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

#DAY 1 Trevor
label helpTrevor:
   scene bg vernersoffice
   with fade

   show trevor default
   trev "I don’t recognize you. Are you the new coffee runner?"
   menu:
      trev "I don’t recognize you. Are you the new coffee runner?"
      "Excuse me?":
         jump coffeeRunnerNeutral
      "Pardon me, are you Trevor?":
         jump coffeeRunnerNeg
      "Fuck yeah I am.":
         jump coffeeRunnerPos
      
label coffeeRunnerNeutral:
   trev "I’ll take that as a yes. Listen, my dad needs some coffee, and I have better things to do. Can you go get coffee?"
   menu:
      trev "Can you go get coffee?"
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
      trev "Go get my dad some coffee. He wants me to do it, but I've got better things to do."
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
      trev "I need someone to go get my dad coffee. He wants me to do it, but I've got better things to do."
      "I guess I can do that.":
         jump coffeeRunPos
      "Wow, you're an ass.":
         jump youreAnAss
      "Who's your dad?":
         jump whosYourDaddy

#Day 1 Back to Jade
label backToJade:
   scene bg erstwhilefoyer
   with fade
   show jade default
   jade "You’re back! Thanks so much for doing that for me, I would’ve never made that meeting in time otherwise. How was Trevor?"
   menu:
      jade "How was Trevor?"
      "He's... nice.":
         jump blatantLies
      "He's kind of an asshole.":
         jump assholeBoy

label blatantLies:
   show jade pleasant
   jade "Haha, you don’t have to sugarcoat it! Trev is notoriously difficult to get along with."
   jump jadeFinalDayOne

label assholeBoy:
   jade "Yeah, he can be a little hard to handle sometimes."
   jump jadeFinalDayOne

label jadeFinalDayOne:
   show jade default
   jade "Well, I’m sure Morgan needs to see you now. She’s the lady in charge of the intern program. Why don’t I take you to her office?"
   jump morganEndDayOne

#Day 1 Morgan End
label morganEndDayOne:
   scene bg morganoffice
   with fade
   show morgan default
   morgan "Ah, there you are. Thought you had gotten lost. You’re late. This behavior won’t be tolerated in the future."
   show jade default
   jade "It’s not their fault, Mrs. Odell. Trevor and I needed help to cover a task because I got pulled into a meeting. If anyone is to blame, it’s me."
   morgan "Hmmph. Well, be more cognizant of your deadlines in the future, the both of you. The Erstwhile House would fall apart if everyone did not stick to the rules."
   morgan "Thank you for bringing them to me, Jade. You’re dismissed."
   jade "I’ll see you around."
   hide jade default
   morgan "Alright, let’s get some paperwork out of the way."

   python:
    povname = renpy.input("Your name is...")
    povname = povname.strip()

    if not povname:
         povname = "Alex"

   me "My name is [povname]."
   morgan "Alright [povname], let me give you a run down on how your internship is going to work."
   jump dutiesExplanation

label dutiesExplanation:
   morgan "You’ll be spending the next few weeks getting to know how the government is operated here at the Erstwhile House, the home of democracy for our great nation."
   morgan "Here, cabinet members in charge of the state, defense, justice, and treasury advise our Prime Minister Petrone on any topics that he needs counseling in."
   morgan "Every morning, you will report to me in my office to receive your tasks for the day. You will do whatever the cabinet members wish, or, in special circumstances, Prime Minister Petrone himself."
   morgan "Failure to complete your tasks will result in a poor performance review, and possible removal from your internship duties."
   morgan "I receive feedback of your work from the cabinet members on the regular, so don’t even think about shirking your work, got it?"
   menu:
      "I understand.":
         jump iUnderstand
      "What constitutes poor performance?":
         jump poorPerformanceExplanation

label iUnderstand:
   morgan "Good. Now, it looks like you have already met your fellow intern colleagues, so I’ll give you a tour of the offices that you will help service."
   scene bg blairoffice
   with fade
   show morgan default
   morgan "This is Blair Bailey’s office. She is the Secretary of State, and one of Prime Minister Petrone’s top advisers."
   scene bg fredaoffice
   with fade
   show morgan default
   morgan "This is Freda Robert’s desk. She’s been in charge of the Treasury Department for longer than anyone in this House."
   morgan "She has a soft spot for interns, however, so use that to your advantage, if you can."
   scene bg trumanoffice
   with fade
   show morgan default
   morgan "Truman Pierce works here. In charge of all things defense, Truman knows his way around the political system."
   morgan "He’s an older gentleman, close to retirement I believe."
   scene bg vernersoffice
   with fade
   show morgan default
   morgan "Verner Matthias is the last cabinet member in your jurisdiction for the internship. He is one of Prime Minister Petrone's most trusted advisors. Keep to his good side."
   scene bg erstwhilefoyer
   with fade
   show morgan default
   morgan "And that’s all the offices that you will be responsible for. Since this is just your orientation day, we will stop here for now. I expect to see you bright and early tomorrow morning."
   morgan "Don’t be late again."
   me "Yes ma’am!"
   jump endDay

label poorPerformanceExplanation:
   morgan "Well, failure to complete tasks for one. We would not have selected you as an intern if we did not believe you were capable of performing, so I expect you will not disappoint."
   morgan "Also, as you will probably learn, the Erstwhile House is filled with people with distinct.... personalities. I would advise that you watch the words you use with your superiors, as what one might find funny, another might find offensive. Use your best judgement."
   morgan "Now, do you understand you duties?"
   menu:
      "I understand.":
         jump iUnderstand
      "Could you go over it again?":
         jump dutiesExplanation

#DAY 2 START
label startDayTwo:
   scene bg morganoffice
   with fade
   show morgan default
   morgan "Good morning, [povname]. I expect you are well."
   morgan "Here are you tasks for the day..."
   morgan "It seems like Verner Matthias wants to meet with you. He's taking a special interest in this year's intern class, since his son has joined the ranks."
   morgan "And it seems that Freda Robert has asked for some assistance for today as well."
   morgan "Good luck today."
   hide morgan default
   me "Ok, it looks like today I have to check on Verner and Freda."
   menu:
      me "Where should I go first?"     
      "Help Truman":
         jump trumanDayTwo
      "Help Freda":
         jump fredaDayTwo
      "Call it a day":
         jump playingHooky

label playingHooky:
   me "I think I've done enough work for today. Time to head home."
   jump endDay

#Day 2 Freda
label fredaDayTwo:
   scene bg fredaoffice
   with fade
   show freda default
   if trumanNote == False:
      freda "Oh, hello there! And who might you be?"
      menu: 
         "I’m [povname], the new intern.":
            $ fredaScore += 1
            jump freda2Pos
         "I'm [povname], the help.":
            $ fredaScore += 2
            jump freda2Funny
   else:
      jump freda2Task

label freda2Pos:  
   freda "Nice to meet you, [povname]!"
   jump freda2Task

label freda2Funny:
   freda "Ah, finally! A sense of humor!"
   jump freda2Pos

label freda2Task:
   if trumanNote == False:
      jump freda2Task_1
   else:
      freda "... What's that in your hand there?"
      menu:
         "A note for you from Truman.":
            $ fredaScore += 5
            $ trumanFredaRomance += 5
            jump freda2_giveLetter
         "Nothing you need to see.":
            freda "Oh. I see."
            jump freda2Task_1

label freda2Task_1:
   freda "I’m glad that Morgan sent you here today. I seem to have lost something... do you mind helping me look for it?"
   menu:
      "What did you lose?":
         $ fredaScore +=1
         jump freda2_1Pos
      "I guess I have some time to spare..":
         jump freda2_1Neg

label freda2_giveLetter:
   freda "Oh! Truman!"
   freda "..."
   freda "He’s so sweet..."
   freda "Ah! Sorry, I was spacing, I gotta run!"
   if visitedBlair == False:
      freda "Just in case you haven’t heard, Blair was looking for some help!"
      freda "You might wanna go help her."
   freda "Bye!"
   hide freda default
   me "Hmmm... that was strange..."
   visitedFreda = True
   jump day2Toggle

label freda2_1Neg:
   freda "Perfect! Go check over in that corner.. I could’ve sworn they were around here somewhere..."
   menu:
      me "What does this lady want???"
      "-Pick up paper clip-":
         jump freda2_silly
      "-Pick up stapler-":
         jump freda2_silly

label freda2_silly:
   freda "Oh! I didn’t even tell you what I’m looking for! My glasses, I can’t find my glasses!"
   freda "Oh wait! That’s right! I think they’re in Blair’s office, can you go get them for me? "
   menu:
      "I have some things to do around here...":
         $ fredaScore -= 1
         jump freda2_reject
      "Will do":
         $ fredaScore += 1
         jump freda2_4Pos
      "I guess...":
         jump freda2_4Pos

label freda2_reject:
   freda "Oh...Uhm. I guess I’ll try looking for them myself.
   freda "Go on then. Blair Bailey was looking for you by the way..."
   rejectedFreda = True
   visitedFreda = True
   hide freda default
   jump day2Toggle

label freda2_1Pos:
   freda "Oh well, let me think." 
   freda "..."
   freda "I had them on this morning when I went and got my first coffee..."
   freda "And then my second..."
   freda "...."
   freda "... And then my third....."
   freda "...."
   menu:
      me "This lady drinks a lot of caffeine!"
      "That’s... a lot of coffee.":
         $ fredaScore += 1
         jump freda2_2Pos
      "What does this have to do with your lost glasses?":
         jump freda2_2Funny

label freda2_2Pos:
   freda "When you get to be my age, you do what you gotta do to stay alert."
   jump freda2_3Neutral

label freda2_2Funny:
   freda "I’m retracing my lost steps! Don’t act like you’ve never lost anything before."
   jump freda2_3Neutral

label freda2_3Neutral:
   freda "Oh yeah! I think I remember now! I think I left my glasses in Blair’s office! Do you mind going to grab them?"
   $ visitedFreda = True
   menu:
      freda "I think I left my glasses in Blair’s office! Do you mind going to grab them?" 
      "Of course!" if visitedBlair == False:
         $ fredaScore += 1
         jump freda2_4Pos
      "Sure." if visitedBlair == False:
         jump freda2_4Pos
      "Actually, I have them right here." if visitedBlair == False:
         $ fredaScore += 5
         jump freda2_completeTask

label freda2_completeTask:
   freda "You do? Well thank you so much for grabbing those for me, [povname]!"
   freda "You've been a big help. I'll let Morgan know about your progress."
   hide freda default
   visitedFreda = True
   jump day2Toggle

label freda2_4Pos:
   freda "Thank you so much, [povname]!"
   hide freda default
   visitedFreda = True
   jump blairDayTwo

label day2Toggle:
   menu:
      me "Ok, where should I go next?" 
      "Help Freda" if visitedFreda == False:
         jump fredaDayTwo
      "Help Truman" if visitedTruman == False:
         jump trumanDayTwo
      "Help Blair" if visitedBlair == False:
         jump blairDayTwo
      "Call it a day":
         jump playingHooky

#Day 2 Truman
label trumanDayTwo:
   scene bg trumanoffice
   with fade
   show truman default
   truman "Oh, hello there! And who might you be?"
   menu:
      "I’m [povname], the new intern.":
         $ trumanScore += 1
         jump truman2_pos
      "[povname]. Don't you know who I am?":
         $ trumanScore -= 1
         jump truman2_neg

label truman2_pos:
   truman "Well it's nice to meet you, [povname]. Listen, I need some of my files organized alphabetically, do you mind helping me?"
   menu:
      me "Truman asked me to help him organize his files... what should I say?"
      "Absolutely, where do we start?":
         $ trumanScore += 1
         jump truman2_acceptTask
      "Sure":
         jump truman2_acceptTask
      "Why would I help you?":
         $ trumanScore -= 3
         jump truman2_negTask
      
label truman2_acceptTask:
   if trumanScore >= 2:
      truman "That's the spirit! I like you, [povname]."
      truman "You remind me of Freda..."
      jump truman2_freda
   truman "Let's that stack over there. When you finish with that, can you go see Blair in her office? She was asking for an intern's help for today."
   menu:
      "Sounds good":
         $ trumanScore += 1
         jump trumanToBlair
      "If I have to":
         $ trumanScore -= 1
         jump trumanToBlair

label truman2_freda:
   menu:
      me "What does Freda have to do with this?"
      "It's no problem, sir!":
         jump truman2_np
      "Freda?":
         $ trumanScore += 1
         jump truman2_freda1

label truman2_np:
   truman "When you finish, don’t forget to stop by Blair’s office, thanks again!"
   jump trumanToBlair

label truman2_freda1:
   truman "Oh yes..Freda..."
   truman "{i}So cute...{/i}"
   truman "Do you mind running by her office and giving her this note?"
   menu:
      me "Truman wants me to deliver a note to Freda for him?"
      "You can count on me!":
         $ trumanScore += 1
         jump truman2_acceptFredaQuest
      "Um, I'd rather not get involved...":
         $ trumanScore -= 1
         jump truman2_rejectFredaQuest

label truman2_rejectFredaQuest:
   truman "Oh...ok"
   truman "Well...go see Blair once you finish up."
   jump trumanToBlair

label truman2_acceptFredaQuest:
   truman "Thank you so much, [povname]."
   visitedTruman = True
   jump fredaDayTwo

label trumanToBlair:
   scene black
   with fade
   me "I finish up helping Blair with his organization, then head to Blair Bailey's office."
   visitedTruman = True
   jump blairDayTwo

label truman2_negTask:
   truman "Sorry? Are you giving me attitude?"
   menu: 
      "Maybe.":
         $ trumanScore -= 5
         jump truman2_rejectTask
      "... No sir":
         jump truman2_recovery

label truman2_rejectTask:
   truman "How dare you! I don’t need you anymore. Go to Blair’s office right this minute. "
   truman "I’ll remember this." 
   visitedTruman = True
   rejectedTruman = True
   jump blairDayTwo

label truman2_recovery:
   truman "That's what I thought. Now go finish organizing those files, {i}please.{/i}"
   truman "Once you’re done with that, go see Blair."
   jump trumanToBlair

label truman2_neg:
   truman "Ah... they always seem to find the cheeky ones."
   jump truman2_pos


#Day 2 Blair
label blairDayTwo:
   scene bg blairoffice
   with fade
   show blair default
   blair "There you are! I’ve been waiting for you, listen. I need some coffee. Can you go grab some for me?"
   menu:
      me "Blair wants me to grab her some coffee... what should I say?"
      "Ok! Right away.":
         $ blairScore += 1
         jump blair2_accept
      "What? No. Why does everyone think I’m the errand runner around here.":
         $ blairScore -= 1
         jump blair2_reject
      "Uh, I guess...":
         jump blair2_accept

label blair2_accept:
   blair "Well hop to it!"
   blair2_runInWithMorgan

label blair2_reject:
   blair "Well..you are the intern, so if you want to keep this internship, you better do as you're told."
   menu:
      "Fine.":
         jump blair2_reject1
      "Whatever":
         $ blairScore -= 1
         jump blair2_reject1

label blair2_reject1:
   blair "Well, return to me quickly, [povname]."
   jump blair2_runInWithMorgan

label blair2_runInWithMorgan:
   scene bg erstwhilefoyer
   with fade
   show morgan default
   menu:
      morgan "And where are you off to? Did you finish your tasks?"
      "I’m on my way to get coffee for Blair.":
         $ morganScore += 1
         jump blair2_morganPos
      "I still need to help one last person...":
         jump blair2_morganNeu
      "Lay off, I'm working.":
         $ morganScore -= 1
         jump blair2_morganNeg

label blair2_morganPos:
   morgan "Ah, good. Well, move along then, I see you are doing well as an intern so far."
   jump blair2_coffee

label blair2_morganNeu:
   morgan "Well, what are you standing around for?"
   morgan "I’m watching you, [povname]."
   jump blair2_coffee

label blair2_morganNeg:
   morgan "Excuse me? I’ll be making a note of this."
   morgan "You better continue doing whatever you were in the middle of doing before I fire you on the spot. "
   morgan "Shoo!"
   jump blair2_coffee

label blair2_coffee:
   scene black
   with fade
   me "I finished grabbing a cup of mediocre coffee from the break room, and returned to Blair's office."
   jump blair2_end

label blair2_end:
   scene bc blairoffice
   with fade
   show blair default
   blair "AH! There you are. What took you so long?"
   menu:
      "I got sidetracked.":
         $ blairScore -= 1
         jump blair2_sidetracked
      "Here's your coffee.":
         $ blairScore += 1
         jump blair2_giveCoffee
      
label blair2_sidetracked:
   blair "Actually, I don’t care."
   jump blair2_endend

label blair2_giveCoffee:
   blair "Hmph."
   jump blair2_endend
   
label blair2_endend:
   blair "Thank you for the coffee. You may leave me now."
   visitedBlair = True
   jump morgan2

label morgan2: 
   scene bg morganoffice
   with fade
   show morgan default
   morgan "Ah, there you are. I hope you have completed all of your tasks for the day?"
   menu:
      "Psh, no.":
         $ morganScore -= 1
         jump morgan2_neg
      "Of course I have!":
         $ morganScore += 1
         jump morgan2_pos
      "Yeah":
         jump morgan2_neutral

label morgan2_neutral:
   morgan "Well...good then."
   morgan "I hope you keep it up! Well, I have nothing left for you today, you may leave."
   jump endDay

label morgan2_pos:
   morgan "Good! I’m very pleased with your enthusiasm and hard work. Keep it up!"
   jump endDay

label morgan2_neg:
   morgan "Hmph. Interesting. I’ll be taking note of that."
   morgan "It would serve you well to remember why you're here."
   jump endDay


#DAY THREE START
label startDayThree:
   scene bg morganoffice
   with fade
   show morgan default
   if morganScore <= -10:
      morgan "Good morning, [povname]."
      morgan "I got some alarming reports from yesterday that you did not complete your assignments. This is highly disappointing. We all expected better of you."
      morgan "Do not make the same mistake today."
      morgan "Here are you tasks..."
      morgan "It looks like Verner Matthias needs an extra hand. Go by his office today and see what he needs."
      morgan "Good luck."
   else:
      morgan "Good morning, [povname]. I expect you are well."
      morgan "Here are you tasks for the day..."
      morgan "It looks like Verner Matthias needs an extra hand. Go by his office today and see what he needs."
      morgan "Good luck."
   hide morgan default
   jump day3Toggle

#Day 3 Verner
label vernerDayThree:
   scene bg vernersoffice
   with fade
   show verner default
   verner "So, you’re the newest intern. I’m Verner Matthias, as I'm sure you know. You may be new here, but work here is difficult, so don’t slack off."
   verner "I don’t tolerate foolishness. There is enough of that in this office."
   menu:
      "Yes, sir.":
         $ vernerScore += 1
         jump verner3Pos
      "…":
         jump verner3Pos
      "You’re kind of grouchy.":
         $ vernerScore -= 1
         jump verner3Neg

label verner3Pos:
   verner "Good. I have high expectations from you. Do not disappoint me too."
   jump verner3Neutral

label verner3Neg:
   verner "Grouchy? There is no time to be fooling around in a place like this. You are working for some of the most powerful people in this country. It would be best for you to remember that."
   jump verner3Neutral

label verner3Neutral:
   verner "Any questions?"
   menu:
      "What do you know about Truman Pierce?":
         jump verner3LearnAboutTruman
      "I want to learn about your colleague, Blair Bailey.":
         jump verner3LearnAboutBlair
      "Can you tell me about Freda Robert?":
         jump verner3LearnAboutFreda
      "So what's with with Trevor?":
         $ vernerScore -= 1
         jump verner3LearnAboutTrevor
      "I have to go.":
         jump verner3End

label verner3LearnAboutTruman:
   verner "Truman? He’s a quiet man, doesn’t speak much. As long as he continues to do his work, I don’t particularly care about what he does."
   verner "Though I wish he kept his personal life away from his work life..."
   jump verner3Neutral

label verner3LearnAboutBlair:
   verner "Blair? She is an ambitious cabinet member and is very outspoken about her beliefs. She is efficient in her work, but there is something suspicious about her..."
   jump verner3Neutral

label verner3LearnAboutFreda:
   verner "Freda? She’s been a long time cabinet member. Her work isn’t bad, but her private life is too involved with her work..."
   jump verner3Neutral

label verner3LearnAboutTrevor:
   verner "Trevor? Do not ask about him again, but if you must know, that fool is my son, unfortunately. I’m hoping being in Erstwhile House will straighten him out."
   verner "Do not become like him."
   jump verner3Neutral

label verner3End:
   verner "I expect only the best. Do not disappoint me."
   $ visitedVerner = True
   hide verner default
   jump day3Toggle

#Day 3 Freda
label fredaDayThree:
   scene bg fredaoffice
   with fade
   show freda default
   visitedFreda = True
   "IN PROGRESS"

label day3Toggle:
   menu:
      me "Ok, it looks like today I have to check on Verner and Freda."     
      "Help Verner" if visitedVerner == False:
         jump vernerDayThree
      "Help Freda"if visitedFreda == False:
         jump fredaDayThree
      "Call it a day":
         jump playingHooky

#DAY FOUR START
label startDayFour: 
   scene bg morganoffice
   with fade
   show morgan default
   if morganScore <= -20:
      morgan "... [povname]."
      morgan "I got some alarming reports from yesterday that you did not complete your assignments. This has been the second day in a row that you have performed poorly."
      morgan "This internship is highly competetive, and if you cannot keep up this early in the program, then this may not be the best fit for for you."
      morgan "I think it may be best to pack up your things and go home."
      morgan "I expect you to be off the premises by mid-morning."
      jump badEnding
   else:
      morgan "Good morning, [povname]. I expect you are well."
      morgan "Here are your tasks for the day..."
      morgan "It looks like Verner Matthias needs an extra hand. Go by his office today and see what he needs."
      morgan "Good luck."
      hide morgan default
      jump dayFourToggle

label dayFourToggle:
   menu:
      me "Ok, where should I go next?" 
      "Help Verner" if visitedVerner == False:
         jump vernerDayFour
      "Call it a day":
         jump playingHooky

#Day 4 Verner
label vernerDayFour:
   scene bg vernersoffice
   with fade
   show verner default
   verner "Here to assist? Glad to see someone taking their job seriously. I have an abundance of work to do and will need all the assistance I can get."
   menu:
      "How long have you been a cabinet member?":
         $ vernerScore += 1
         jump verner4_cabinetMember
      "What can I assist you on?":
         $ vernerScore += 1
         jump verner4_Pos
      "Why are you so busy?":
         $ vernerScore -= 1
         jump verner4_busy

label verner4_cabinetMember:
   verner "...Many years now."
   verner "I did not always involve myself in politics, but ever since. . ."
   verner ". . ."
   verner "Let’s get back to work."
   jump verner4_Pos

label verner4_Pos:
   verner "The midterm election is a few months away. Our task is to assist Minister Petrone in his campaign for reelection. There are many events that we must plan for."
   verner "But first, we must call up our sponsors and see if they will be lending their support to us for this campaign. We need a rough estimate of how many people will be there before we can begin setting a location and date for the events."
   verner "Your job today is to call and sort through who will be attending these events. Mark them down on the list and turn them into me before the end of the day."
   jump verner4_minigame

#TODO minigame if time?
label verner4_minigame:
   scene black
   with fade
   jump verner4_end

label verner4_busy:
   verner "As you should know, elections are coming up a few months. It would do you some good to do some prior research."
   verner "Our task is to assist Minister Petrone in his campaign for reelection. There are many events that we must plan for. But first, we must call up our sponsors and see if they will be lending their support to us for this campaign."
   verner "We need a rough estimate of how many people will be there before we can begin setting a location and date for the events."
   verner "Your job today is to call and sort through who will be attending these events. Mark them down on the list and turn them into me before the end of the day."
   jump verner4_minigame

label verner4_end:
   scene bg vernersoffice
   with fade
   show verner default
   verner "Finished with the list? Thank you for the help. I’ll look these over later. You can go on ahead and assist the others."
   $ visitedVerner = True
   jump dayFourToggle

#DAY FIVE START
label startDayFour: 
   scene bg morganoffice
   with fade
   show morgan default
   if morganScore <= -20:
      morgan "... [povname]."
      morgan "I got some alarming reports from yesterday that you did not complete your assignments."
      morgan "This internship is highly competetive, and if you cannot keep up this early in the program, then this may not be the best fit for for you."
      morgan "I think it may be best to pack up your things and go home."
      morgan "I expect you to be off the premises by mid-morning."
      jump badEnding
   else:
      morgan "Good morning, [povname]. I expect you are well."
      morgan "Here are your tasks for the day..."
      morgan "It looks like Verner Matthias needs an extra hand. Go by his office today and see what he needs."
      morgan "Good luck."
      hide morgan default
      jump dayFiveToggle

label dayFiveToggle:
   menu:
      me "Ok, where should I go next?" 
      "Help Verner" if visitedVerner == False:
         jump vernerDayFour
      "Call it a day":
         jump playingHooky
   
#Day 5 Verner
label vernerDayFour:
   scene bg vernersoffice
   with fade
   show verner default
   verner "Oh [povname], you’re in the office today. I almost thought you ran off somewhere like Trevor did. That boy always dodges his responsibilities."
   menu:
      "Trevor seems like a fun guy.":
         $ vernerScore -= 1
         jump verner5_neg
      "Is there anything I can assist you with?":
         $ vernerScore += 1
         jump verner5_pos
      "I want to run off too, actually.":
         $ vernerScore -= 5
         jump verner5_veryneg
      "...":
         jump verner5_neutral

label verner5_neg:
   verner "A fun guy, you say? Your generation really only thinks about having fun. No wonder kids these days are like this."
   jump verner5_neutral

label verner5_veryneg:
   verner "Is. That. So."
   verner "Well. Unfortunate. Perhaps you should have given your internship to someone who actually wants it."
   jump verner5_neutral

label verner5_pos:
   verner "Yes...I do not like to bring in my personal life into work, but Trevor and I have our...disagreements. Often."
   verner "If you would, please speak to him about his behavior. Perhaps he would be more inclined to listen to someone his own age."
   jump verner5_options

label verner5_neutral:
   verner "Regardless. . . I do not like to bring in my personal life into work, but Trevor and I have our...disagreements. Often. If you would, please speak to him about his behavior."
   verner "Perhaps he would be more inclined to listen to someone his own age."
   jump verner5_options

label verner5_options:
   menu:
      "I will talk to him.":
         $ vernerScore += 10
         verner "...Thank you. Apologies for dragging you into personal matters. I’m sure you’ll get through to him more than I ever will."
         jump verner5_trevor
      "I don’t think I should talk to him.":
         verner "You are right, this is no place to let personal matters interfere with work. My apologies for getting you involved."
         verner "Well, back to work. I have another list of sponsors I would like you to call. Please have it finished by the end of the day."
         jump verner5_end_noTrevor
      "Aren’t you his father? Why don’t you talk to him?":
         $ vernerScore -= 5
         verner "...Yes, I suppose that is the only proper way. My apologies for getting you involved in personal matters."
         verner "Well, back to work. I have another list of sponsors I would like you to call. Please have it finished by the end of the day."
         jump verner5_end_noTrevor

label verner5_trevor:
   scene bg erstwhilefoyer
   with fade
   show trevor default
   trev "Huh? What do you want? My father sent you? How like him to cower and avoid the problem."
   menu:
      "What's up with you and your dad? Why are you fighting?":
         $ trevorScore += 1
         trev "We’re not fighting. It's always been like this."
         jump verner5_trevor_sad
      "You shouldn’t fight. Isn’t he your father":
         trev "...The people you fight with the most will always be your family."
         jump verner5_trevor_sad
      "You need to get it together.":
         $ trevorScore -= 1
         trev "What do you know about us..."
         jump verner5_trevor_sad

label verner5_trevor_sad:
   show trevor flustered
   trev "Ever since mother died, father threw himself into this political career. Everything was so much happier back then. Now we just argue over stupid things... It wasn't my choice to be interning here, honestly."
   trev "I'd rather give it to someone who actually wants to be here. My father forcefully put me here, hoping I would “straighten out.”"
   trev "I know it's really because I'm a lot like mother, and he doesn't want to be reminded of her, and so he wants me to be more like him."
   menu:
      me "Could Trevor possibly... be not that bad??"
      "I'm sorry.":
         $ trevorScore += 1
         $ vernerScore += 1
         trev "There's nothing for you to be sorry for. This is just how things turned out to be. I'd be sorry for a lot of things if I could control the things that happen."
         jump verner5_trevor_ask
      "You a mama's boy, huh?":
         show trevor annoyed
         $ trevorScore -= 1
         trev "... If you're here to make fun of me, leave."
         jump verner5_trevor_end
      "You have to talk to him if you want things to get better. I'm sure he means well.":
         show trevor pleasant
         $ trevorScore += 2
         $ vernerScore += 5
         trev "... I know. It's just difficult when neither of us have the words we want to say within our grasp."
         verner5_trevor_ask

label verner5_trevor_ask:
   menu:
      me "This kid needs cheering up... what do I say?"
      "What do you want to do if not politics?":
         $ trevorScore += 2
         jump verner5_trevor_fashion
      "Things will work out.": 
         trev "...I guess"
         jump verner5_trevor_end

label verner5_trevor_fashion:
   show trevor flustered
   trev "I actually... want to... Become a fashion designer... Is that weird?"
   menu:
      "That's cool!":
      show trevor pleasant
         $ trevorScore += 1
         trev "...Really?... My mother used to be one. She taught me a lot of things. Guess that's why I take after her so much."
         jump verner5_trevor_end
      "Yeah, kinda weird.":
         show trevor annoyed
         $ trevorScore -= 1
         trev "Forget it. Leave me alone."
         jump verner5_trevor_end

label verner5_trevor_end:
   show trevor default
   trev "Anyway... I’ll guess I’ll go back to the office. See you around, maybe."
   jump verner5_trevor_spoken

label verner5_trevor_spoken:
   scene bg vernersoffice
   with fade
   show verner default
   menu:
      verner "You spoke to Trevor?"
      "Yes, I think it went well.":
         $ vernerScore += 5
         verner "I see… Again, I apologize for getting personal matters involved. I suppose I shouldn’t reprimand Freda and Truman for doing the same... Well, you are dismissed for the day."
         verner "And [povname]... Thank you."
         jump endDay
      "Unfortunately":
         $ vernerScore -= 2
         verner "Ah... I guess it didn't go well."
         verner "My apologies for getting personal matters involved. You are dismissed."
         jump endDay
   
label verner5_end_noTrevor:
   scene black
   with fade
   scene bg vernersoffice
   with fade
   show verner default
   verner "Finished? Thank you. Your work is appreciated. You are free to go."
   visitedVerner = True
   endDay

label endDay:
   scene black
   with fade
   "End Day [day]."
   python:
      day = day + 1
   if day == 2:
      jump startDayTwo
   if day == 3:
      if visitedTruman == False and visitedFreda == False:
         $ morganScore -= 20
      elif visitedTruman == False or visitedFreda == False or rejectedFreda == True or rejectedTruman == True:
         $ morganScore -= 10
      call resetFlags
      jump startDayThree
   if day == 4:
      if visitedVerner == False:
         $ morganScore -= 10
      call resetFlags
      jump startDayFour
   if day == 5:
      if visitedVerner == False:
         $ morganScore -= 10
      call resetFlags
      jump end

label resetFlags:
   visitedBlair = False
   visitedFreda = False
   visitedTruman = False
   visitedVerner = False
   rejectedBlair = False
   rejectedFreda = False
   rejectedTruman = False
   rejectedVerner = False
   return

# You got firedddd
label badEnding:
   scene bg erstwhileoutside
   with fade
   "Unfortunately, you were not successful in your internship."
   "Morgan Odell reported back to your university of your failure to complete your duties. The dean of your school is not happy."
   "You decide not to pursue a career in politics anymore."
   "GAME OVER"
   jump end

# This ends the game.
label end:
   return
