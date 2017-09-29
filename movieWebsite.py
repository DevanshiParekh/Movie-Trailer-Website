# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:48:02 2017

@author: Devanshi
"""
import fresh_tomatoes
import movie

it = movie.Movie("It","A group of bullied kids band together when a shapeshifting demon, taking the appearance of a clown, begins hunting children.","http://cdn2.enelbreak.com/espectaculos/wp-content/uploads/2017/03/It-El-Payaso-Asesino-2017-poster.jpg",
                       "https://www.youtube.com/watch?v=7no56Zw1e20")

mother = movie.Movie("Mother","A couple's relationship is tested when uninvited guests arrive at their home, disrupting their tranquil existence.","http://ksassets.timeincuk.net/wp/uploads/sites/55/2017/05/Mother-920x584.jpg",
                       "https://www.youtube.com/watch?v=XpICoc65uh0")

kingsman = movie.Movie("Kingsman: The Golden Circle ","When their headquarters are destroyed and the world is held hostage, the Kingsman's journey leads them to the discovery of an allied spy organization in the US. These two elite secret organizations must band together to defeat a common enemy.","http://cdn1-www.comingsoon.net/assets/uploads/2017/08/kingsmanheader.jpg",
                       "https://www.youtube.com/watch?v=4PggfbzJcvA")

movies = [it,mother,kingsman]

fresh_tomatoes.open_movies_page(movies)