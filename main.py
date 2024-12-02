from src.logger import Logger, TypeDelay


'''
https://github.com/Textualize/rich
'''

knzo = Logger(initial_delay_ms=300)

knzo.info("Testing info")
knzo.warn("Testing warning")
knzo.error("Testing error")
knzo.comms("Testing comms")
knzo.debug("Testing debug")

knzo.clear_initial_delay
knzo.comms("Uh oh. It looks like some memory is corrupted I think I sho", char_delay_ms=45)
knzo.garbage(1000, char_delay_ms=1, append=True)

knzo.error("Vital system binary unreachable. Halting")

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

knzo.spinner("KNZO is thinking about his deer", duration_ms=5000, spinner="aesthetic")
knzo.info("Thought finished! ", char_delay_ms=TypeDelay.NORMAL)
knzo.info("What a good deer!", char_delay_ms=TypeDelay.NORMAL, initial_delay_ms=250, append=True)

knzo.console.print("SYSTEM INFO", style="white")
