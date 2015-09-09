
class MlStruct:
    pass


UNLOCK_RETURN_CODES = MlStruct()

UNLOCK_RETURN_CODES.ALREADY_UNLOCKED        = 0
UNLOCK_RETURN_CODES.SUCCESSFULLY_UNLOCKED   = 1
UNLOCK_RETURN_CODES.NOT_ENOUGH_BALLS        = 2


class MlRoom( object ):
    def __init__( self, pk, description, mess=0, coins=0, balls=0, locked=False ):
        self._pk                = pk
        self._description       = description
        self._direction_dict    = dict()
        self._coins             = coins
        self._balls             = balls
        self._locked            = locked
        
        if mess < 0:
            self._mess = 0
        elif mess > 4:
            self._mess = 4
        else:
            self._mess = mess

        self._DescribeMess()


    @property
    def pk( self ):
        return self._pk


    @property
    def description( self ):
        print( self._description )


    @property
    def mess( self ):
        return self._mess


    @property
    def coins( self ):
        return self._coins


    @property
    def balls( self ):
        return self._balls


    @property
    def directions( self ):
        return [ key for key in self._direction_dict ]
    


    def SetDirection( self, direction, room ):
        assert isinstance( room, MlRoom )
        self._direction_dict[ direction ] = room


    def GetDirection( self, direction ):
        if direction in self._direction_dict:
            return self._direction_dict[ direction ]
        else:
            return None


    @property
    def locked( self ):
        return self._locked


    def _DescribeMess( self ):
        if self._mess == 0:
            self._description += "\nThis room is clean."
        elif self._mess == 1:
            self._description += "\nThis room is a bit messy."
        elif self._mess == 2:
            self._description += "\nThis room is messy."
        elif self._mess == 3:
            self._description += "\nThis room is very messy."
        elif self._mess == 4:
            self._description += "\nThis room is such a mess. You can barely moove here."


    def ExtractBall( self ):
        if self._balls > 0:
            self._balls -= 1
        else:
            pass


    def ExtractCoin( self ):
        if self._coins > 0:
            self._coins -= 1
        else:
            pass


    def Unlock( self, balls ):
        if balls > 2 and self._locked:
            self._locked = False
            return UNLOCK_RETURN_CODES.SUCCESSFULLY_UNLOCKED
        elif balls < 2 and self._locked:
            return UNLOCK_RETURN_CODES.NOT_ENOUGH_BALLS
        else:
            return UNLOCK_RETURN_CODES.ALREADY_UNLOCKED
