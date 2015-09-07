
from room import MlRoom


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
        return self._rooms_dict[ self._current ].north


    def CanMoveSouth( self ):
        return self._rooms_dict[ self._current ].south


    def CanMoveWest( self ):
        return self._rooms_dict[ self._current ].west


    def CanMoveEast( self ):
        return self._rooms_dict[ self._current ].east


    def MoveNorth( self ):
        self._current = self._rooms_dict[ self._current ].north
        print( "You move to:" )
        self._rooms_dict[ self._current ].description


    def MoveSouth( self ):
        self._current = self._rooms_dict[ self._current ].south
        print( "You move to:" )
        self._rooms_dict[ self._current ].description


    def MoveWest( self ):
        self._current = self._rooms_dict[ self._current ].west
        print( "You move to:" )
        self._rooms_dict[ self._current ].description


    def MoveEast( self ):
        self._current = self._rooms_dict[ self._current ].east
        print( "You move to:" )
        self._rooms_dict[ self._current ].description
