############################
# THIS IS GOING TO BE HELL #
############################

import pygame
import math
import random
import os


# Ideas for AI
# Get a list of possible actions (move, attack, scout, etc) and assign each some arbitrary value, a "fitness value"
# Give perhaps top 3 or 5 further consideration and calculation (Like predicting moves and outcomes) and decide which has best "outcome" (Again, some arbitrary value)
# 
# Do a multi-pass system where the first one or two passes will calculate map and terrain values such as some kind of "heat map" of sorts to assign
# arbitrary values to each grid for how "explored" they are. Highest priorities will go to tiles that have never been visited before and priority will increase
# for tiles that haven't been visited in a while. This could be used in conjunction with a similar map but of known enemy (our) positions where any known positions
# will be "hotter" but as turns pass, the known locations will get "colder" as the chances of the enemy (us) having moved to a different area of the map increases greatly.
# 
# once some sort of "destination" can be achieved for the enemy to attempt, use A* obviously.
#
# Perhaps keep something like a priority queue on what possible actions are and keep it dynamic for changing objectives and whatnot for the AI.


