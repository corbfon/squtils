# This file is for strategy

from util.objects import *
from util.routines import *


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        self.defend_flag = is_ball_going_towards_goal(self)

        # set_intent tells the bot what it's trying to do
        if self.intent is not None:
            return

        if self.kickoff_flag:
            self.set_intent(kickoff())
            return

        print(self.defend_flag)

        if self.defend_flag:
            self.set_intent(defend_shot())
            return
