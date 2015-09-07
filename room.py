
class MlRoom( object ):
    def __init__( self, pk, description, mess=0, coins=0, balls=0 ):
        self._pk            = pk
        self._description   = description
        self._north         = None
        self._south         = None
        self._west          = None
        self._east          = None
        self._coins         = coins
        self._balls         = balls
        
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
    def north( self ):
        if self._north:
            return self._north.pk
        else:
            return None


    @north.setter
    def north( self, direction ):
        assert type( direction ) == MlRoom
        self._north = direction


    @property
    def south( self ):
        if self._south:
            return self._south.pk
        else:
            return None


    @south.setter
    def south( self, direction ):
        assert type( direction ) == MlRoom
        self._south = direction


    @property
    def west( self ):
        if self._west:
            return self._west.pk
        else:
            return None


    @west.setter
    def west( self, direction ):
        assert type( direction ) == MlRoom
        self._west = direction


    @property
    def east( self ):
        if self._east:
            return self._east.pk
        else:
            return None


    @east.setter
    def east( self, direction ):
        assert type( direction ) == MlRoom
        self._east = direction


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
