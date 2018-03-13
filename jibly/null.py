# Then let's import the logging module so we can print out information
import logging

import sys
sys.path.append('.')
if len(sys.argv) > 1 and sys.argv[1] == "NODEBUG":
    from hlt.networking import Game
else:
    from socketnetworking import Game

# GAME START
# Here we define the bot's name as Settler and initialize the game, including communication with the Halite engine.
game = Game("Null")
# Then we print our start message to the logs
logging.info("Starting my null bot!")

while True:
    # TURN START
    # Update the map for the new turn and get the latest version
    game_map = game.update_map()
    if game_map is None:
        # no more updates
        break
    command_queue = []
    game.send_command_queue(command_queue)
