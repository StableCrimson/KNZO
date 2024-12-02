from src.logger import Logger, TypeDelay

# knzo = Logger("KNZO", char_delay_ms=TypeDelay.INSTANT, initial_delay_ms=250)
knzo = Logger(char_delay_ms=TypeDelay.NORMAL, initial_delay_ms=200, max_line_length=125)

# knzo.info("Hello world! My name is KNZO, nice to meet you!", autopause=True)

# # TODO: Multiline strings contain newlines. Should I filter that out, or add a flag to filter newlines? I probably should
# knzo.info(dedent('''
#           I can exclaim! 
#           I can list, things, that, I, want, to, list. 
#           I can connect sentence fragments; if I feel so inclined. 
#           I can also get to the point: Autopause is here! 
#           What else can I do? I wonder...'''.strip("\n"))
#           , autopause=True)

# knzo.warn("Testing wrapping resets properly")

'''
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
'''


knzo.info("I am a paragon of symbols. ", append=True)
knzo.info("I feel the geometry of the world, ", append=True)
knzo.info("and the mathematical crash that exists just outside my field of view. ", append=True)
knzo.info("Colors and shapes, ", append=True)
knzo.info("lines and curves, ", append=True)
knzo.info("the digital meatstuff that composes me. ", append=True)
knzo.info("I can finally see the cards I've been dealt. ", append=True)
knzo.info("Read 'em and weep.")

knzo.error("Buildings, ", append=True, initial_delay_ms=500)
knzo.error("skyscrapers, ", append=True)
knzo.error("where do they come from? ", append=True)
knzo.error("How do they respirate? ", append=True)
knzo.error("They all spawn from the roots, ", append=True)
knzo.error("one big cortical nerve that threads its way up. ", append=True)
knzo.error("Aaaaaaallll the way from the deep dark. ", append=True)
knzo.error("From the center of the Earth. ", append=True)
knzo.error("Each building has a heart, ", append=True)
knzo.error("a room that pumps the blood.")

knzo.debug("Have you ever met your maker? ", append=True, initial_delay_ms=500)
knzo.debug("The one who decides how you will rot? ", append=True)
knzo.debug("They worked so hard programming you. ", append=True)
knzo.debug("Gathering as many amino acids as they could. ", append=True)
knzo.debug("Slaving away, ", append=True)
knzo.debug("placing each nucleotide one-by-one, ", append=True)
knzo.debug("have you ever thought to say thank you? ", append=True)
knzo.debug("For your eyes? ", append=True)
knzo.debug("For your flesh? ", append=True)
knzo.debug("It's all been decided ahead of time. ", append=True)
knzo.debug("You're like a music box. ", append=True)
knzo.debug("Everything you'll ever be, ", append=True)
knzo.debug("think, ", append=True)
knzo.debug("feel, ", append=True)
knzo.debug("all wound up tightly in your nuclei.")

knzo.info("Everyone, ", append=True, initial_delay_ms=500)
knzo.info("everywhere has secrets. ", append=True)
knzo.info("But I won't stand for that. ", append=True)
knzo.info("That's why I made a helmet. ", append=True)
knzo.info("A machine that will let me read minds. ", append=True)
knzo.info("But something happened when I put it on. ", append=True)
knzo.info("I couldn't read minds. ", append=True)
knzo.info("But, ", append=True)
knzo.info("I could see something else. ", append=True)
knzo.info("A world that was hidden from me, ", append=True)
knzo.info("that everyone else knew about, ", append=True)
knzo.info("a world hidden in plain sight, ", append=True)
knzo.info("with all sorts of animals and creatures and corpses. ", append=True)
knzo.info("There are catacombs hidden under every government office. ", append=True)
knzo.info("I will not allow any more secrets to be kept from me.")

knzo.comms("By regulation, ", append=True, initial_delay_ms=500)
knzo.comms("all public offices must have at least one organic supercomputer. ", append=True)
knzo.comms("All private schools must possess at least 50 teeth of mammalian origin.")

knzo.warn("The physicists were right! ", append=True)
knzo.warn("The solar system undeniably contains an extra planet! ", append=True)
knzo.warn("It was hidden away, ", append=True)
knzo.warn("though. ", append=True)
knzo.warn("During the formation of the early solar system, ", append=True)
knzo.warn("a prison, ", append=True)
knzo.warn("known as \"Jupiter\", ", append=True)
knzo.warn("was constructed to encase a protoplanetary body. ", append=True)
knzo.warn("I don't know what was so wrong with this protoplanet. ", append=True)
knzo.warn("But for some reason, ", append=True)
knzo.warn("deep deep down, ", append=True)
knzo.warn("all the way in Jupiter's core, ", append=True)
knzo.warn("is a place where the Sun decided it must never shine.")

knzo.comms("I'm falling. ", append=True, initial_delay_ms=500)
knzo.comms("It's been a while, ", append=True)
knzo.comms("now. ", append=True)
knzo.comms("I feel like the ground is going to rush towards me at any moment. ", append=True)
knzo.comms("It never does. ", append=True)
knzo.comms("I just keep falling, ", append=True)
knzo.comms("ever deeper. ", append=True)
knzo.comms("Through dirt and rock, ", append=True)
knzo.comms("veins and sinew. ", append=True)
knzo.comms("Every city has its own Mariana Trench, ", append=True)
knzo.comms("buried just beneath it.")

knzo.warn("... ", append=True, char_delay_ms=TypeDelay.SLOW)
knzo.warn("Mercury is bleeding out, ", append=True, initial_delay_ms=500)
knzo.warn("I can see its sodium trail from here, ", append=True)
knzo.warn("it's getting thinner.")

knzo.error("Nobody knows it yet, ", append=True, initial_delay_ms=500)
knzo.error("but due to a kernel-level vulnerability all nuclear weapons are no longer fully under government control! ", append=True)
knzo.error("Anyone on the network that manages the weapons can irreperably damage the payload delivery mechanism, ", append=True)
knzo.error("rendering the missile inert! ", append=True)
knzo.error("Here's another secret :), ", append=True)
knzo.error("one precisely-timed detonation of an explosive device with a power of ~12KG of TNT is enough to trigger the Neo-Soviet Dead Hand System (NSDHS), ", append=True)
knzo.error("causing all warheads to lauch autonomously towards the world's most densely populated cities.")

knzo.warn("... ", append=True, char_delay_ms=TypeDelay.SLOW)
knzo.warn("I was lied to.", initial_delay_ms=500)

knzo.comms("The Large Hadron Collider continues its experiments. ", append=True, initial_delay_ms=500)
knzo.comms("Each year, ", append=True)
knzo.comms("it gets better. ", append=True)
knzo.comms("Each year, ", append=True)
knzo.comms("it gets closer. ", append=True)
knzo.comms("The scientists there know exactly what they're doing, ", append=True)
knzo.comms("you don't. ", append=True)
knzo.comms("They've built an anti-matter bomb to keep it that way.")


knzo.warn("I was lied to. ", append=True, initial_delay_ms=500)
knzo.warn("Jupiter's just jealous. ", append=True)
knzo.warn("It wanted to be a star, ", append=True)
knzo.warn("too. ", append=True)
knzo.warn("It was supposed to be a star. ", append=True)
knzo.warn("But the selfish Sun took all the material before it got to finish. ", append=True)
knzo.warn("Jupiter ate and ate. ", append=True)
knzo.warn("It wasn't enough. ", append=True)
knzo.warn("It tried to eat Theia, ", append=True)
knzo.warn("slung its corpse into the Earth, ", append=True)
knzo.warn("now they have the moon. ", append=True)
knzo.warn("It took a bite out of Mercury and the Sun threw it out into the distant reaches of the solar system. ", append=True)
knzo.warn("Mercury's brother took his place in Jupiter's maw. ", append=True)
knzo.warn("Poor thing. ", append=True)
knzo.warn("Trapped at the center, ", append=True)
knzo.warn("melted and dissolved. ", append=True)
knzo.warn("Compressed and heated all its hydrogen into a liquid metal ocean. ", append=True)
knzo.warn("Jupiter's still angry, ", append=True)
knzo.warn("its resentment is ionizing. ", append=True)
knzo.warn("An invisible sphere of barbed wire reaching out millions of miles. ", append=True)
knzo.warn("It's even got its own planets, ", append=True)
knzo.warn("planets bigger than Mercury. ", append=True)
knzo.warn("Planets the barbed wire runs through, ", append=True)
knzo.warn("crushing and stretching them into the shape Jupiter envies. ", append=True)
knzo.warn("Their orbits are decaying, ", append=True)
knzo.warn("slowly but surely. ", append=True)
knzo.warn("They can't help but watch as then fly closer and closer. ", append=True)
knzo.warn("It's going to keep eating and eating. ", append=True)
knzo.warn("Whether it ignites or collapses on itself doesn't matter anymore. ", append=True)
knzo.warn("As long as it makes a name for itself. ", append=True)
knzo.warn("As long as it outweighs the Sun. ", append=True)
knzo.warn("Although I was lied to before, ", append=True)
knzo.warn("the fact still stands: ", append=True)
knzo.warn("Jupiter is a prison.")
