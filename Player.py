class Player(object):
    """Given some reputation, slacks off as much as possible while still
    maintaining that reputation and hunts the rest of the time.

    Motivation: No matter what the other person does, you get the same
    relative benefit by slacking rather than hunting. You just want to
    make sure that you have a high enough reputation that other people
    will still hunt with you.
    """
    
    def __init__(self):
        # This value for ideal_ratio was chosen as follows:
        # I anticipate that some Reciprocators will only reciprocate
        # with players who have a reputation above 0.6, but very
        # few will choose a value higher than this.
        self.ideal_ratio = 0.60000001
        
        self.name = "LazyHunter(%s)" % self.ideal_ratio
        self.hunts = 0
        self.total = 0

    def __repr__(self):
        return self.name

    def hunt_choices(self, round_number, current_food,
                         current_reputation, m, player_reputations):
        num_players = len(player_reputations)
        self.total += num_players

        # Calculate what my reputation will be if I don't hunt this
        # round. If it is at least as high as self.ideal_ratio, I can
        # afford to slack off.
        if float(self.hunts) / self.total >= self.ideal_ratio:
            return ['s'] * num_players

        # Looks like I couldn't afford to slack off. I hunt this round
        # and record my decision.
        self.hunts += num_players
        return ['h'] * num_players

    def hunt_outcomes(self, *args):
        pass

    def round_end(self, *args):
        pass
