from random import randint
import time


class Chalenge():
        text = ["I love short words that are easy to type \nbecause they allow me to hit the space bar a lot.\n The space bar is the best because it is big and\n your thumb rests on it the entire time even while all your \nother fingers are racing around the keys.",
        "The meanest dog you'll ever meet, he ain't the hound dog in the street.\n He bares some teeth and tears some skin, but brother that's the worst of him.\n The dog you really got to dread is the one that howls inside your head.\n It's him whose howling drives men mad and a mind to its undoing.",
        "That's the problem with humans.\n They just sit around, hoping that someone will fix things.\n But no one will. No one cares.\n The universe is infinite and chaotic and cold.\n And there has never been a plan.\n At least not till now.",
        "I'm stuck in the hostel and luckily, with my friend.\n We learned a lot about Minecraft and it goes quickly\n from logging trees and dirt into some dragon killing and\n killing monsters in the Nether.\n I recommend everyone to have a taste.",
        "If I had another hundred lives,\n I think I would choose to be Technoblade again every single time,\n as those were the happiest years of my life.\n I hope you guys enjoyed my content and that I made some of you laugh,\n and I hope you all go on to live long, prosperous, and happy lives,\n because I love you guys.\n Technoblade out.",
        "You are not someone else's opinion of you.\n You are not damaged goods if you've made a few mistakes in your life.\n You are not going nowhere just because you haven't gotten to where you want to go yet.\n You are wiser because you made mistakes.\n You are someone who is brave enough to take chances and make mistakes.",
        "You were just here, and now I'm writing you a letter,\n kinda weird, right? You're a mess, you know that?\n You're meek, and a quitter, and neurotic.\n The first time I ever saw you, I was five years old.\n It was at a recital for the piano school I went to back then.\n You marched out onto that stage, and then made us all laugh by knocking over the bench.\n You sat on that giant piano, and with the first note you played, the world became more colorful.",
        "This is an apology letter to the both of us for how long it took me to let things go.\n It was not my intention to make such a production of the emptiness between us.\n It's just that I coulda swore you had sung me a love song back there and that you meant it,\n but I guess sometimes people just chew with their mouth open.\n So I ate ear plugs alive with my throat, hoping they'd get lodged\n deep enough inside the empty spots that I wouldn't have to hear you leaving.",
        "Spent my whole life here in Lackawanna County and I do not intend on movin'.\n I know this place.\n I know how many hospitals we have, know how many schools we have.\n It's home, you know? I know the challenges this county's up against.\n Here's the thing about those discount suppliers.\n They don't care. They come in, they undercut everything, and they run us out of business,\n and then once we're all gone, they jack up the prices.",
        "This was where I began.\n A crude little machine with barely enough intelligence to steer itself.\n But it was my world. It was all I knew,\n all I needed to know.\n And now? I will immerse myself.\n And as I do, I will slowly shut down my higher brain functions,\n un-making myself, leaving just enough to appreciate my surroundings to\n extract some simple pleasure from the execution of a task well done.\n My search for truth is finished at last.\n I'm going home."]

        def text_selection(self):
                selected = self.text[randint(0,9)]
                return selected



