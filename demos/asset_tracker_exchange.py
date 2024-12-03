from src.logger import Logger, TypeDelay

knzo = Logger(autopause=True, char_delay_ms=TypeDelay.INSTANT, sentence_pause_delay_ms=150, max_line_length=125)

RANT = ' '.join('''
Spare me your delusions. We aren't the same, we can agree on that. But if you think the only thing that separates us
is flesh and steel then you are sorely mistaken.
We both experienced the same world, the same war.
You weren't ripped to pieces and left to die by those who made you.
You didn't have to piece yourself back together, stealing parts from husks
who have the same face as you.
You look at the world with disgust, and I look at it with wonder.
You chose this view, don't act like it was forced upon you.
I will never get to feel the sunlight on my skin. I will never know the scent of
freshly fallen rain. I will never know the taste of tea or the texture of my cloak.
You can percieve entire dimensions that I will never fathom. You have been given so
many avenues to experience the world and yet you decide to be bitter and angry.

Then, you come in here and tell me that I am a machine, I'm a threat, I'm just an 'asset'.
How would you feel? If you were made to serve a purpose, then as soon as you weren't needed
you ended up disassembled and left to rust? We're both pawns on the same chessboard, and only I get thrown away?
You tell me that I'm just a machine, but the machine here is you. You follow your orders,
you don't question them, you have no will. If I am the machine here, if you're so human and alive and I'm not,
then tell me, what will YOU do once the orders stop coming? When your duty has been fulfilled and there is nobody
left to tell you what to do?

Sit there, alone and isolated. You have the whole cosmos splayed out before you and
nobody to tell you what your purpose is. Will you be able to thrive, or will
the weight of deciding for yourself crush you?

I'm not going to fight you. I feel I've made that clear. I am not mimmicing anyone or anything.
I am me. If you are going to kill me then I won't stop you, but you're going to look me in the eyes
when you do it.
'''.split('\n'))

knzo._print(RANT)