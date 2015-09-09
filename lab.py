
from room import MlRoom, UNLOCK_RETURN_CODES


class MlLab( object ):
    def __init__( self ):
        self._rooms_dict    = dict()
        self._entrance      = None
        self._exit          = None
        self._current       = None


    @property
    def character_at_exit( self ):
        return self._current == self._exit


    @property
    def current_room( self ):
        return self._rooms_dict[ self._current ]


    def TryUnlockSomething( self, balls ):
        success_string  = "You've unlocked %s, GODDAMNIT!"
        curse_string    = "You don't have enough balls, dickhead!"

        for direction in self.current_room.directions:
            target_room = self.current_room.GetDirection( direction )

            if target_room.Unlock( balls ) == UNLOCK_RETURN_CODES.SUCCESSFULLY_UNLOCKED:
                print( success_string % direction )
                return
            elif target_room.Unlock( balls ) == UNLOCK_RETURN_CODES.NOT_ENOUGH_BALLS:
                print( curse_string )
                return

        print( "There is nothing to unlock, you idiot!" )


    def AddRoom( self, room ):
        assert type( room ) == MlRoom
        self._rooms_dict[ room.pk ] = room


    def SetEntrance( self, room_pk ):
        if room_pk in self._rooms_dict:
            self._entrance  = room_pk
            self._current   = room_pk
        else:
            raise Exception( "There is no such room" )


    def SetExit( self, room_pk ):
        if room_pk in self._rooms_dict:
            self._exit = room_pk
        else:
            raise Exception( "There is no such room" )


    def CanMoveDirection( self, direction ):
        return self.current_room.GetDirection( direction ) is not None


    def MoveInDirection( self, direction ):
        target_room = self.current_room.GetDirection( direction )
        if target_room.locked:
            print( "Fuck! This way is locked." )
        else:
            self._current = target_room.pk
            print( "You move to:" )
            self.current_room.description
