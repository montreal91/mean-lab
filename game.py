
import sys

from random                             import randint

from character                          import MlCharacter
from lab                                import MlLab
from rock_paper_scissors_lizard_spock   import MlRockPaperScissorsLizardSpock
from room                               import MlRoom, MlStruct

DIRECTIONS          = MlStruct()

DIRECTIONS.NORTH    = "North"
DIRECTIONS.EAST     = "East"
DIRECTIONS.SOUTH    = "South"
DIRECTIONS.WEST     = "West"


class MlGame( object ):
    def __init__( self ):
        self._lab       = MlLab()
        self._character = MlCharacter()

        self._CreateLabRooms()


    def __GetRandomDigits( self, amount ):
        if amount > 10:
            amount = 10
        res = set()
        while len( res ) < amount:
            res.add( randint( 1, 9 ) )
        return res

    def _ProcessInput( self ):
        try:
            ch = str( input( ">" ) )
            if ch == "n" and self._lab.CanMoveDirection( DIRECTIONS.NORTH ):
                self._lab.MoveInDirection( DIRECTIONS.NORTH )
            elif ch == "s" and self._lab.CanMoveDirection( DIRECTIONS.SOUTH ):
                self._lab.MoveInDirection( DIRECTIONS.SOUTH )
            elif ch == "w" and self._lab.CanMoveDirection( DIRECTIONS.WEST ):
                self._lab.MoveInDirection( DIRECTIONS.WEST )
            elif ch == "e" and self._lab.CanMoveDirection( DIRECTIONS.EAST ):
                self._lab.MoveInDirection( DIRECTIONS.EAST )
            elif ch == "can":
                self._PrintListOfPossibilities()
            elif ch == "i":
                self._PrintListOfItemsInInventory()
            elif ch == "l":
                self._LookForSomething()
            elif ch == "u":
                self._lab.TryUnlockSomething( self._character.balls )
            else:
                print( "WTF?" )
        except KeyboardInterrupt:
            print( "\nGiving up?" )
            print( "You suck!\n" )
            sys.exit()


    def _PrintListOfPossibilities( self ):
        print( "You can look for some crap." )
        print( "You can look into your inventory." )
        print( "You can move to:" )
        if self._lab.CanMoveDirection( DIRECTIONS.NORTH ):
            print( "\t%s." % DIRECTIONS.NORTH )
        if self._lab.CanMoveDirection( DIRECTIONS.SOUTH ):
            print( "\t%s." % DIRECTIONS.SOUTH )
        if self._lab.CanMoveDirection( DIRECTIONS.WEST ):
            print( "\t%s." % DIRECTIONS.WEST )
        if self._lab.CanMoveDirection( DIRECTIONS.EAST ):
            print( "\t%s." % DIRECTIONS.EAST )
        print( "Or you can fuck yourself right here." )


    def _PrintListOfItemsInInventory( self ):
        print( "You have %d fucking balls." % self._character.balls )
        print( "You have %d fucking coins." % self._character.coins )
        print( "You have %d pieces of crap in your pocket." % self._character.crap )


    def _CreateLabRooms( self ):
        room_list   = list()
        balls       = self.__GetRandomDigits( 3 )
        for i in range( 1, 10 ):
            if i in balls:
                room = MlRoom(
                    i * 10, 
                    "Lab Room %s" % i, 
                    mess=randint( 0, 4 ), 
                    balls=1,
                    coins=randint( 0, 2 )
                )
            else:
                room = MlRoom(
                    i * 10,
                    "Lab Room %s" % i,
                    mess=randint( 0, 4 ), 
                    coins=randint( 0, 2 )
                )
            room_list.append( room )

        room_list[ 0 ].SetDirection( DIRECTIONS.NORTH, room_list[ 3 ] )
        room_list[ 0 ].SetDirection( DIRECTIONS.EAST, room_list[ 1 ] )

        room_list[ 1 ].SetDirection( DIRECTIONS.NORTH, room_list[ 4 ] )
        room_list[ 1 ].SetDirection( DIRECTIONS.WEST, room_list[ 0 ] )

        room_list[ 2 ].SetDirection( DIRECTIONS.NORTH, room_list[ 5 ] )

        room_list[ 3 ].SetDirection( DIRECTIONS.EAST, room_list[ 4 ] )
        room_list[ 3 ].SetDirection( DIRECTIONS.SOUTH, room_list[ 0 ] )

        room_list[ 4 ].SetDirection( DIRECTIONS.EAST, room_list[ 5 ] )
        room_list[ 4 ].SetDirection( DIRECTIONS.SOUTH, room_list[ 1 ] )
        room_list[ 4 ].SetDirection( DIRECTIONS.WEST, room_list[ 3 ] )

        room_list[ 5 ].SetDirection( DIRECTIONS.NORTH, room_list[ 8 ] )
        room_list[ 5 ].SetDirection( DIRECTIONS.SOUTH, room_list[ 2 ] )
        room_list[ 5 ].SetDirection( DIRECTIONS.WEST, room_list[ 4 ] )

        room_list[ 6 ].SetDirection( DIRECTIONS.EAST, room_list[ 7 ] )

        room_list[ 7 ].SetDirection( DIRECTIONS.EAST, room_list[ 8 ] )
        room_list[ 7 ].SetDirection( DIRECTIONS.WEST, room_list[ 6 ] )

        room_list[ 8 ].SetDirection( DIRECTIONS.SOUTH, room_list[ 5 ] )
        room_list[ 8 ].SetDirection( DIRECTIONS.WEST, room_list[ 7 ] )

        entrance                = MlRoom( 11, "Entrance" )
        exit                    = MlRoom( 22, "Exit", locked=True )

        entrance.SetDirection( DIRECTIONS.NORTH, room_list[ 1 ] )
        room_list[ 1 ].SetDirection( DIRECTIONS.SOUTH, entrance )

        exit.SetDirection( DIRECTIONS.SOUTH, room_list[ 7 ] )
        room_list[ 7 ].SetDirection( DIRECTIONS.NORTH, exit )
        
        self._lab.AddRoom( entrance )
        self._lab.AddRoom( exit )

        for room in room_list:
            self._lab.AddRoom( room )

        self._lab.SetEntrance( entrance.pk )
        self._lab.SetExit( exit.pk )


    def _FindBallCondition( self ):
        ball = self._character.LookForBall( self._lab.current_room.mess )
        return ball and self._lab.current_room.balls > 0


    def _FindCoinCondition( self ):
        coin = self._character.LookForCoin( self._lab.current_room.mess )
        return coin and self._lab.current_room.coins > 0
               

    def _LookForSomething( self ):
        if self._FindBallCondition():
            self._character.FindBall()
            self._lab.current_room.ExtractBall()
            print( "You've found a fucking ball!" )
            return
        if self._FindCoinCondition():
            self._character.FindCoin()
            self._lab.current_room.ExtractCoin()
            print( "You've found a fucking coin!" )
            return

        self._character.FindCrap()
        print( "You've found a piece of crap. Congratulations!" )


    def Run( self ):
        print( "\nYou are standing before the lab and you can't go back." )
        print( "The only way is through the lab." )
        print( "Unfortunately, the lab is mean and will curse you." )
        print( "\nPrint 'n' to go north." )
        print( "Print 's' to go south." )
        print( "Print 'w' to go west." )
        print( "Print 'e' to go east." )
        print( "Print 'l' to look for something." )
        print( "Print 'i' to look into your inventory." )
        print( "Print 'can' if you don't know what to do." )
        print( "Press [Ctrl + C] to quit.\n" )
        while not self._lab.character_at_exit:
            self._ProcessInput()
        final_battle = MlRockPaperScissorsLizardSpock()
        result = final_battle.Run()
        if result is True:
            print( "\nCongratulations!" )
            print( "You've managed to find your fucking way through the mean lab." )
            print( "Now you can fuck yourself wherever you want!\n" )
        else:
            print( "\nUnfortunately, you haven't managed to find your fucking way through the mean lab" )
            print( "and now you will not fuck yourself wherever you want." )
            print( "Because you are as dead as Aphrodite's cunt!\n" )


if __name__ == '__main__':
    game = MlGame()
    game.Run()
