
from random import random


class MlCharacter( object ):
    def __init__( self ):
        self._balls             = 0
        self._coins             = 0
        self._crap              = 0

        self._find_ball_chance  = 1.00
        self._find_coin_chance  = 1.25


    @property
    def balls( self ):
        return self._balls


    @property
    def coins( self ):
        return self._coins


    @property
    def crap( self ):
        return self._crap


    def _LoadedToss( self, chance ):
        return random() < chance


    def LookForBall( self, mess ):
        if mess == 0:
            chance = self._find_ball_chance + 0.1
        else:
            chance = self._find_ball_chance / mess

        return self._LoadedToss( chance )


    def LookForCoin( self, mess ):
        if mess == 0:
            chance = self._find_coin_chance + 0.05
        else:
            chance = self._find_coin_chance / mess
        return self._LoadedToss( chance )


    def FindBall( self ):
        self._balls += 1


    def FindCoin( self ):
        self._coins += 1


    def FindCrap( self ):
        self._crap += 1
