import argparse
import random
import datetime


def throw_the_die(sides=6):
    """
    Simulate throwing a die

    :param sides: number of sides
    :return: Values
    """
    return random.randint(1, sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def show(self):
        print(f"{self}")

    def __str__(self):
        """String representation"""
        return f"{self.name}'s Total = {self.total}"

    def turn(self):
        """
        Play one turn

        :return:
        """
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != "h":
            die = throw_the_die()
            if die == 1:
                # scratch - let the user know!
                break

            turn_total += die
            # Print some information to the user. My recommendation is to:
            # print turn_total,
            # print possible total if I hold, total + turn_total
            # print real total
            roll_hold = input("Roll(r) or Hold(h)? ").lower()

        if roll_hold == 'h':
            # update the player's total
            self.total += turn_total

        self.show()


class ComputerPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def turn(self):
        """
        Computer player turn
        :return:
        """
        turn_total = 0
        scratch = False
        while turn_total >= min(self.total, 100 - self.total):
            die = throw_the_die()
            if die == 1:
                # scratch - let the user know!
                scratch = True
                break

            turn_total += die
            # Print some information to the user. My recommendation is to:
            # print turn_total,
            # print possible total if I hold, total + turn_total
            # print real total
            roll_hold = input("Roll(r) or Hold(h)? ").lower()

        if not scratch:
            # update the player's total
            self.total += turn_total

        self.show()


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):
        """
        Returns true if there is winner
        :return:
        """
        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

        return False

    def play_game(self):
        current_player = self.players[0]
        while not self.check_winner():
            # play the game
            current_player.turn()
            # change current_player to the next player

        # show the winner


class TimedGame(Game):

    def __init__(self, player1, player2, time_limit):
        super().__init__(player1, player2)
        self.start_time = datetime.datetime.now()
        self.time_limit = time_limit

    def check_time(self, time_now):
        """
        Check for the time
        :return: True if time expired
        """
        return (time_now - self.start_time).total_seconds() > self.time_limit

    def play_game(self):
        current_player = self.players[0]
        time_flag = False
        while not self.check_winner() or not time_flag:
            # play the game
            current_player.turn()
            # change current_player to the next player

            time_flag = self.check_time(datetime.datetime.now())

        # check if game end because of time
        # show the winner


def make_player(player_type, player_name):
    """
    Factory function

    :param player_type:
    :param player_name:
    :return:
    """
    if player_type.upper() == 'C':
        return ComputerPlayer(player_name)
    elif player_type.upper() == 'H':
        return Player(player_name)
    else:
        raise ValueError("I don't know what to build!!!!")


if __name__ == '__main__':
    p1 = make_player('h', "John")
    p2 = make_player('c', "HAL")

    pig_game = Game(p1, p2)
    pig_game.play_game()

