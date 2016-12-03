## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define s = Character('Shiro',color="#888888")
define l = Character('Lea')
define sh = Character('Shiro?')
init:
    # Define some new transitions here.
    $ nvle = Character(None,color="#c8ffc8", kind=nvl)
    $ slow_dissolve = Dissolve(1.0)
    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve
    define slideawayup = CropMove(1.0, "slideawayup")
    define slideawaydown = CropMove(1.0, "slideawaydown")
    define coba=ComposeTransition(dissolve,before=slideawaydown,after=slideawayup)
init python:
        style.nvl_window.top_padding = 800
        ##style.nvl_window.bottom_padding = ##
       ## style.nvl_window.left_padding = ##
       ## style.nvl_window.right_padding = ##

## The game starts here.

label start:
    stop music fadeout 1.0
    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene black

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    ## These display lines of dialogue.

    ##$ meaningless1_flag = True
    ## Flag is disabled for any choice taken will not affect story whatsoever, hence the name meaningless
    "It seems to be really out of the blue, even for my standards, but for some reason I have this feeling that I need to introduce myself."
    "I'm Shiro Shiroma, usually called Shiro by my friends."
    "Just your usual Japanese high school boy you usually see everyday."
    "Likes to play games, watch movies, and stuff normal people usually like to do."
    "Well, at least until yesterday that I'm a normal person."
    "It was my eighteenth birthday yesterday. With your usual birthday party of that age and stuff."
    "But for some reason, when I woke up today, I feel great."
    "Or rather, I feel beyond great. Something like, really strong."
    "Maybe it's 'powerful'? I mean, my voice changed a bit somehow."
    "I can feel like some sort of power lingering inside me, along with something else."
    extend " Or could it be someone?"
    "Well, whatever. Not that I care that much right now."
    "But still, maybe this, 'power', is related to my voice? Or it just affected my voice"
    "I mean, I can say anything and do anything just fine, and nothing unusual happened."
    "Well, considering the size of my room, I can't do too much anyway, so it's hard to notice anything different."
    
    
    s "Maybe I can wish for anything I want?!"
    
    "Oops, didn't mean to say it out loud."
    "Oh well, guess I'll try it later."
    "I haven't told this to anyone actually, not even my parents."
    "Also I can't tell if there's anything different about my parents and my friends."
    "Looks like I'm the only one that has changed, as much as I know at least."
    
label to_school:
    
    scene bg street
    ##street background here
    
    show shiro
    ##requires main char sprite first
    
    "I'm going to try lots of things about this 'power' of mine I got yesterday for today."
    "My schedule's today really jam-packed, so I think I can only try to do one kind of thing only."
    "But the question is, what should I try to do later?"
    
    
    menu:
        "Punch a tree.":
            jump meaningless_one
            
        "Throw a ball.":
            jump meaningless_two
            
label meaningless_one:
    
    ##$ meaningless1_flag = True
    
    "Guess I'll try to punch a tree later at the park after school."
    "Possibly as many as possible."
    "Well, it sounds kinda random, but it certainly worth a try."
    
    jump meaningless1_done
    
label meaningless_two:
    
    ##$ meaningless1_flag = False
    
    "A ball."
    extend " Wait, a ball?"
    extend " Did I just think about a ball?"
    "Why am I thinking about a ball?"
    "Okay, that was WAY too random to the point it even creeps me out." with hpunch
    "But hey, maybe I can try to throw a ball as far as possible later."
    
    jump meaningless1_done
    
label meaningless1_done:
    
    ##nvl show dissolve
    "Then I suddenly see a group of suspicious looking people appeared out of nowhere in the distance."
    "Those three sure looks weird."
    "But it seems these people aren't noticed by everyone nearby."
    "I mean, seriously, with those black suit and stuff like an agent, in the morning, running in the street,"
    extend "and nobody notices them except me?"
    "There's something really fishy in here."
    "Wait, they're looking at me?"
    ##nvl clear
    ##nvl hide dissolve
    s "Uh oh, this can't be good."
    ##nvl show dissolve
    "Holy mother of -- did one of them jumped over my head?!"
    ##nvl clear
    nvl hide dissolve
    
    ##$ renpy.play('punch.wav')
    with vpunch
    ##show shiro_surprised
    
    s "Ack!"
    "Great. I completely forgot about the other two and they grabbed my arms."
    s "Who are you people?!"
    "No response."
    "Seems like they're professional to these kind of odd jobs."
    s "Why are you--"
    "A dull noise." with hpunch
    "My view's spinning."
    "Did that one just knocked me--"
    
label prison1:
    
    scene black
    with coba
    
    s "Uuugh."
    "Oooh, my neck hurts so bad."
    "It feels like I slept for three whole days, and my head feels really heavy"
    "Just what the hell those people were up to anyway?"
    
    scene bg cell
    with slow_dissolve
    ##transition animation here
    
    "..."
    "Wait a minute. Where am I?"
    "What is this place?"
    "It looks like... "
    "A prison? Why am I in a prison?!"
    s "Hold on. Calm down me, calm down." with hpunch
    s "Freaking out won't help me whatsoever right now, let alone anything good would happen if I do so."
    "*huff* *huff* *huff*" with hpunch
    "..."
    "Alright, that's better."
    "Now, I'd better observe my surroundings."
    s "Wait, is that...?"
    "On first look, it certainly looks like an old prison."
    "But then, I noticed machineries."
    extend "Lots of them, outside some of the cells including mine apparently."
    "Looks like computers or some sort. Not really my kind of stuff."
    "But I certainly can tell that it's not a part of a security system for sure."
    "It looks pretty clean as well. Did the one who uses this place renovated it?"
    "...footsteps?"
    "No wait, sounds more like this person's using high heels."
    "Sounds like a woman alright."
    "But why is that woman in here?"
    "Is this place--"
    l "And you must be the new one here."
    s "What? Who--"
    l "Ah yes, pardon my rudeness. I forgot to introduce myself."
    l "I'm Lea. Call me Lea."
    l "Since you'll be here for quite a while, I suppose it wouldn't hurt for me to let you know my name."
    s "Yeah, and I'm--"
    l "Shiro, I know that."
    s "What? But how--"
    l "It's all in here. All your data."
    l "Your hobbies. Your favorite pastimes."
    l "Even your power."
    s "What? Did you said--"
    l "Actually, what your power seems to be. We only managed to scratch a bit."
    s "H-hold on. I'm really confused right now."
    s "First thing first, where are we?"
    s "This is not a prison, I know that much."
    l "Well, I guess I can tell you about this place."
    l "We're at a research facility, where we keep you and your kind and study how powerful you 'special' people are."
    l "It a research facility by name only actually, it's a lot worse than that."
    s "Wait what? My kind? What do you mean by that?"
    l "Well, I mean people with power. Just like you."
    l "Anyway, your data says that you're somewhat weak, but I have a feeling that you might be the one."
    l "Maybe you'll be the one to get me out of this hell hole?"
    s "What?"
    l "ANYWAY, that's all for now. See you around."
    s "Well, I won't go anywhere anyway."
    "She sure is a weird one."
    l "Ah yes, I almost forgot."
    l "01230."
    s "What?"
    l "01230. It's your code here. Just be sure to remember it."
    s "Oookay...?"
    "She left for sure this time."
    sh "She's pretty interesting, I must admit."
    s "Wait, who was that?!"
    "..."
    "Was it just my imagination?"
    "Maybe it's because my head still hurts."
    "Guess I'll take another rest for now."
    "But what do I do from now on?"
    "Maybe I can actually get out of this place?"
    "Based on what she said, this place doesn't sounds like it's filled with friendly people."
    "I guess surviving comes first."
    "And better stick to this place's rules as well."

    ## This ends the game.

    return
