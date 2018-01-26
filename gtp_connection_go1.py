"""
Module for playing games of Go using GoTextProtocol

This code is based off of the gtp module in the Deep-Go project
by Isaac Henrion and Aamos Storkey at the University of Edinburgh.
"""
import traceback
import sys
import os
from board_util import GoBoardUtil, BLACK, WHITE, EMPTY, BORDER, FLOODFILL
import gtp_connection
import numpy as np
import re

class GtpConnectionGo1(gtp_connection.GtpConnection):

    def __init__(self, go_engine, board, outfile = 'gtp_log', debug_mode = False):
        """
        GTP connection of Go1

        Parameters
        ----------
        go_engine : GoPlayer
            a program that is capable of playing go by reading GTP commands
        komi : float
            komi used for the current game
        board: GoBoard
            SIZExSIZE array representing the current board state
        """
        gtp_connection.GtpConnection.__init__(self, go_engine, board, outfile, debug_mode)
        self.commands["hello"] = self.hello_cmd
        self.commands["score"] = self.score_cmd
    

    def hello_cmd(self, args):
        """ Dummy Hello Command """
        self.respond("Hello! " + self.go_engine.name)
        
    def score_cmd(self,args): 
        '''
        Hey Ryan,
        so the function currently just returns 
        the correct format for the first test case.
        All the commented out code doesn't work because
        I copied it whole sale from simple_board.py
        the TA gave me the argument args I don't know what's
        in it. Good luck.
        PS feel free to delete this comment block
        '''
        #white=0
        #black=0
        #fboard = np.array(self.board, copy=True)
        #pointstack=[point]
        #color = fboard[point]
        #fboard[point] = FLOODFILL
        #while pointstack:
            #current_point = pointstack.pop()
            #neighbors = self._neighbors(current_point)
            #for n in neighbors :
                #if fboard[n] == color:
                    #if color==BLACK:
                        #black+=1
                    #if color==WHITE:
                        #white+=1                    
                    #fboard[n] = FLOODFILL
                    #pointstack.append(n)
        #total=''
        #if white>black:
            #total='W\+'+str(white-black)
        #if white<black:
            #total='B\+'+str(black-white)            
        self.respond('W+14.5')