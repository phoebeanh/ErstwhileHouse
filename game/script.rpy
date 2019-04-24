# The script of the game goes in this file.

#Characters
define trev = Character("Trev")
define jade = Character("Jade")
define morgan = Character("Morgan Odell")
define blair = Character("Blair Bailey")
define freda = Character("Freda Robert")
define truman = Character("Truman Pierce")
define verner = Character("Verner Matthias")
define unknown = Character("???")
define petrone = Character("Prime Minister Petrone")
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

#Freda
define fredaGlasses = False

#Freda/Truman Romance Flags
define trumanFredaRomance = 0
define trumanNote = False
define coffeeOrder = ""

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
      jade "Hey, who are you?"
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
   
   menu:
      jade "Trev mentioned that he needed some help in his father’s office, but I can’t help and be on time for this meeting. Would you mind going in my stead?"

      "Sure, I can do that.":
         jump helpJadePos

      "You sure are needy.":
         jump helpJadeNeg

      "Who's Trevor?":
         jump whosTrev

label helpJadePos:
   show jade pleasant

   jade "Okay, great! Thanks so much, you’re a big help!"
   jade "I’m hardworking but I can’t always do everything on my own."
   jump helpTrevor

label helpJadeNeg:
   show jade annoyed
   menu:
      jade "Well, you sure are rude. Listen, it shouldn’t take very long, please? I’ll owe you one."
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
      jade "Well what do you say? Can you help me out?"

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
   trev "I hate being interrupted when I’m working, especially by people I don’t know."
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
    povname = renpy.input("Your name is...", length=15, exclude="1234567890!@#$%^&*()<>")
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
   menu:
      morgan "I receive feedback of your work from the cabinet members on the regular, so don’t even think about shirking your work, got it?"

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
   morgan "She can be very aggressive, so I’d watch out for her if you ever got on her bad side."
   scene bg fredaoffice
   with fade
   show morgan default
   morgan "This is Freda Robert’s desk. She’s been in charge of the Treasury Department for longer than anyone has been employed in this House."
   morgan "She can also be a little...scatterbrained. So try to be patient with her."
   scene bg trumanoffice
   with fade
   show morgan default
   morgan "Truman Pierce works here. In charge of all things defense, Truman knows his way around the political system."
   morgan "He’s an older gentleman, close to retirement I believe."
   scene bg vernersoffice
   with fade
   show morgan default
   morgan "Verner Matthias is the last cabinet member in your jurisdiction for the internship. He is one of Prime Minister Petrone's most trusted advisors."
   morgan "He's known to be a bit prickly, so keep to his good side."
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
   menu:
      morgan "Now, do you understand you duties?"

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
   morgan "It seems like Truman Pierce and Freda Robert have asked for some assistance for today."
   morgan "In addition, Verner Matthias said he would like to speak to each of the interns on their first day. He doesn't usually show this kind of attention to interns, so I would take advantage of his expertise."
   morgan "Good luck."
   hide morgan default
   me "Ok, it looks like today I have to check on Truman, Verner and Freda."
   jump day2Toggle

#DAY END EARLY
label playingHooky:
   me "I think I've done enough work for today. Time to head home."
   jump endDay

#Day 2 Freda
label fredaDayTwo:
   scene bg fredaoffice
   with fade
   show freda noglasses
   if trumanNote == False:
      menu: 
         freda "Oh, hello there! And who might you be?"
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
      jump freda2Task_noNote
   else:
      freda "Ah, hello youngin'!"
      freda "... What's that in your hand there?"
      menu:
         "A note for you from Truman.":
            $ fredaScore += 5
            $ trumanFredaRomance += 5
            jump freda2_giveLetter
         "Nothing you need to see.":
            freda "Oh. I see."
            jump freda2_visitedBlair

label freda2Task_noNote:
   menu:
      freda "I’m glad that Morgan sent you here today. I seem to have lost something... do you mind helping me look for it? "
      "What did you lose?":
         $ fredaScore +=1
         jump freda2_1Pos
      "I guess I have some time to spare..":
         jump freda2_1Neg

label freda2_giveLetter:
   freda "Oh! Truman!"
   freda "..."
   freda "He’s so sweet..."
   freda "Ah! Sorry, I was spacing."
   if visitedBlair == False:
      freda "Just in case you haven’t heard, Blair was looking for some help!"
      freda "You might wanna go help her."
      freda "Bye!"
      hide freda noglasses
      me "Hmmm... that was strange..."
      $ visitedFreda = True
      jump blairDayTwo
   if visitedBlair == True:
      jump freda2_visitedBlair

label freda2_visitedBlair:
      freda "Oh, by the way, I need your help big time!"
      menu:
         freda "Do you see the stack over there?"
         "Yes":
            $fredaScore += 1
            jump freda2_seeStack
         "No":
            $fredaScore -= 1
            jump freda2_noSeeStack

label freda2_noSeeStack:
   freda "Well...it’s right there, not hard to see."
   menu:
      freda "Take each letter and put them in an envelope and properly address every single one."      
      "Oh my god...":
         jump freda2_stackNeu
      "I'll... do my best!":
         $fredaScore += 1
         jump freda2_stackPos
      "I don't think so!":
         $fredaScore -= 1
         jump freda2_stackNeg

label freda2_seeStack:
   menu:
      freda "Ok good, can you take all of those papers and individually put each paper into an envelope and properly address every letter?"
      "Oh my god...":
         jump freda2_stackNeu
      "I'll... do my best!":
         $fredaScore += 1
         jump freda2_stackPos
      "I don't think so!":
         $fredaScore -= 1
         jump freda2_stackNeg

label freda2_stackNeg:
   freda "Dear, I promise you this is not the worst thing you could be asked to do."
   freda "Here ya go! Have fun!"
   jump freda2_afterStack

label freda2_stackPos:
   freda "Awesome! Thank you so much [povname], come see me when you finish."
   jump freda2_afterStack

label freda2_stackNeu:
   freda "It’s not too bad, go on now. When you finish, come tell me."
   jump freda2_afterStack

label freda2_afterStack:
   scene black
   with fade 
   scene bg fredaoffice
   show freda default
   menu:
      freda "How'd you do?"
      "Well, that’s finally done!":
         jump freda2_afterStackPos
      "I can’t believe you made me do that":
         $ fredaScore -= 1
         jump freda2_afterStackNeg

label freda2_afterStackNeg:
   freda "It wasn’t that bad. C’mon, you’re just exaggerating."
   freda "Well, anyways, I don’t need any more help for today. Thanks for stopping by."
   $ visitedFreda = True
   jump day2Toggle

label freda2_afterStackPos:
   freda "Good! Good! Thank you so much."
   freda "Well, that's all for today from me. Thanks for stopping by, [povname]."
   $ visitedFreda = True
   jump day2Toggle

label freda2_1Neg:
   freda "Oh! I’m so forgetful. So sorry...."
   menu:
      freda "Go check over in that corner.. I could’ve sworn they were around here somewhere..."
      "-Pick up paper clip-":
         jump freda2_silly
      "-Pick up stapler-":
         jump freda2_silly

label freda2_silly:
   freda "Oh! I didn’t even tell you what I’m looking for! My glasses, I can’t find my glasses!"
   menu:
      freda "Oh wait! That’s right! I think they’re in Blair’s office, can you go get them for me? "
      "I have some things to do around here...":
         $ fredaScore -= 1
         jump freda2_reject
      "Will do":
         $ fredaScore += 1
         jump freda2_4Pos
      "I guess...":
         jump freda2_4Pos

label freda2_reject:
   freda "Oh...Uhm. I guess I’ll try looking for them myself."
   freda "Go on then. Blair Bailey was looking for you by the way..."
   $ rejectedFreda = True
   $ visitedFreda = True
   hide freda noglasses
   jump day2Toggle

label freda2_1Pos:
   freda "Oh well, let me think." 
   freda "..."
   freda "I had them this morning when I went and got my first coffee..."
   freda "And then my second..."
   freda "...."
   freda "... And then my third....."
   freda "...."
   menu:
      freda "Maybe I should go get another cup... might jog my memories..."
      "That’s a lot of coffee.":
         $ fredaScore += 1
         jump freda2_2Pos
      "What does this have to do with anything?":
         $ fredaScore -= 1
         jump freda2_2Funny

label freda2_2Pos:
   freda "When you get to be my age, you do what you gotta do to stay alert."
   jump freda2_3Neutral

label freda2_2Funny:
   freda "I’m retracing my lost steps! You young people... always in a rush.."
   jump freda2_3Neutral

label freda2_3Neutral:
   $ visitedFreda = True
   freda "Oh!"
   menu:
      freda "I think I left my glasses in Blair’s office! Do you mind going to grab them?" 
      "Of course!" if visitedBlair == False:
         $ fredaScore += 1
         jump freda2_4Pos
      "Sure." if visitedBlair == False:
         jump freda2_4Pos
      "Actually, I have them right here." if visitedBlair == True:
         $ fredaScore += 5
         freda "You do?"
         jump freda2_completeTask

label freda2_returnGlasses:
   scene bg fredaoffice
   with fade
   show freda default
   freda "Oh thank goodness you found them! I don't think my eyes could have taken much more strain."
   jump freda2_completeTask

label freda2_completeTask:
   hide freda noglasses
   show freda default
   freda "Well thank you so much for grabbing those for me, [povname]!"
   freda "You've been a big help. I'll let Morgan know about your progress."
   hide freda default
   $ visitedFreda = True
   jump day2Toggle

label freda2_4Pos:
   freda "Thank you so much, [povname]!"
   $ visitedFreda = True
   jump blairDayTwo

#DAY 2 TOGGLE
label day2Toggle:
   menu:
      me "Ok, where should I go next?" 
      "Help Freda" if fredaGlasses == False or visitedFreda == False:
         jump fredaDayTwo
      "Help Truman" if visitedTruman == False:
         jump trumanDayTwo
      "Visit Verner" if visitedVerner == False:
         jump vernerDayTwo
      "Call it a day":
         jump morgan2

#Day 2 Truman
label trumanDayTwo:
   scene bg trumanoffice
   with fade
   show truman default
   menu:
      truman "Oh, hello there! And who might you be?"
      "I’m [povname], the new intern.":
         $ trumanScore += 1
         jump truman2_pos
      "[povname]. Don't you know who I am?":
         $ trumanScore -= 1
         jump truman2_neg

label truman2_pos:
   truman "Well it's nice to meet you, [povname]. Listen, I need some of my files organized alphabetically, do you mind helping me?"
   truman "I like to keep my space very organized. I need structure."
   menu:
      truman "So will you help me organize my files?"
      "Absolutely, where do we start?":
         $ trumanScore += 1
         jump truman2_acceptTask
      "Sure":
         jump truman2_acceptTask
      "Why would I help you?":
         $ trumanScore -= 3
         jump truman2_negTask
      
label truman2_acceptTask:
   if trumanScore >= 1:
      truman "That's the spirit! I like you, [povname]."
      jump truman2_freda
   truman "Let's that stack over there..."
   if visitedBlair == False: 
      menu:
         truman "When you finish with that, can you go see Blair in her office? She was asking for an intern's help for today."
         "Sounds good":
            $ trumanScore += 1
            jump trumanToBlair
         "If I have to":
            $ trumanScore -= 1
            jump trumanToBlair
   if visitedBlair == True:
      jump truman2_afterStack

label truman2_afterStack:
   scene black
   with fade 
   scene bg trumanoffice
   show truman default
   menu:
      truman "How'd you do?"
      "Well, that’s finally done!":
         jump truman2_afterStackPos
      "I can’t believe you made me do that":
         $ fredaScore -= 1
         jump truman2_afterStackNeg

label truman2_afterStackNeg:
   truman "It wasn’t that bad. C’mon, you’re just exaggerating."
   truman "Well, anyways, I don’t need any more help for today. Thanks for stopping by."
   $ visitedTruman = True
   jump day2Toggle

label truman2_afterStackPos:
   truman "Good! Good! Thank you so much."
   truman "Well, that's all for today from me. Thanks for stopping by, [povname]."
   $ visitedTruman = True
   jump day2Toggle

label truman2_freda:
   menu:
      truman "You remind me of Freda..."
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
   truman "Do you mind doing me a favor?"
   truman "I have this note I've been meaning to give to Freda, actually, and it would be a big help if you could do it for me?"
   menu:
      truman "I have this note I've been meaning to give to her, and it would be a big help if you could do it for me?"
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
   $ visitedTruman = True
   $ trumanNote = True
   jump fredaDayTwo

label trumanToBlair:
   scene black
   with fade
   me "I finish up helping Blair with his organization, then head to Blair Bailey's office."
   $ visitedTruman = True
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
   truman "How dare you! I don’t need you anymore. Go to Blair’s office right this minute."
   truman "I’ll remember this." 
   $ visitedTruman = True
   $ rejectedTruman = True
   jump blairDayTwo

label truman2_recovery:
   truman "That's what I thought. Now go finish organizing those files, {i}please.{/i}"
   truman "Once you’re done with that, go see Blair."
   jump trumanToBlair

label truman2_neg:
   truman "Ah... they always seem to find the cheeky ones."
   jump truman2_pos

#Day 2 Verner
label vernerDayTwo:
   scene bg vernersoffice
   with fade
   show verner default
   verner "So, you’re the newest intern. I’m Verner Matthias, as I'm sure you know. You may be new here, but work here is difficult, so don’t slack off."
   verner "I don’t tolerate foolishness. There is enough of that in this office."
   menu:
      verner "I don’t tolerate foolishness. There is enough of that in this office."
      "Yes, sir.":
         $ vernerScore += 1
         jump verner2Pos
      "…":
         jump verner2Pos
      "You’re kind of grouchy.":
         $ vernerScore -= 1
         jump verner2Neg

label verner2Pos:
   verner "Good. I have high expectations from you. Do not disappoint me too."
   jump verner2Neutral

label verner2Neg:
   verner "Grouchy? There is no time to be fooling around in a place like this. You are working for some of the most powerful people in this country. It would be best for you to remember that."
   jump verner2Neutral

label verner2Neutral:
   verner "However, I do want to make sure that at least some of you interns succeed."
   verner "Thus, if you have any questions about any of the people that you will be serving, I can help give you an insider's view into the Erstwhile House."
   jump verner2Neutral_choice

label verner2Neutral_choice:
   menu:
      verner "Any questions?"
      "What do you know about Truman Pierce?":
         jump verner2LearnAboutTruman
      "I want to learn about your colleague, Blair Bailey.":
         jump verner2LearnAboutBlair
      "Can you tell me about Freda Robert?":
         jump verner2LearnAboutFreda
      "So what's with with Trevor?":
         $ vernerScore -= 1
         jump verner2LearnAboutTrevor
      "I have to go.":
         jump verner2End

label verner2LearnAboutTruman:
   verner "Truman? He’s a quiet man, doesn’t speak much. As long as he continues to do his work, I don’t particularly care about what he does."
   verner "Though I wish he kept his personal life away from his work life..."
   jump verner2Neutral_choice

label verner2LearnAboutBlair:
   verner "Blair? She is an ambitious cabinet member and is very outspoken about her beliefs. She is efficient in her work, but there is something suspicious about her..."
   jump verner2Neutral_choice

label verner2LearnAboutFreda:
   verner "Freda? She’s been a long time cabinet member. Her work isn’t bad, but her private life is too involved with her work..."
   jump verner2Neutral_choice

label verner2LearnAboutTrevor:
   verner "Trevor? Do not ask about him again, but if you must know, that fool is my son, unfortunately. I’m hoping being in Erstwhile House will straighten him out."
   verner "Do not become like him."
   jump verner2Neutral_choice

label verner2End:
   verner "I expect only the best. Do not disappoint me."
   $ visitedVerner = True
   hide verner default
   jump day2Toggle

#Day 2 Blair
label blairDayTwo:
   scene bg blairoffice
   with fade
   show blair default
   blair "[povname], the new intern, right?"
   blair "Listen, my idiot assistant called in \"sick\" today, and if I don't get me a decent cup of coffee in the next five minutes I'm going to fire somebody."
   menu:
      blair "Can you go grab some for me?"
      "Ok! Right away.":
         $ blairScore += 2
         jump blair2_accept
      "What? No. Why does everyone think I’m the errand runner around here.":
         $ blairScore -= 1
         jump blair2_reject
      "Uh, I guess...":
         $ blairScore += 1
         jump blair2_accept

label blair2_accept:
   blair "Well hop to it!"
   jump blair2_runInWithMorgan

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
      "I'm almost done..":
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
   morgan "You better continue doing whatever you were in the middle of doing before I fire you on the spot."
   morgan "Shoo!"
   jump blair2_coffee

label blair2_coffee:
   scene black
   with fade
   scene bg breakroom
   me "Hmmm, there looks like there's a good selection of coffee."
   menu:
      me "What kind of coffee should I get?"
      "Mocha Macchiato":
         $ coffeeOrder = "mocha"
         me "I make the drink and head back to Blair Bailey's office."
         jump blair2_end
      "Iced latte":
         $ coffeeOrder = "iced"
         me "I make the drink and head back to Blair Bailey's office."
         jump blair2_end
      "Black coffee":
         $ coffeeOrder = "black"
         $ blairScore += 1
         me "I make the drink and head back to Blair Bailey's office."
         jump blair2_end
label blair2_end:
   scene bg blairoffice
   with fade
   show blair default
   blair "AH! There you are. What took you so long?"
   menu:
      "I got sidetracked.":
         $ blairScore -= 1
         jump blair2_sidetracked
      "Here's your coffee.":
         $ blairScore += 2
         jump blair2_giveCoffee
      
label blair2_sidetracked:
   blair "Actually, I don’t care about other people's problems. You may relinquish the coffee and go."
   jump blair2_giveCoffee

label blair2_giveCoffee:
   blair "Hmph."
   if coffeeOrder == "black":
      show blair smile
      blair "Black coffee. Finally, an intern who knows what to do without being asked. Thank you for the coffee."
   if coffeeOrder == "mocha":
      blair "A macchiato... a bit sugary for my tastes but it will do. Thank you for the coffee."
   if coffeeOrder == "iced":
      blair "An iced latte? Iced coffee is for 20-year old college girls and alcoholic suburban mothers, not a government official."
   jump blair2_endend
   
label blair2_endend:
   blair "You may leave me now."
   $ visitedBlair = True
   if fredaGlasses == False:
      blair "Oh, by the way, Freda left her glasses in here from our last staff meeting. Please get them to her at some point."
      me "{i}They seem a bit crooked...{/i}"
      $ fredaGlasses = True
      me "I better return these to Freda."
      if visitedTruman == False:
         jump freda2_returnGlasses
      if visitedTruman == True:
         jump day2Toggle
   hide blair default
   jump day2Toggle

#MORGAN END DAY 2
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
      morgan "Blair Bailey also needs a hand revising some local jurisdiction paperwork."
      morgan "Good luck."
   hide morgan default
   jump day3Toggle

#Day 3 Blair
label blairDayThree:
   scene bg blairoffice
   with fade
   show blair default
   blair "Come in [povname], good to see you again. Never sure if our interns will come back."
   blair "You know I’ve been working here long enough to know you can’t trust half the people in this building. Especially the prime minister himself."
   blair "...Don’t tell him I said that."
   blair "I do hope that I can trust you. I’ve been working with interns for awhile now and I want you to know I’m going to treat you like any other employee."
   menu:
      blair "If you do better than Verner's waste of skin son, you'll be fine."
      "Even Verner doesn't seem to be the biggest fan of Trevor":
         blair "Well I can’t be sure you’re any better until you prove yourself to me."
         jump blair3_task
      "Do you mind me asking why you don’t like Petrone?":
         $ blairScore += 5
         blair "Well, you didn't hear this from me, but I think Petrone has lost sight of what's important. For example, running this country."
         blair "Tell me, [povname], have you seen Prime Minister Petrone since you started working in this office?"
         me "Well, no--"
         blair "Exactly. A good leader should be interested in who exactly is coming in and out of the most powerful building in the country. Especially if they're to be the next generation of leaders."
         blair "I think we need to reconsider just how dedicated he is to the good of the country."
         jump blair3_petrone
      "It's nice of you to treat me like an equal":
         $ blairScore += 1
         blair "Well don’t get too comfortable. All that means is I’m expecting you to complete the same tasks and not complain about it."
         jump blair3_task

label blair3_task:
   blair "So to help you prove yourself to me im gonna start you off with a rather difficult task. Take this stamp and this stack of papers."
   blair "I need you to mark each one with the corresponding date on the ledger and stamp the ones that need revision. Do this and I might learn to trust you."
   menu:
      blair "Any questions?"
      "I understand. I’ll get it done and bring it back.":
         $ blairScore += 1
         jump blair3_afterTask
         blair "Great! Well hurry back when you’re done."
      "When should it be complete?":
         blair "Well it’s not on deadline but I would prefer to get it back as soon as possible."
         jump blair3_afterTask
      "I’ll get it done when I can.": 
         $ blairScore += 1
         blair "This should be your priority. We don’t need another Trevor. How can I trust you if you don’t take my work seriously? Get going."
         jump blair3_afterTask

define askedAboutPetrone = False

label blair3_petrone:
   $ askedAboutPetrone = True
   me "Wait, wait does that mean?"
   blair "Oh, I meant nothing by it. We should always be striving to push towards something greater, [povname]."
   blair "Anyway, I need you to mark each one with the corresponding date on the ledger and stamp the ones that need revision. Do this and I might learn to trust you."
   menu:
      blair "Any questions?"
      "I understand. I’ll get it done and bring it back.":
         $ blairScore += 1
         blair "Great! Well hurry back when you’re done."
         jump blair3_afterTask
      "When should it be complete?":
         blair "Well it’s not on deadline but I would prefer to get it back as soon as possible."
         jump blair3_afterTask
      "I’ll get it done when I can.": 
         $ blairScore += 1
         blair "This should be your priority. We don’t need another Trevor. How can I trust you if you don’t take my work seriously? Get going."
         jump blair3_afterTask

label blair3_afterTask:
   scene black with fade
   scene bg blairoffice with fade
   show blair default
   blair "Got it done? Good. Maybe there is a use for you after all. All right, well that’s all I got for you right now. So I guess you're free for now. And if I need you for anything I’ll let you know."
   if askedAboutPetrone == True:
      me "Wait! Can I ask some more about your opinion of Petrone?"
      blair "Like I said earlier, I think Petrone's fitness for leadership leaves... something to be desired. Someone with some actual grit definitely deserves the position. That’s all I will say right now."
      blair "I hope when the time comes, I trust you will follow the right leader. Well, head out for today. We'll talk later."
   $ visitedBlair = True
   hide blair default
   jump day3Toggle

#Day 3 Verner
label vernerDayThree:
   scene bg vernersoffice
   with fade
   show verner default
   verner "Here to assist? Glad to see someone taking their job seriously. I have an abundance of work to do and will need all the assistance I can get."
   menu:
      "What can I assist you on?":
         $ vernerScore += 1
         jump verner3_Pos
      "Why are you so busy?":
         $ vernerScore -= 1
         jump verner3_busy
      "How long have you been a cabinet member?":
         $ vernerScore += 1
         jump verner3_cabinetMember

label verner3_cabinetMember:
   verner "...Many years now."
   verner "I did not always involve myself in politics, but ever since. . ."
   verner ". . ."
   verner "Let’s get back to work."
   jump verner3_Pos

label verner3_Pos:
   verner "The midterm election is a few months away. Our task is to assist Minister Petrone in his campaign for reelection. There are many events that we must plan for."
   verner "But first, we must call up our sponsors and see if they will be lending their support to us for this campaign. We need a rough estimate of how many people will be there before we can begin setting a location and date for the events."
   verner "Your job today is to call and sort through who will be attending these events. Mark them down on the list and turn them into me before the end of the day."
   jump verner3_minigame

#TODO minigame if time?
label verner3_minigame:
   scene black
   with fade
   jump verner3_end

label verner3_busy:
   verner "As you should know, elections are coming up a few months. It would do you some good to do some prior research."
   verner "Our task is to assist Minister Petrone in his campaign for reelection. There are many events that we must plan for. But first, we must call up our sponsors and see if they will be lending their support to us for this campaign."
   verner "We need a rough estimate of how many people will be there before we can begin setting a location and date for the events."
   verner "Your job today is to call and sort through who will be attending these events. Mark them down on the list and turn them into me before the end of the day."
   jump verner3_minigame

label verner3_end:
   scene bg vernersoffice
   with fade
   show verner default
   verner "Finished with the list? Thank you for the help. I’ll look these over later. You can go on ahead and assist the others."
   $ visitedVerner = True
   jump day3Toggle

#Day 3 TOGGLE
label day3Toggle:
   menu:
      me "Ok, it looks like today I have to check on Verner and Freda."     
      "Help Verner" if visitedVerner == False:
         jump vernerDayThree
      "Help Blair" if visitedBlair == False:
         jump blairDayThree
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
      if askedAboutPetrone == True or blairScore > 5:
         morgan "Blair Bailey would also like to speak with you."
      morgan "Good luck."
      hide morgan default
      jump dayFourToggle

label dayFourToggle:
   menu:
      me "Ok, where should I go next?" 
      "Help Verner." if visitedVerner == False:
         jump vernerDayFour
      "See what Blair wants." if visitedBlair == False and (askedAboutPetrone == True or blairScore > 5):
         jump blairDayFour
      "Call it a day.":
         if trumanNote == False:
            jump playingHooky
         if trumanNote == True:
            jump freda4_gift

#BLAIR DAY 4
label blairDayFour:
   scene bg blairoffice with fade
   show blair smile
   blair "Hello, [povname]."
   blair "I need your help on something I've cooked up. Are you scheduled to be here tomorrow?"
   menu:
      "As I always am.":
         $ blairScore += 2
         blair "Good. Come to me bright and early tomorrow. It's important."
         me "What are we doing?"
         show blair smirk
         blair "You'll see."
      "Unfortunately.":
         $ blairScore -= 1
         blair "Don't be so morose."
         blair "Come to me bright and early tomorrow. It's important."
         me "What are we doing?"
         show blair smirk
         blair "You'll see."
   $ visitedBlair = True
   hide blair smirk
   jump dayFourToggle

#FREDA DAY 4
label freda4_gift:
   scene bg erstwhilefoyer with fade
   show freda frown
   freda "[povname]! I really would like your help if you could spare a minute?"
   menu:
      freda "[povname]! I really would like your help if you could spare a minute?"
      "Uh, what do you need help with?":
         $ fredaScore += 5
         jump freda4_acceptGift
      "Sorry, I'm busy.":
         $ fredaScore -= 5
         jump freda4_rejectGift
 
label freda4_acceptGift:
   freda "AH! Thank you. Here, this gift is for Truman, could you deliver it to him for me?"
   me "I--"
   freda "Great! Thank you so so much!"
   jump truman4

label freda4_rejectGift:
   freda "Well..alright, thanks anyways. See you around."
   jump endDay

label truman4:
   truman "Hello [povname]. Is there something you need help with?"
   menu:
      truman "I don't recall asking your assistance today.."
      "-Hand Truman the gift from Freda-":
         $ fredaScore += 5
         $ trumanScore += 5
         jump truman4_gift
      "Nope":
         truman "Oh. Well, ok then. Thanks for stopping by I suppose."
         truman "{i}Weird kid...{/i}"
         jump endDay

label truman4_gift:
   truman "Is this--- from Freda??? What a sweetheart. Thank you so much for delivering this to me!"
   truman "I appreciate you helping us. I’ll see you again soon."
   jump endDay

#Day 4 Verner
label vernerDayFour:
   scene bg vernersoffice
   with fade
   show verner default
   verner "Oh [povname], you’re in the office today. I almost thought you ran off somewhere like Trevor did. That boy always dodges his responsibilities."
   menu:
      "Trevor seems like a fun guy.":
         $ vernerScore -= 1
         jump verner4_neg
      "Is there anything I can assist you with?":
         $ vernerScore += 1
         jump verner4_pos
      "I want to run off too, actually.":
         $ vernerScore -= 5
         jump verner4_veryneg
      "...":
         jump verner4_neutral

label verner4_neg:
   verner "A fun guy, you say? Your generation really only thinks about having fun. No wonder kids these days are like this."
   jump verner4_neutral

label verner4_veryneg:
   verner "Is. That. So."
   verner "Well. Unfortunate. Perhaps you should have given your internship to someone who actually wants it."
   jump verner4_noTrevor

label verner4_pos:
   verner "Yes...I do not like to bring in my personal life into work, but Trevor and I have our...disagreements. Often."
   verner "It is unacceptable behavior for an Erstwhile House intern and certainly for my son."
   verner "If you could, please speak to him about his behavior. Perhaps he would be more inclined to listen to someone his own age."
   jump verner4_options

label verner4_neutral:
   verner "Regardless... I do not like to bring in my personal life into work, but Trevor has repeatedly disrespected my kindness to him in giving him this summer internship position."
   verner "It is unacceptable behavior for an Erstwhile House intern and certainly for my son."
   verner "If you could, please speak to him about his behavior. Perhaps he would be more inclined to listen to someone his own age."
   jump verner4_options

label verner4_noTrevor:
   verner "Get back to work. I have another list of sponsors I would like you to call. Have it finished by the end of the day or I will be having a very serious talk with Mrs. Odell about your continued employment here."
   jump verner4_end_noTrevor

label verner4_options:
   menu:
      verner "If you could, please speak to him about his behavior. Perhaps he would be more inclined to listen to someone his own age."
      "I will talk to him.":
         $ vernerScore += 10
         verner "...Thank you. Apologies for dragging you into personal matters. I’m sure you’ll get through to him more than I ever will."
         jump verner4_trevor
      "I don’t think I should talk to him.":
         verner "You are right, this is no place to let personal matters interfere with work. My apologies for getting you involved."
         verner "Well, back to work. I have another list of sponsors I would like you to call. Please have it finished by the end of the day."
         jump verner4_end_noTrevor
      "Aren’t you his father? Why don’t you talk to him?":
         $ vernerScore -= 5
         verner "...Yes, I suppose that is the only proper way. My apologies for getting you involved in personal matters."
         verner "Well, back to work. I have another list of sponsors I would like you to call. Please have it finished by the end of the day."
         jump verner4_end_noTrevor

label verner4_trevor:
   scene bg erstwhilefoyer with fade
   show trevor default
   trev "Huh? What do you want? My father sent you? How like him to cower and avoid the problem."
   menu:
      "What's up with you and your dad? Why are you fighting?":
         $ trevorScore += 1
         trev "We’re not fighting. It's always been like this."
         jump verner4_trevor_sad
      "You shouldn’t fight. Isn’t he your father?":
         trev "...The people you fight with the most will always be your family."
         jump verner4_trevor_sad
      "You need to get it together.":
         $ trevorScore -= 1
         trev "What do you know about us..."
         jump verner4_trevor_sad

label verner4_trevor_sad:
   show trevor flustered
   trev "I shouldn't be telling you all this... but whatever, he's been a complete ass lately."
   trev "Ever since mother died, father threw himself into this political career. Everything was so much happier back then. Now we just argue over stupid things... It wasn't my choice to be interning here, honestly."
   trev "I'd rather give it to someone who actually wants to be here. My father forcefully put me here, hoping I would “straighten out.”"
   trev "He wants me to be more like him, but plot twist: I'm not. If anything, I'm much more like my mom."
   menu:
      trev "He just doesn't get it..."
      "I'm sorry.":
         $ trevorScore += 1
         $ vernerScore += 1
         trev "There's nothing for you to be sorry for. This is just how things turned out to be. I'd be sorry for a lot of things if I could control the things that happen."
         jump verner4_trevor_ask
      "You a mama's boy, huh?":
         show trevor annoyed
         $ trevorScore -= 1
         trev "... If you're here to make fun of me, leave."
         jump verner4_trevor_end
      "You have to talk to him if you want things to get better. I'm sure he means well.":
         show trevor pleasant
         $ trevorScore += 2
         $ vernerScore += 5
         trev "... I know. It's just difficult when neither of us have the words we want to say within our grasp."
         jump verner4_trevor_ask

define trevorWantsToTalkToDad = False

label verner4_trevor_ask:
   menu:
      "What do you want to do if not politics?":
         $ trevorScore += 2
         jump verner4_trevor_fashion
      "Things will work out.": 
         trev "...I guess"
         jump verner4_trevor_end
      "What if I helped you talk to your dad?":
         $ trevorScore += 1
         trev "No, no... I couldn't ask you to do that. It's fine."
         show trevor default
         trev "Hey... thanks for caring. Not many people stop and talk to me. Mostly people just assume I'm an asshole."
         show trevor pleasant
         trev "Which is true."
         show trevor default
         $ trevorWantsToTalkToDad = True
         jump verner4_trevor_end

label verner4_trevor_fashion:
   show trevor flustered
   trev "I actually... want to... Become a fashion designer... Is that weird?"
   menu:
      "That's cool!":
         show trevor pleasant
         $ trevorScore += 1
         trev "...Really?... My mother used to be one. She taught me a lot of things. Guess that's why I take after her so much."
         jump verner4_trevor_end
      "Yeah, kinda weird.":
         show trevor annoyed
         $ trevorScore -= 1
         trev "Forget it. Leave me alone."
         jump verner4_trevor_end

label verner4_trevor_end:
   show trevor default
   trev "Anyway... I’ll guess I’ll go back to the office. See you around, maybe."
   jump verner4_trevor_spoken

label verner4_trevor_spoken:
   scene bg vernersoffice
   with fade
   show verner default
   $ visitedVerner = True
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
   
label verner4_end_noTrevor:
   scene black
   with fade
   scene bg vernersoffice
   with fade
   show verner default
   verner "Finished? Thank you. You are free to go."
   $ visitedVerner = True
   jump endDay

#DAY FIVE START
label startDayFive: 
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
      morgan "Freda seemed rather distraught this morning. I advise you go check on her."
      morgan "It also looks like Verner Matthias needs an extra hand. Go by his office today and see what he needs."
      morgan "Lastly, Blair has requested to see you."
      morgan "It looks like you have a busy day. Good luck."
      hide morgan default
      jump dayFiveToggle

label dayFiveToggle:
   menu:
      me "Ok, where should I go next?" 
      "Help Verner." if visitedVerner == False:
         jump vernerDayFive
      "Help Freda." if visitedFreda == False:
         jump fredaDayFive
      "Help Blair." if visitedBlair == False:
         jump blairDayFive
      "Call it a day.":
         jump playingHooky

define trevorTalk = False

#VERNER DAY 5
label vernerDayFive:
   if trevorWantsToTalkToDad == True:
      jump trevorDayFive
   scene bg vernersoffice with fade
   show verner default
   verner "Good morning, [povname]. We have a busy day today, so I expect you to get cracking!"
   menu:
    "I have a message for you. From Trevor." if trevorTalk == True:
      $ vernerScore += 5
      jump verner5_trev
    "What's on the menu today?":
      $ vernerScore += 1
      verner "Cheeky, aren't you?"
      jump verner5_pos
    "Yes sir.":
      jump verner5_pos

label verner5_trev:
   verner "He asked you to tell me something? Why couldn't he just do it himself?"
   verner "...You know what it? It doesn't matter. What did he want me to know?"
   menu:
      verner "...You know what it? It doesn't matter. What did he want me to know?"
      "He’s doesn't want to work in politics.":
         verner "I always felt like he was never into politics. And after his mother died maybe I’ve been a little pushy."
         verner "But he is still my son, and I guess I can support him in whatever he wants to do."
         verner "I’ll find time to speak with him."
         verner "Thank you, [povname]."
         jump verner5_pos
      "He’s worried you won’t be okay with what he wants his career to be.":
         verner "Really? I guess I’ve been pretty hard on him since his mother died. I've noticed he hasn't really been as open with me ever since."
         verner "But, I’m sure whatever it is, he can tell me. He might be a better man if he had a little support behind him."
         verner "Thanks for letting me know, [povname]."
         jump verner5_pos
      "It’s nothing. Nevermind.":
         verner "Oh. Well, if you're sure."
         jump verner5_pos

label verner5_pos:
   verner "piss poop"
   jump dayFiveToggle

#TREVOR DAY 5
label trevorDayFive:
   scene bg erstwhilefoyer with fade
   show trevor flustered
   $ trevorWantsToTalkToDad = False
   trev "...Hey, [povname]. Can I talk to you for a minute?"
   menu:
      "Sure, Trevor. What's up?":
         jump trevor5_yes
      "Not right now, I'm busy.":
         jump trevor5_no

label trevor5_yes:
   show trevor default
   trev "I started thinking about what you said yesterday. And I think... I do need some help talking to my dad. Or it's not going to get any better."
   trev "It’s not a big deal, but maybe you could tell my dad how I feel about politics and that I’m thankful for the opportunity he gave me, but I would rather follow my dreams of designing clothes."
   menu:
      trev "Do you think you could do that for me?"
      "I’ll let him know how you feel.":
         $ trevorScore += 5
         trev "Thanks I’ll remember that you did this for me. It was really nice of you. I just struggle to talk with my dad. Well, see you around."
         trev "Thanks, [povname]."
         $ trevorTalk = True
         jump vernerDayFive
      "I guess so but, it’s a little awkward.":
         trev "If you could try, I would appreciate it. I’m sure he won’t get mad at you at least. I’ll see you later."
         $ trevorTalk = True
         jump vernerDayFive
      "Oh... I was just kidding...":
         show trevor annoyed
         $ trevorScore -= 20
         trev "Oh... really? I open up to you and you're just being a dick!"
         trev "Don’t fucking talk to me anymore."
         jump vernerDayFive

label trevor5_no:
   show trevor annoyed
   trev "Oh... I see."
   trev "Whatever. Wasn't important anyway."
   trev "Bye."
   $ trevorWantsToTalkToDad = False
   jump vernerDayFive

# FREDA DAY 5
label fredaDayFive:
   scene bg fredaoffice with fade
   show freda default
   freda "Ah! There you are, [povname]. Listen… I have a special task for you today."
   freda "I received some...flowers, of course..it has a T on the letter that came with them."
   freda "Do you know who that might be?"
   menu:
      freda "Do you know who that might be?"
      "Tacos?":
         jump freda5_tacos
      "Truman?":
         $ fredaScore += 1
         jump freda5_truman

label freda5_truman:
   freda "That’s right! It has to be Truman."
   freda "Truman, oh Truman…"
   freda "Can you go give him this note please? It’d be much appreciated."
   freda "And come back here and tell me what he says."
   $ visitedFreda = True
   jump trumanDayFive

label freda5_tacos:
   freda "Not... quite." 
   freda "It's a person."
   menu:
      freda "It's a person."
      "Oh, right. Truman?":
         $ fredaScore += 1
         jump freda5_truman
      "Trevor?":
         show freda frown
         freda "Trevor...he’s a grouch, why would he ever send me flowers? Who else is here that has a name that starts with T…"
         show freda default
         jump freda5_silly

label freda5_silly:
   menu:
      freda "Trevor...he’s a grouch, why would he ever send me flowers? Who else is here that has a name that starts with T…"
      "Truman?":
         jump freda5_truman
      "I give up":
         jump freda5_exasperated

label freda5_exasperated:
   show freda frown
   freda "It's Truman! It's got to be!"
   show freda happy
   freda "Truman, oh Truman…"
   freda "Can you go give him this note please? It’d be much appreciated."
   freda "And come back here and tell me what he says."
   $ visitedFreda = True
   jump trumanDayFive

#TRUMAN DAY 5
label trumanDayFive:
   scene bg trumanoffice with fade
   show truman default
   truman "Hello! Did...did Freda get my flowers?"
   menu:
      truman "Hello! Did...did Freda get my flowers?"
      "Yep!":
         $ trumanScore += 1
         jump truman5_yes
      "She loved them.": 
         $ trumanScore += 5
         jump truman5_yes

label truman5_yes:
   show truman smile
   truman "Oh good! I’m so happy… "
   show truman default
   truman "You know we both lost our spouses, we are both so lonely these days."
   truman "It’d be great if I had somebody to walk this life again with."
   menu:
      truman "It’d be great if I had somebody to walk this life again with."
      "Why don’t you go talk to her yourself?":
         $ trumanScore += 1
         jump truman5_yesPos
      "I guess I do":
         jump truman5_yesNeu
      "Seems a little dramatic":
         $ trumanScore -= 1
         jump truman5_yesNeg

label truman5_yesNeg:
   truman "Oh you kids don’t understand love these days.."
   truman "One day you’ll get it."
   truman "Maybe today is the day..."
   truman "Yes, that is right, I think I’ll tell her my true feelings."
   menu: 
      truman "Yes, that is right, I think I’ll tell her my true feelings."
      "Tell her what now?":
         jump truman5_tellHerWhat
      "Oh?":
         jump truman5_oh

label truman5_oh:
   show truman smile
   truman "I really like being with her, you know. Maybe I should tell her that."
   truman "Yeah, I think I will."
   truman "Could you do one last favor for me, [povname]?"
   truman "Can you go tell her I want to see her real quick?"
   menu:
      truman "Can you go tell her I want to see her real quick?"
      "She actually asked me to give you this note...":
         jump truman5_giveNote

label truman5_tellHerWhat:
   truman "How much I love her of course!"
   jump truman5_oh

label truman5_yesNeu:
   truman "Love is the most wonderful thing in life...You know what, I should tell her how I feel."
   truman "Yeah, I think I will."
   truman "Could you do one last favor for me, [povname]?"
   truman "Can you go tell her I want to see her real quick?"
   menu:
      truman "Can you go tell her I want to see her real quick?"
      "She actually asked me to give you this note...":
         jump truman5_giveNote

label truman5_yesPos:
   truman "What! I don’t know if she would like that…"
   menu:
      truman "What! I don’t know if she would like that…"
      "You both talk about each other all the time!":
         truman "She talks about me???"
         truman "Maybe you’re right...I will talk to her."
         jump truman5_decision

      "Everyone knows you and Freda are into each other":
         truman "Really?? Is it that obvious? Well I guess there is no denying it."
         truman "Maybe I should tell her how I feel finally in person."
         jump truman5_decision

label truman5_decision:
   truman "Can you go tell her I want to see her real quick?"
   menu:
      truman "Can you go tell her I want to see her real quick?"
      "She actually asked me to give you this note...":
         jump truman5_giveNote

label truman5_giveNote:
   truman "What? She did now?"
   truman "Let me see that."
   truman "..."
   truman "......"
   truman "Oh... I had no idea she felt this same way."
   truman "You know what? I'm done hiding behind others to share my emotions. I'm going to tell her myself."
   truman "Please excuse me, [povname]."
   jump truman5_romanceFinal
 
label truman5_romanceFinal:
   scene bg fredaoffice
   show freda default
   show truman default
   truman "Oh! Freda...Freda, I have something to tell you."
   freda "Yes, Truman?"
   truman "Something I’ve been waiting to tell you for a long time now..."
   freda "I have something I’ve wanted to tell you for a long time now too.."
   truman "Well...Freda..."
   freda "Yes, Truman?"
   show truman smile
   truman "I’m in love with you Freda, I’ve been in love with you since the moment I saw you."
   show freda happy
   freda "Oh Truman! I’ve been in love with you too...for so long."
   truman "This might be crazy... but we're getting older and I won’t take any more chances..."
   truman "Will you… will you marry me Freda?"
   freda "Oh Truman! Yes, yes. I’d love to be your wife for my remaining days.."
   truman "Oh I’m so happy! I’m so glad."
   truman "This all couldn’t have been possible without you, [povname]."
   truman "Say... What do you think about working here full time?" 
   truman "We are retiring here soon, anyways and could use more young people that truly care about the wellbeing of others."
   menu:
      truman "Even if we are just lovestruck old birds."
      "I'd be honored!":
         $fredaScore += 1
         $trumanScore += 1
         truman "Oh good!! Happy days. Let’s get out of here, Freda."
         freda "Right behind you."
         jump romanceEnding
      "I'd love to stay!":
         $fredaScore += 1
         $trumanScore += 1
         truman "Oh good!! Happy days. Let’s get out of here, Freda."
         freda "Right behind you." 
         jump romanceEnding    
      "Nah, that’s ok. I think I'm done with politics.":
         show truman default
         truman "Oh...Ok well, thank you again for your help."
         truman "This all wouldn’t have been possible without you."
         truman "Me and Freda are off! Goodbye!"
         jump neutralEnding

# BLAIR DAY 5
label blairDayFive:
   scene bg blairoffice
   show blair default
   blair "Oh, you’re here, [povname]. Listen, I know we’ve been “talking” lately, and I have a little assignment for you..."
   show blair smirk
   blair "Spying that is, are you in?"
   menu:
      blair "Spying that is, are you in?"
      "Hell yeah! Who are we spying on?":
         $blairScore += 5
         jump blair5_yes
      "What? No, I would never do that.":
         $ blairScore -= 5
         jump blair5_no

label blair5_yes:
   blair "Prime Minister Petrone of course, we must keep an eye on them and wait for the perfect opportunity to strike."
   menu:
      "Strike?":
         $blairScore -= 1
         jump blair5_strike
      "What are we waiting for?":
         $blairScore += 1
         jump blair5_whatWaitingFor
      "Let's get on with it then!":
         jump blair5_letsGetOn

label blair5_strike:
   blair "Yes. Petrone's grip on this country is loosening, and it's time a real leader stepped up to get something done."
   menu:
      blair "Yes. Petrone's grip on this country is loosening, and it's time a real leader stepped up to get something done."
      "Right...":
         blair "I hope you're not getting cold feet on me."
         blair "Well, get going, go get me something juicy."
         jump blair5_goSpy
      "Oh, right!":
         blair "I knew you’d remember, now go get me some good gossip."
         jump blair5_goSpy

label blair5_whatWaitingFor:
   blair "Exactly! Now make sure you bring me something good back."
   blair "We are trying to get rid of her after all."
   jump blair5_goSpy

label blair5_letsGetOn:
   show blair smile
   blair "Perfect, I knew you were the one for this job."
   jump blair5_goSpy

label blair5_no:
   blair "No? Funny, you seemed pretty interested a few days ago."
   blair "You’re seriously going to go back on me like that?"
   show blair smirk
   blair "... Fine. But you'll pay for what you've done."
   menu:
      blair "... Fine. But you'll pay for what you've done."
      "What I’ve done?":
         jump blair5_whatIveDone
      "Not if I throw you in jail first!":
         $ blairScore -= 5
         jump blair5_notIfIDoItFirst
      "Try me.":
         $ blairScore -= 1
         jump blair5_tryMe

label blair5_whatIveDone:
   blair "Why, yes! Trying to overthrow the Prime minister that is, you bastard. I’m calling security."
   menu: 
      "Wait no! Ok ok... I’ll spy on the prime minister":
         $ blairScore += 1
         jump blair5_letsGetOn
      "You're a monster.":
         blair "Security! Security! This intern was trying to assassinate Prime Minister Petrone themself! I have all the evidence to prove it!"
         blair "{i}Good luck trying to worm you way out of this one, kid.{/i}"
         jump arrestedEnding

label blair5_notIfIDoItFirst:
   show blair smirk
   blair "As if!"
   menu:
      blair "As if!"
      "Security! Security! This woman was trying to frame me AND assasinate Prime Minister Petrone!":
         $ blairScore -= 5
         show blair default
         blair "Fuck you."
         jump arrestBlairEnding   
      "Don’t try and play games with me. Let’s just call it even.":
         $ blairScore += 1
         blair "Too little, too late. I’m calling security. Sucker."
         jump arrestedEnding

label blair5_tryMe:
   show blair smirk
   blair "Help! Security! [povname] is trying to attack the prime minister!"
   jump arrestedEnding

label blair5_goSpy:
   scene bg room with fade
   me "It's so quiet... it doesn't look like Prime Minister Petrone is in here..."
   "{i}click... click... click{/i}"
   show petrone silo
   unknown "What's that I smell? A human?"
   unknown "Who goes there?"
   me "Aw, shit..."
   show petrone default
   petrone "You there? Who are you? What are you doing in my office?"
   me "{i}A pigeon????{/i}"
   me "{i}Prime Minister Petrone is???? A pigeon????{/i}"
   me "Uh.... trying to find a bathroom?"
   petrone "Unlikely."
   petrone "You're in {i}*coo coo*{/i} biiiiiig trouble, kid."
   blair "Not so fast!"
   show blair default
   blair "Your bird reign of terror is over, Petrone! Hand it over or we will take it by force!"
   petrone "Over {i}*coo coo*{/i} my dead body."
   blair "Get them, [povname]!"
   menu: 
      blair "Get them, [povname]!"
      "(Attack Petrone)":
         jump blair5_attackPetrone
      "(Kill Petrone)":
         jump blair5_killPetrone
      "(Frame Petrone)":
         jump blair5_framePetrone

label blair5_attackPetrone:
   hide blair default
   "{i}SMASH! CRACK! SQUAK!{/i}"
   petrone "You bastard! I’ll end you!"
   menu:
      "Now, Blair!":
         jump blair5_getPetrone
      "Don’t you dare.":
         jump blair5_dontYouDare

label blair5_getPetrone:
   petrone "NOOO!"
   jump usurpPetroneEnding

label blair5_dontYouDare:
   petrone "Help! Help me! I’m being attacked!"
   unknown "Hey, what's going on in here?"
   me "Uh oh...."
   jump usurpPetroneUnsuccessfulEnding

label blair5_killPetrone:
   "CRACK!!!"
   petrone "AHHHH! I’ll remember this in the next life..."
   jump killedPetroneEnding

label blair5_framePetrone:
   blair "Security! Help! The Prime Minister is attacking an intern!!"
   petrone "I’ll have your head for this!"
   jump usurpPetroneEnding


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
      call resetFlags from _call_resetFlags
      jump startDayThree
   if day == 4:
      if visitedVerner == False:
         $ morganScore -= 10
      call resetFlags from _call_resetFlags_1
      jump startDayFour
   if day == 5:
      if visitedVerner == False or visitedBlair == False:
         $ morganScore -= 10
      call resetFlags from _call_resetFlags_2
      jump startDayFive
   if day == 6: 
      jump end

label resetFlags:
   $ visitedBlair = False
   $ visitedFreda = False
   $ visitedTruman = False
   $ visitedVerner = False
   $ rejectedBlair = False
   $ rejectedFreda = False
   $ rejectedTruman = False
   $ rejectedVerner = False
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

# You got arrested
label arrestedEnding:
   scene bg erstwhileoutside
   with fade
   "Unfortunately, the judge did not believe your side of the story in court."
   "Of course, Blair Bailey was eager to frame you."
   "Your sentence is 25 years. Ouch."
   "You get fired from your internship."
   "Better luck next time."
   "GAME OVER"
   jump end

# You have full time job
label romanceEnding:
   scene bg erstwhileoutside with fade
   "The two lovebirds soon retire after their elopement. Based on their glowing reviews of you, Morgan Odell assigns you to take over both of their positions can be filled."
   "You do such a good job of it, you become the new Secretary of Treasury, officially taking over Freda Robert's role."
   "You end up having a very fruitful career in the Erstwhile House."
   "CONGRATULATIONS"
   jump end

# You finish job
label neutralEnding:
   scene bg erstwhileoutside with fade
   "You finish out your days at your internship with not much fuss."
   "No one appears to overly enjoy your presence, or hate it."
   "You get a positive feedback review from Morgan Odell, and return to your university."
   "Congratulations on a successful summer."
   jump end

# arrest blair
label arrestBlairEnding:
   scene bg erstwhileoutside with fade
   "After a thorough search of her office, Blair Bailey's treason has become apparent to the Erstwhile House government."
   "She is arrested, and sentenced to 25 years. You are showered in praise by the rest of the Erstwhile House staff for your bravery."
   "You get a positive feedback review from Morgan Odell, and return to your university, with a new perspective on the political climate in your country."
   "Congratulations on a successful summer."
   jump end

# kill petrone
label killedPetroneEnding:
   scene bg erstwhileoutside with fade
   "You murdered Prime Minister Petrone."
   "Thankfully, Blair Bailey was able to help convince security that the Prime Minister had gotten a case of fatal bird brain, and gone beserk on you, poor intern."
   "The Erstwhile House thanks you for your bravery."
   "Blair Bailey is eventually named as the new Prime Minister shortly after."
   "She offers you a position as her Chief of Staff."
   "Congratulations on a successful summer."
   jump end

# usurp petrone
label usurpPetroneEnding:
   scene bg erstwhileoutside with fade
   "You successfully usurped the reign of Prime Minister Petrone."
   "Thankfully, Blair Bailey was able to help convince security that the Prime Minister had gotten a case of fatal bird brain, and gone beserk on you, poor intern."
   "The Erstwhile House thanks you for your bravery."
   "Blair Bailey is eventually named as the new Prime Minister shortly after."
   "She offers you a position as her Chief of Staff."
   "Congratulations on a successful summer."
   jump end

# unsucessful government takeover
label usurpPetroneUnsuccessfulEnding:
   scene bg erstwhileoutside with fade
   "You and Blair Bailey's plan to overthrow Petrone's leadership was unsuccessful."
   "Of course, Blair Bailey was eager to frame you, and throw most of the blame on you."
   "Your sentence is 50 years. Ouch."
   "You get fired from your internship."
   "Better luck next time."
   "GAME OVER"
   jump end

# This ends the game.
label end:
   return
