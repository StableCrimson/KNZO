from src.logger import Logger, TypeDelay


'''
https://github.com/Textualize/rich
'''

knzo = Logger(initial_delay_ms=300)

'''
The KNZO library contains wrappers for basic system messages.
'''
knzo.info("Testing info")
knzo.warn("Testing warning")
knzo.error("Testing error")
knzo.comms("Testing comms")
knzo.debug("Testing debug")

knzo.clear_initial_delay

'''
If you want to simulate corruption, you can call `garbage`, which will print
out random data to the terminal. Instead of taking in a message, you simply
pass in the length of the garbage data you want to generate.
'''
knzo.comms("Uh oh. It looks like some memory is corrupted I think I sho", char_delay_ms=45)
knzo.garbage(1000, char_delay_ms=1, append=True)
knzo.error("Vital system binary unreachable. Halting")

'''
For different types of messages, be it for style or mood, you might want them to be printed at different
speeds. This can be done by using `char_delay_ms`. This specifies how many milliseconds the library
will wait before printing the next character.

You can specify the delay manually, but you can also use `TypeDelay` which contains
commonly used message speeds as well.
'''
knzo.comms("Testing comms with delay.", char_delay_ms=TypeDelay.NORMAL, initial_delay_ms=500)
knzo.comms("Testing appending to a terminal entry so I can change typing speeds mid-message. ", char_delay_ms=TypeDelay.NORMAL, append=True)
knzo.set_initial_delay(250)
knzo.comms("For example, ", char_delay_ms=TypeDelay.NORMAL)
knzo.comms("I could type really fast! ", char_delay_ms=TypeDelay.FAST, append=True)
knzo.comms("Or ", char_delay_ms=TypeDelay.NORMAL, append=True)
knzo.set_initial_delay(450)
knzo.comms("... ", char_delay_ms=TypeDelay.SNAIL, append=True)
knzo.comms("I could type ", char_delay_ms=TypeDelay.NORMAL, append=True)
knzo.set_initial_delay(0)
knzo.comms("reeeeeeeaaaaaallyyyy sloooow!", char_delay_ms=TypeDelay.SLOW, append=True)
