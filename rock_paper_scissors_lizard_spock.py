
from random import randint

from room   import MlStruct


CHOICES             = MlStruct()

CHOICES.ROCK        = 0
CHOICES.PAPER       = 1
CHOICES.SCISSORS    = 2
CHOICES.LIZARD      = 3
CHOICES.SPOCK       = 4


class MlRockPaperScissorsLizardSpock( object ):
    def __init__( self ):
        self._player_won = 0
        self._guard_won = 0
        self._draws = 0
        self._round = 1
        self._wins_to_total_wictory = 4


    @property
    def game_is_over( self ):
        return self._player_won == self._wins_to_total_wictory or self._guard_won == self._wins_to_total_wictory


    def _PlayerWins( self ):
        self._player_won += 1


    def _GuardWins( self ):
        self._guard_won += 1


    def _PlayDraw( self ):
        self._draws += 1


    def _Compare( self, player, guard ):
        # Bruteforced solution. Probably, I should look for better.

        victory_string  = "You win."
        defeat_string   = "Guard wins."
        draw_string     = "You and Guard groan in frustration."
        gp_string       = "Guard plays "

        if player == CHOICES.ROCK:
            print( "You play Rock." )
            if guard == CHOICES.ROCK:
                print( gp_string + "Rock." )
                print( draw_string )
                self._PlayDraw()
            elif guard == CHOICES.PAPER:
                print( gp_string + "Paper.")
                print( "Guard's Paper covers your Rock." )
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.SCISSORS:
                print( gp_string + "Scissors." )
                print( "Your Rock crushes Guard's Scissors.")
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.LIZARD:
                print( gp_string + "Lizard." )
                print( "Your Rock crushes Guard's Lizard." )
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.SPOCK:
                print( gp_string + "Spock." )
                print( "Guard's Spock vaporizes your Rock." )
                print( defeat_string )
                self._GuardWins()
        elif player == CHOICES.PAPER:
            print( "You play Paper." )
            if guard == CHOICES.ROCK:
                print( gp_string + "Rock." )
                print( "Your Paper covers Guard's Rock." )
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.PAPER:
                print( gp_string + "Paper." )
                print( draw_string )
                self._PlayDraw()
            elif guard == CHOICES.SCISSORS:
                print( gp_string + "Scissors." )
                print( "Guard's Scissors cuts your Paper." )
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.LIZARD:
                print( gp_string + "Lizard." )
                print( "Guard's Lizard eats your Paper." )
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.SPOCK:
                print( gp_string + "Spock." )
                print( "Your Paper disproves Guard's Spock" )
                print( victory_string )
                self._PlayerWins()
        elif player == CHOICES.SCISSORS:
            print( "You play Scissors." )
            if guard == CHOICES.ROCK:
                print( gp_string + "Rock." )
                print( "Guard's Rock crushes your Scissors." )
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.PAPER:
                print( gp_string + "Paper." )
                print( "Your Scissors cuts Guard's Paper." )
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.SCISSORS:
                print( gp_string + "Scissors." )
                print( draw_string )
                self._PlayDraw()
            elif guard == CHOICES.LIZARD:
                print( gp_string + "Lizard." )
                print( "Your Scissors decapitates Guard's Lizard." )
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.SPOCK:
                print( gp_string + "Spock." )
                print( "Guard's Spock smashes your Scissors." )
                print( defeat_string )
                self._GuardWins()
        elif player == CHOICES.LIZARD:
            print( "You play Lizard." )
            if guard == CHOICES.ROCK:
                print( gp_string + "Rock." )
                print( "Guard's Rock crushes your Lizard." )
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.PAPER:
                print( gp_string + "Paper." )
                print( "Your Lizard eats Guard's Paper." )
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.SCISSORS:
                print( gp_string + "Scissors." )
                print( "Guard's Scissors decapitates Your Lizard.")
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.LIZARD:
                print( gp_string + "Lizard." )
                print( draw_string )
                self._PlayDraw()
            elif guard == CHOICES.SPOCK:
                print( gp_string + "Spock." )
                print( "Your Lizard poisons Guard's Spock." )
                print( victory_string )
                self._PlayerWins()
        elif player == CHOICES.SPOCK:
            print( "You play Spock." )
            if guard == CHOICES.ROCK:
                print( gp_string + "Rock." )
                print( "Your Spock vaporizes Guard's Rock." )
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.PAPER:
                print( gp_string + "Paper." )
                print( "Guard's Paper disproves your Spock." )
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.SCISSORS:
                print( gp_string + "Scissors." )
                print( "Your Spock smashes Guard's Scissors.")
                print( victory_string )
                self._PlayerWins()
            elif guard == CHOICES.LIZARD:
                print( gp_string + "Lizard." )
                print( "Guard's Lizard poisons your Spock." )
                print( defeat_string )
                self._GuardWins()
            elif guard == CHOICES.SPOCK:
                print( gp_string + "Spock." )
                print( draw_string )
                self._PlayDraw()
        else:
            Exception( "It's just impossible!" )


    def _GetPlayerInput( self ):
        ch = str( input( ">" ) )
        if ch.lower() == "rock":
            return CHOICES.ROCK
        elif ch.lower() == "paper":
            return CHOICES.PAPER
        elif ch.lower() == "scissors":
            return CHOICES.SCISSORS
        elif ch.lower() == "lizard":
            return CHOICES.LIZARD
        elif ch.lower() == "spock":
            return CHOICES.SPOCK
        elif ch.lower() == "p":
            self._PrintScore()
        elif ch.lower() == "q" or ch.lower() == "quit":
            print( "You gave up and now Guard will kill you." )
            print( "Good luck in the next life.\n" )
            return False
        else:
            print( "Try again." )


    def _PrintScore( self ):
        if self._player_won == self._guard_won:
            print( "The game is tied %d:%d" % ( self._player_won, self._player_won ) )
        elif self._player_won > self._guard_won:
            print( "You lead %d:%d" % ( self._player_won, self._guard_won ) )
        elif self._player_won < self._guard_won:
            print( "Guard leads %d:%d" % ( self._guard_won, self._player_won ) )
        else:
            Exception( "It's just impossible!" )


    def Run( self ):
        print( "You open the door and suddenly see the Guard and the Guard have a fucking gun.\n" )
        print( "\"You aren't suposed to be here.\", said the Guard with acid in his voice.\n" )
        print( "\"And so?\" you asked.\n" )
        print( "\"So I should kill you!\" - the Guard was already preparing to shoot you.\n" )
        print( "\"Wait!\" - shouted you. \"Let's play a game. If I win, you'll release me." )
        print( "If you win, well, you'll kill me\"\n" )
        print( "\"What fucking game?\" - the Guard was smiling viciously.\n" )
        print( "\"Rock-Paper-Scissors-Lizard-Spock\"\n" )
        print( "\"What the fuck?\" - the Guard was really surprised.\n" )
        print( "\"It's very simple. Look -- Scissors cuts Paper, Paper covers Rock." )
        print( "Rock crushes Lizard, Lizard poisons Spock. Spock smashes Scissors," )
        print( "Scissors decapitates Lizard. Lizard eats Paper, Paper disproves Spock," )
        print( "Spock vaporizes rock, and as it always has, Rock crushes Scissors.\"\n" )
        print( "\"Okay. I think I got it.\" -- said the Guard.\n" )
        print( "Gosh! It will be the hardest battle you ever fourght.\n")

        while not self.game_is_over:
            print( "\nRound %d" % self._round )
            player_choice = self._GetPlayerInput()
            if player_choice is None:
                continue
            elif player_choice is False:
                return False
            else:
                self._round += 1
                self._Compare( player_choice, randint( 0, 4 ) )

        if self._player_won > self._guard_won:
            print( "\nIn a long and exausting battle you defeat wicked guard!" )
            return True
        else:
            print( "\nYou loose and now guard will kill you!" )
            return False
