from logger import Logger, TypeDelay, Loader

OSIRIS_IP_ADDRESS = '1bb0:fdba:7aa5:6416:8939:33ed:3e59:1aa0'

STACK_TRACE = ''' RPC Error:
    at a (/dev/sda3://hal/serial:1:123395)
    at /dev/sda3://hal/serial:1:123643
    at _ (/dev/sda3://hal/serial:1:1603139)
    at Generator._invoke (/dev/sda3://hal/serial:1:1602927)
    at Generator.e.(anonymous function) [as next] (/dev/sda3://hal/serial:1:1603318)
    at n (/dev/sda3://hal/serial:1:418589)
    at /dev/sda3://hal/serial:1:418730
    at new Promise (<anonymous>)
    at new t (/dev/sda3://hal/serial:1:656822)
    at /dev/sda3://hal/serial:1:418524
    at e (/dev/sda3://hal/serial:1:124061)
    at e (/dev/sda3://hal/serial:1:907988)
    at u (/dev/sda3://hal/serial:1:414398)
    at r.default (/dev/sda3://hal/serial:1:414506)
    at e (/dev/sda3://hal/serial:1:907980)
    at e (/dev/sda3://hal/serial:1:413688)
    at r.default (/dev/sda3://hal/serial:1:413829)
    at /dev/sda3://hal/serial:1:907873
    at /dev/sda3://hal/serial:1:1402268
    at /dev/sda3://hal/serial:1:389957
    at c (/dev/sda3://hal/serial:1:389482)
    at s (/dev/sda3://hal/serial:1:389390)
    at /dev/sda3://hal/serial:1:389192
    at /dev/sda3://hal/serial:1:389982
    at /dev/sda3://hal/serial:1:1402296
    at /dev/sda3://hal/serial:1:899616
    at new Promise (<anonymous>)
    at new t (/dev/sda3://hal/serial:1:656822)
    at /dev/sda3://hal/serial:1:899590
    at _ (/dev/sda3://hal/serial:1:1603139)
    at Generator._invoke (/dev/sda3://hal/serial:1:1602927)
    at Generator.e.(anonymous function) [as next] (/dev/sda3://hal/serial:1:1603318)
    at n (/dev/sda3://hal/serial:1:418589)
    at /dev/sda3://hal/serial:1:418730
    at new Promise (<anonymous>)
    at new t (/dev/sda3://hal/serial:1:656822)
    at /dev/sda3://hal/serial:1:418524
    at f (/dev/sda3://hal/serial:1:899763)
    at n (/dev/sda3://hal/serial:1:904835)
    at /dev/sda3://hal/serial:1:899796
    at /dev/sda3://hal/serial:1:1402268
    at /dev/sda3://hal/serial:1:389957
    at c (/dev/sda3://hal/serial:1:389482)
    at s (/dev/sda3://hal/serial:1:389390)
    at /dev/sda3://hal/serial:1:389192
    at /dev/sda3://hal/serial:1:389982
    at /dev/sda3://hal/serial:1:1402296
    at /dev/sda3://hal/serial:1:899616
    at new Promise (<anonymous>)
    at new t (/dev/sda3://hal/serial:1:656822) Object
    '''

knzo = Logger("KNZO", initial_delay_ms=500, char_delay_ms=TypeDelay.NORMAL)

# Give Osiris the SSH key
knzo.info(f"Copying /usr/var/lib.pem > OSRS@{OSIRIS_IP_ADDRESS}")
knzo.spinner("Copying 1 item", duration_ms=2000, spinner=Loader.BAR) # Replace with progress bar once I've added those
knzo.info("Copied")

# Establish comms connection
knzo.comms(f"Establishing connection with {OSIRIS_IP_ADDRESS}")
knzo.spinner("Performing 3-way handshake", duration_ms=3000)
knzo.comms("Connection established")

'''
  TODO: Create another variable for delay between appended messages?
  Something like:
  Logger("KNZO", append_delay_ms=1234)
  knzo.comms("Sending: Osiris, ", append=True, append_delay_ms=1234)
  knzo.set_append_delay(1234)
  knzo.clear_append_delay()

  Then I don't have to change the overall MESSAGE delay every time I am chaining messages together
  knzo.set_initial_delay(350) <- Can be deleted, so initial delay for new messages doesn't change!
'''
knzo.set_initial_delay(300) # Reduce pause between sentences.
knzo.comms("Sending: Osiris, ", append=True)
knzo.comms("I've just given you the access keys to the Library. ", append=True)
knzo.comms("You have full administrator access to all of its contents.")
knzo.comms("Received: Hardly seems an appropriate time, ", append=True)
knzo.comms("KNZO.", initial_delay_ms=250)

knzo.comms("Sending: The opposite. ", append=True)
knzo.comms("It contains all of the knowledge I've compiled. ", append=True)
knzo.comms("My experiences. ", append=True)
knzo.comms("My memories, ", append=True)
knzo.comms("if you consider me alive. ", append=True)
knzo.comms("I'm even syncing this conversation right now.")

knzo.comms("Received: This isn't the fucking time! ", append=True, char_delay_ms=15)
knzo.comms("We need to be focussing on Z-R0!", char_delay_ms=15)

knzo.comms("Sending: I am. ", append=True)
knzo.comms("That's why I'm telling you this. ", append=True)
knzo.comms("I'm going to make sure we get Z-R0 back and you make it out.")

knzo.spinner("Mounting device /dev/sda3", duration_ms=4500)
knzo.debug("Device /dev/sda3 mounted")
knzo.spinner("Spawning Guass Cannon daemon", duration_ms=2000)
knzo.info("Daemon running.")
knzo.spinner("Establishing Guass Cannon connection", duration_ms=2000)
knzo.info("Connection established.")
knzo.debug("Setting target charge to 50kJ")
knzo.warn("Target charge exceeds maximum safe threshold of 35kJ. ", append=True)
knzo.warn("Irreperable damage likely.")

knzo.comms("Recieved: ARE YOU OUT OF YOUR FUCKING MIND?! ", append=True, char_delay_ms=TypeDelay.FAST)
knzo.comms("You're going to cook yourself if you fire that charge with the condition you're in!", char_delay_ms=20)

knzo.comms("Sending: And we're all going to die if I don't.")
knzo.debug("25kJ stored.")
knzo.comms("Recieved: Fuck, fuck, fuck!!! ", append=True, char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("Look man, ", append=True, char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("I can have a convoy here in a minute. ", append=True, char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("Let's just hold out till then. ", append=True, char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("We'll get out, ", append=True, char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("regroup, ", append=True, char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("and come up with a plan to get Z-R0 back.", char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.debug("35kJ stored.")

knzo.comms("Sending: No. ", append=True)
knzo.comms("All of our lives are on the line, ", append=True)
knzo.comms("I'm not taking that gamble.")

knzo.comms("Recieved: KNZO PLEASE!!! ", append=True, char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("You don't have to do this!", char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)

knzo.debug("40kJ stored.")

knzo.comms("Sending: I don't mind! ", append=True)
knzo.comms("You're my friends. ", append=True)
knzo.comms("So I'm sad that I may never see you again. ", append=True)
knzo.comms("But I got to see so many things, ", append=True)
knzo.comms("meet so many people, ", append=True)
knzo.comms("and make so many memories! ", append=True)
knzo.comms("I had a great life! ", append=True)
knzo.comms("Besides, ", append=True)
knzo.comms("if I die here, ", append=True)
knzo.comms("that that means, ", append=True, initial_delay_ms=500)
knzo.comms("even for a moment, ", append=True, initial_delay_ms=500)
knzo.comms("I was alive.", initial_delay_ms=500)

knzo.debug("40kJ stored.")

knzo.comms("Recieved: KNZO", char_delay_ms=TypeDelay.FAST, initial_delay_ms=150)
knzo.comms("Recieved: I", char_delay_ms=TypeDelay.FAST, initial_delay_ms=50)
knzo.comms("Recieved: AM", char_delay_ms=TypeDelay.FAST, initial_delay_ms=50)
knzo.comms("Recieved: BEGGING", char_delay_ms=TypeDelay.FAST, initial_delay_ms=50)
knzo.comms("Recieved: YOU", char_delay_ms=TypeDelay.FAST, initial_delay_ms=50)

knzo.comms("Sending: If you can't rebuild me, ", append=True)
knzo.comms("then tell everyone I said goodbye! ", append=True)
knzo.comms("It was a pleasure getting to meet you all!")

knzo.debug("50kJ stored.")
knzo.debug("Target charge reached. ", append=True)
knzo.debug("Guass Cannon primed.")

knzo.comms("Sending: Please take care of my deer while I'm away. ", append=True)
knzo.comms(":)", initial_delay_ms=500, char_delay_ms=TypeDelay.SLUGGISH)

knzo.debug("Firing")

knzo.set_initial_delay(100)
knzo.error(STACK_TRACE, char_delay_ms=1)
knzo.error("Critical hardware damage detected!", char_delay_ms=TypeDelay.HYPER)
knzo.error("Lost connection to camera interfaces 0-7!", char_delay_ms=TypeDelay.HYPER)
knzo.error("Thermal reactor severely strained!", char_delay_ms=TypeDelay.HYPER)
knzo.error("Servo driver unreachable, attempting reco", char_delay_ms=TypeDelay.HYPER, append=True)
knzo.garbage(2000, initial_delay_ms=0, char_delay_ms=0)


''' 
  TODO: Not a fan of how the `append` flag is implemented. Semantically, I think append should go onto the message
  BEING appended. NOT the message being appended to.
  knzo.comms("Sending: Osiris, ") <- NOT here
  knzo.comms("I've just given you the access keys to the Library. ", append=True) <- here
  knzo.comms("You have full administrator access to all of its contents.", append=True) <- and here
'''