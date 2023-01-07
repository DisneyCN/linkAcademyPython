import time
class Team:
    def __init__(self, teamName):
        self.teamName = teamName
class Score:
    def __init__(self, home, away):
        self.home = home
        self.away = away
class Match:
    def __init__(self,home:Score,away:Score,score ):
        self.home = home
        self.away = away
        self.minutes = 0
        self.score = score
    def start(self):
        while True:
            self.minutes += 1
            if self.minutes ==  90:
                print('Match finished')
                break

