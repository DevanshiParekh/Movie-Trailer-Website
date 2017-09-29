# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:46:09 2017

@author: Devanshi
"""
import webbrowser

class Movie():
    def __init__(self,titles,storyline,poster,trailer):
        self.title = titles
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer
        
    def getTrailer(self):
        webbrowser.open(self.trailer)
        