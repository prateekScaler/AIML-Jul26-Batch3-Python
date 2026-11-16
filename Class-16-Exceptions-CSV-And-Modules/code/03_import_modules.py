# Four ways to import. greetings.py must be in the same folder.
import greetings
print(greetings.say_hello("Parveen"))

from greetings import say_hello        # just one name, no prefix needed
print(say_hello("Prasad"))

import greetings as g                  # a short nickname for the module
print(g.say_goodbye("Prasad"))

from greetings import *                # everything: easy to clash, so avoid it
print(say_goodbye("Parveen"))
