from src.logger import Logger, Loader

knzo = Logger()

'''
To make a spinner, all you need to provide is a
process name (The text that will display with the spinner)
and the duration (in milliseconds) that you want
the spinner to last for.
'''
knzo.spinner("Like this!", 2500)

'''
If you want to change the style of the spinner,
you have a few options! First, you can use
the `Loader` import for a few common spinner styles.
'''
knzo.spinner("This one is a bar!", 2500, spinner=Loader.BAR)
knzo.spinner("This one is a monkey!", 2500, spinner=Loader.MONKEY)

'''
But don't feel limited to those! You can
use all of the provided loader styles given
by `rich`. For a list of the available loaders,
run `python -m rich.spinner` in your terminal.
'''
knzo.spinner("Bouncing ball", 2500, spinner='bouncingBall')
knzo.spinner("Clock", 2500, spinner='clock')
knzo.spinner("Emojis!", 2500, spinner='smiley')

'''
As with the rest of the KNZO library,
you can set an initial delay for the spinner if you're
trying to pace your dialogue, or if you think that things
are just going too fast!
'''
knzo.spinner("KNZO is thinking about his deer...", 2500)
knzo.console.print("[white]WAIT!")
knzo.spinner("KNZO is thinking about his deer again!", 2500, initial_delay_ms=1000)
knzo.clear()

'''
You can also use `rich` inline text styling
to customize your process name!
'''
knzo.spinner("This can help give some [bold][red][underline]impact[/underline][/red][/bold]!", 2500)

