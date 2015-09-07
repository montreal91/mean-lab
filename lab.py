
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


    def _UnlockNorth( self, balls ):
        return self.current_room.north.Unlock( balls )


    def _UnlockSouth( self, balls ):
        return self.current_room.south.Unlock( balls )


    def _UnlockWest( self, balls ):
        return self.current_room.west.Unlock( balls )


    def _UnlockEast( self, balls ):
        return self.current_room.east.Unlock( balls )


    def TryUnlockSomething( self, balls ):
        success_string = "You've unlocked %s, GODDAMNIT!"
        curse_string = "You don't have enough balls, dickhead!"
        if self._UnlockNorth( balls ) == UNLOCK_RETURN_CODES.SUCCESSFULLY_UNLOCKED:
            print( success_string % "North" )
            return
        if self._UnlockNorth( balls ) == UNLOCK_RETURN_CODES.NOT_ENOUGH_BALLS:
            print( curse_string )
            return
        if self._UnlockEast( balls ) == UNLOCK_RETURN_CODES.SUCCESSFULLY_UNLOCKED:
            print( success_string % "East" )
            return
        if self._UnlockEast( balls ) == UNLOCK_RETURN_CODES.NOT_ENOUGH_BALLS:
            print( curse_string )
            return
        if self._UnlockSouth( balls ) == UNLOCK_RETURN_CODES.SUCCESSFULLY_UNLOCKED:
            print( success_string % "South" )
            return
        if self._UnlockSouth( balls ) == UNLOCK_RETURN_CODES.NOT_ENOUGH_BALLS:
            print( curse_string )
            return
        if self._UnlockWest( balls ) == UNLOCK_RETURN_CODES.SUCCESSFULLY_UNLOCKED:
            print( success_string % "West" )
            return
        if self._UnlockWest( balls ) == UNLOCK_RETURN_CODES.NOT_ENOUGH_BALLS:
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


    def CanMoveNorth( self ):
        return self.current_room.north is not None


    def CanMoveSouth( self ):
        return self.current_room.south is not None


    def CanMoveWest( self ):
        return self.current_room.west is not None


    def CanMoveEast( self ):
        return self.current_room.east is not None


    def MoveNorth( self ):
        if self.current_room.north.locked:
            print( "Fuck! This way is locked." )
        else:
            self._current = self.current_room.north.pk
            print( "You move to:" )
            self.current_room.description


    def MoveSouth( self ):
        if self.current_room.south.locked:
            print( "Fuck! This way is locked." )
        else:
            self._current = self.current_room.south.pk
            print( "You move to:" )
            self.current_room.description


    def MoveWest( self ):
        if self.current_room.west.locked:
            print( "Fuck! This way is locked." )
        else:
            self._current = self.current_room.west.pk
            print( "You move to:" )
            self.current_room.description


    def MoveEast( self ):
        if self.current_room.east.locked:
            print( "Fuck! This way is locked." )
        else:
            self._current = self.current_room.east.pk
            print( "You move to:" )
            self.current_room.description
