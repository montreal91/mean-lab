
import sys

from random     import randint

from character  import MlCharacter
from lab        import MlLab
from room       import MlRoom


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
            if ch == "n" and self._lab.CanMoveNorth():
                self._lab.MoveNorth()
            elif ch == "s" and self._lab.CanMoveSouth():
                self._lab.MoveSouth()
            elif ch == "w" and self._lab.CanMoveWest():
                self._lab.MoveWest()
            elif ch == "e" and self._lab.CanMoveEast():
                self._lab.MoveEast()
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
        if self._lab.CanMoveNorth():
            print( "\tNorth." )
        if self._lab.CanMoveSouth():
            print( "\tSouth." )
        if self._lab.CanMoveWest():
            print( "\tWest." )
        if self._lab.CanMoveEast():
            print( "\tEast." )
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

        room_list[ 0 ].north    = room_list[ 3 ]
        room_list[ 0 ].east     = room_list[ 1 ]

        room_list[ 1 ].north    = room_list[ 4 ]
        room_list[ 1 ].west     = room_list[ 0 ]

        room_list[ 2 ].north    = room_list[ 5 ]

        room_list[ 3 ].east     = room_list[ 4 ]
        room_list[ 3 ].south    = room_list[ 0 ]

        room_list[ 4 ].east     = room_list[ 5 ]
        room_list[ 4 ].south    = room_list[ 1 ]
        room_list[ 4 ].west     = room_list[ 3 ]

        room_list[ 5 ].north    = room_list[ 8 ]
        room_list[ 5 ].south    = room_list[ 2 ]
        room_list[ 5 ].west     = room_list[ 4 ]

        room_list[ 6 ].east     = room_list[ 7 ]

        room_list[ 7 ].east     = room_list[ 8 ]
        room_list[ 7 ].west     = room_list[ 6 ]

        room_list[ 8 ].south    = room_list[ 5 ]
        room_list[ 8 ].west     = room_list[ 7 ]

        entrance                = MlRoom( 11, "Entrance" )
        exit                    = MlRoom( 22, "Exit", locked=True )

        entrance.north          = room_list[ 1 ]
        room_list[ 1 ].south    = entrance

        exit.south              = room_list[ 7 ]
        room_list[ 7 ].north    = exit
        
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
        print( "\nCongratulations!" )
        print( "You've managed to find your fucking way through the mean lab." )
        print( "Now you can fuck yourself wherever you want!\n" )


if __name__ == '__main__':
    game = MlGame()
    game.Run()
