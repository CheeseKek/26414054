## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define s = Character('Shiro')

## The game starts here.

label start:

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

    "I'm going to try lots of things about this 'power' of mine I got yesterday for today."
    "My schedule's today really jam-packed, so I think I can only try to do one kind of thing only."
    "But the question is, what should I try to do later?"

    "Guess I'll try to punch a tree later at the park after school."
    "Possibly as many as possible."
    "Well, it sounds kinda random, but it certainly worth a try."
    
    "Then I suddenly see a group of suspicious looking people appeared out of nowhere in the distance."

    ## This ends the game.

    return
