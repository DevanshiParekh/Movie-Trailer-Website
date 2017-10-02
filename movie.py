# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:46:09 2017

@author: Devanshi
"""
import webbrowser


class Movie():
    def __init__(self, titles, storyline, poster, trailer):
        """
        This constructor allows users to assign the title, storyline,
        poster url and trailer url for respective movie instance.
        """
        self.title = titles
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def getTrailer(self):
        """
        This method allows user to open the trailer in the webbrowser.
        """
        webbrowser.open(self.trailer)
