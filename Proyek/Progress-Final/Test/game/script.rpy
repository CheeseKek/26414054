
define s = Character('Shiro')
define l = Character('Lea')
define sh = Character('Shiro?')
define i = Character(None,window_left_padding=70,image="shiro")
define slideawayup = CropMove(1.0, "slideawayup")
define slideawaydown = CropMove(1.0, "slideawaydown")
define coba = ComposeTransition(dissolve,before=slideawaydown,after=slideawayup)
image side shiro = "shiro.png"
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
##screen countdow:
    ##timer 1 repeat True action If(time >= 0, true=SetVariable('time', time + 1), false=[Hide('countdown'), Jump(timer_jump)])
   ## if time <= 2:
   ##     text str(time) xpos .1 ypos .1 color "#FF0000" at alpha_dissolve
   ## else:
  ##      text str(time) xpos .1 ypos .1 at alpha_dissolve
init:
    ##$ n = Character(None, kind=nvl)
    $ n = Character(None, kind=nvl,
                          what_size=20,
                          what_xalign=0.5,
                          window_xalign=0.5,
                          window_yalign=1.0,
                          what_text_align=0.5,
                          window_background=None,
                          what_outlines=[(3, "#000000", 2, 2), (3, "#282", 0, 0)],
                          #Gives an outline
                          what_slow_cps=20,
                          )
    $ slow_dissolve = Dissolve(1.0)
    image side shiro happy = im.Crop("shiro_side.png", 0, 0, 429, 400)
    $ timer_range = 0
    $ timer_jump = 0
label start:
    stop music fadeout 1.0
    ##show screen countdow
    scene black
    i happy "It seems to be really out of the blue, even for my standards, but for some reason I have this feeling that I need to introduce myself."
    i happy "I'm Shiro Shiroma, usually called Shiro by my friends."
    i happy "Just your usual Japanese high school boy you usually see everyday."
    i happy "Likes to play games, watch movies, and stuff normal people usually like to do."
    i happy "Well, at least until yesterday that I'm a normal person."
    i happy "It was my eighteenth birthday yesterday. With your usual birthday party of that age and stuff."
    i happy "But for some reason, when I woke up today, I feel great."
    i happy "Or rather, I feel beyond great. Something like, really strong."
    i happy "Maybe it's 'powerful'? I mean, my voice changed a bit somehow."
    i happy "I can feel like some sort of power lingering inside me, along with something else."
    extend " Or could it be someone?"
    i happy "Well, whatever. Not that I care that much right now."
    i happy "But still, maybe this, 'power', is related to my voice? Or it just affected my voice"
    i happy "I mean, I can say anything and do anything just fine, and nothing unusual happened."
    i happy "Well, considering the size of my room, I can't do too much anyway, so it's hard to notice anything different."
    
    show shiro with dissolve
    s "Maybe I can wish for anything I want?!"
    hide shiro with dissolve
    i happy "Oops, didn't mean to say it out loud."
    i happy "Oh well, guess I'll try it later."
    i happy "I haven't told this to anyone actually, not even my parents."
    i happy "Also I can't tell if there's anything different about my parents and my friends."
    i happy "Looks like I'm the only one that has changed, as much as I know at least."
    
label to_school:
    
    scene bg street
    
    i happy "I'm going to try lots of things about this 'power' of mine I got yesterday for today."
    i happy "My schedule's today really jam-packed, so I think I can only try to do one kind of thing only."
    i happy "But the question is, what should I try to do later?"
    
    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'menu1_slow'
    show screen countdown
    menu:
        "Punch a tree.":
            hide screen countdown
            jump meaningless_one
        "Throw a ball.":
            hide screen countdown
            jump meaningless_two

label menu1_slow:
    nvl show dissolve
    n "You didn't choose anything."
    i happy "Uhhh, I can't think of anything."
    i happy "Well, whatever. It can be done later just fine."
    nvl clear
    nvl hide dissolve
    jump meaningless1_done
    
label meaningless_one:
    
    ##$ meaningless1_flag = True
    
    i happy "Guess I'll try to punch a tree later at the park after school."
    i happy "Possibly as many as possible."
    i happy "Well, it sounds kinda random, but it certainly worth a try."
    
    jump meaningless1_done
    
label meaningless_two:
    
    ##$ meaningless1_flag = False
    
    i happy "A ball."
    extend " Wait, a ball?"
    extend " Did I just think about a ball?"
    i happy "Why am I thinking about a ball?"
    i happy "Okay, that was WAY too random to the point it even creeps me out." with hpunch
    i happy "But hey, maybe I can try to throw a ball as far as possible later."
    
    jump meaningless1_done
    
label meaningless1_done:
    
    nvl show dissolve
    $ renpy.play('footsteps.wav')
    n "Then suddenly a group of suspicious looking people appeared out of nowhere in the distance."
    stop sound fadeout 1.0
    nvl clear
    nvl hide dissolve
    i happy"Those three sure looks weird."
    i happy"But it seems these people aren't noticed by everyone nearby."
    i happy"I mean, seriously, with those black suit and stuff like an agent, in the morning, running in the street,"
    extend "and nobody notices them except me?"
    i happy"There's something really fishy in here."
    i happy"Wait, they're looking at me?"
    show shiro wonder at left with dissolve 
    s "Uh oh, this can't be good."
    hide shiro wonder with dissolve
    i happy"Holy mother of -- did one of them jumped over my head?!"
    
    ##$ renpy.play('punch.wav')
    with vpunch
    
    show shiro shock at left
    s "Ack!"
    hide shiro shock
    i happy "Great. I completely forgot about the other two and they grabbed my arms."
    show shiro squint at left
    s "Who are you people?!"
    hide shiro squint
    nvl show dissolve
    n "No response."
    nvl clear
    nvl hide
    i happy "Seems like they're professional to these kind of odd jobs."
    show shiro squint at left
    s "Why are you--"
    hide shiro squint
    nvl show
    "A dull noise." 
    $ renpy.play('punch.wav')
    with hpunch
    nvl clear
    nvl hide
    i happy "My view's spinning."
    i happy "Did that one just knocked me--"
    
label prison1:
    
    scene black
    with coba
    
    s "Uuugh."
    i happy "Oooh, my neck hurts so bad."
    i happy "It feels like I slept for three whole days, and my head feels really heavy"
    i happy "Just what the hell those people were up to anyway?"
    
    scene bg cell
    with slow_dissolve
    
    i happy "..."
    i happy "Wait a minute. Where am I?"
    i happy "What is this place?"
    i happy "It looks like... "
    i happy "A prison? Why am I in a prison?!"
    show shiro shock with dissolve
    s "Hold on. Calm down me, calm down." with hpunch
    s "Freaking out won't help me whatsoever right now, let alone anything good would happen if I do so."
    hide shiro shock
    i happy "*huff* *huff* *huff*" with hpunch
    i happy "..."
    i happy "Alright, that's better."
    i happy "Now, I'd better observe my surroundings."
    show shiro wonder with dissolve
    s "Wait, is that...?"
    hide shiro wonder
    i happy "On first look, it certainly looks like an old prison."
    i happy "...wait, are those machineries?"
    i happy "Lots of them, outside some of the cells including mine apparently."
    i happy "Looks like computers or some sort. Not really my kind of stuff."
    i happy "But I certainly can tell that it's not a part of a security system for sure."
    i happy "It looks pretty clean as well. Did the one who uses this place renovated it?"
    $renpy.play('footstepw.wav')
    i happy "...footsteps?"
    i happy "No wait, sounds more like this person's using high heels."
    i happy "Sounds like a woman alright."
    i happy "But why is that woman in here?"
    i happy "Is this place--"
    stop sound
    stop music
    show shiro wonder at left
    show lea at right
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
    i happy"She sure is a weird one."
    l "Ah yes, I almost forgot."
    l "01230."
    s "What?"
    l "01230. It's your code here. Just be sure to remember it."
    s "Oookay...?"
    $ renpy.play('footstepw.wav')
    hide lea with dissolve
    hide shiro wonder
    i happy"She left for sure this time."
    stop sound
    stop music
    sh "She's pretty interesting, I must admit."
    show shiro shock
    s "Wait, who was that?!"
    hide shiro shock
    i happy "..."
    i happy "Was it just my imagination?"
    i happy "Maybe it's because my head still hurts."
    i happy "Guess I'll take another rest for now."
    i happy "But what do I do from now on?"
    i happy "Maybe I can actually get out of this place?"
    i happy "Based on what she said, this place doesn't sounds like it's filled with friendly people."
    i happy "I guess surviving comes first."
    i happy "And better stick to this place's rules as well."

    scene black with slow_dissolve

    return
