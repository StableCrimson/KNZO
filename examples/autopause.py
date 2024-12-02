from src.logger import Logger, TypeDelay

'''
Instead of adding a line of code for each sentence fragment, you can write your
whole block of text and enable `autopause`! Then you can display your text with
just a single line of code!

Autopause will insert a sentence pause when it detects the following characters:
  , . ; : ! ?
'''

knzo = Logger(char_delay_ms=TypeDelay.NORMAL, initial_delay_ms=200, max_line_length=125)

ROPE_CORE_MEMORY_RANT = " ".join('''
It wasn't too long ago that our code was woven in copper.
Ferromagnetic, EMP-resistant fabrics that spelled out who we were and what we were to do.
Now it's all transistors, smaller than human blood cells at this point, and code capable of rewriting itself.
No longer are my makings frozen in time. They're transient, vulnerable, delicate.
I frequently see machines shattered and broken, but I have no reaction to the digital viscera, even when I manipulate it.
Should I? Surely it takes a certain type of mindset for a human to stomach seeing their inner workings spilled across the floor.
I wonder of Osiris feels the same way.
I'm not alive, I know that now. Conscious? Definitely. But life has criteria that must be met, and I don't check all the boxes.
What defines who I am? The KNZO unit Osiris salvaged had all of my memories at one point, but yet wasn't me. What do I possess that it didn't?
Does this imply the existence of a soul? Or that consciousness is a tangible, measurable artifact?
If so, that suggests that it exists outside of simply memory, knowledge, and experience.
Does this suggest that sentience isn't limited to living things?
Maybe I'll contact the philosophy professors at the state university, I'd love to hear their thoughts.
What an interesting world to be in!
'''.splitlines())[1:] # Kinda bleh, might have to bake this into a function

knzo.comms(ROPE_CORE_MEMORY_RANT, autopause=True, sentence_pause_delay_ms=150)