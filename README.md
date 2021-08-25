# Learning-Kivy
A repo designed for learning and maintaining knowledge in the kiwy library for Python. Kivy is a library that is used to develop for instance mobile applications. Much like the library pygame one can use it to write games as well (See pygame repo). For video demonstrations of the projects below, click this link: 

https://www.youtube.com/playlist?list=PL3iOX_va0_Lg-aulnxieobxkOMDchif32

# Project Information
## text_game.py (Blueberries)
This is my first kivy project, a small text game where the player plays by pressing different buttons. The goal of the game is to avoid the bear and to collect the blueberries. It is simple in nature consisting of one python file extended via kivy. The entire game is controlled by which state it is in, an update function updates all the buttons and scenario text in accordance with the state. The player can change the state by pressing different buttons, and so it is like a graph in which the player can traverse to different nodes where each node is a game state. One state is a losing state and one state is a winning state. [Pictures!](#text_gamepy)

## kivy_calculator.py
A simple application where the user inputs two numbers a,b and gets an answer based on what operation the user wants to perform. Some error handling is done to make sure that the user inputs integers, and not something else, as well as to avoid division with zero. A standard calculator. [Pictures!](#kivy_calculatorpy-1)

## tic_tac_toe.py
An application of a classic tic-tac-toe game with a red and blue player. The object of the game is to get 3 in a row, diagonally, horisontally or vertically. The first player to achieve this wins in this game where player takes turn to put their markers on a 3x3 board. [Pictures!](#tic_tac_toepy-1)

## tic_tac_toe_3D.py (TODO)
An extension of the normal tic_tac_toe game into 3D-space. The dimensions will be, for this game, 3x3x3 and it is as if you are dropping down a marker in the z-axis. This means that you cannot start with the play (1,1,2) for instance, even though it is an ok square, (1,1,1) and (1,1,0) first has to be taken. We think of it as stones being stacked upon each other. The check becomes more difficult simply because there is inclinational cases to take care of in this, more exciting, version of tic-tac-toe.

## Memory.py
An implementation of a typical memory. Match the squares together in this game and remember where they were. The idea for this game is to initiate a 5x6 grid layout, totaling a size of 30 cards. Every card will be an object where two cards are the same and they will be initiated in a deck. We will then use the Fisher-Yates shuffling algorithm to shuffle the deck around, to then finally distribute them opon the grid. Each card is itself displayed as a layout with one button, where the button is the backside of the card, and upon clicking the button that specific layout will clear its widgets and instead display an image corrosponding to the link of the card object. 

## learner.py (a flash card application I use for learning Italian at the moment:) )
An application much like a flash card learner where a user can add a text and associate that with an answer to then be drilled on those. There is also added functionality so the user can load in previous flashcards, from a textfile. To insert text into a file that is to be loaded in one should start with the name of the flashcard deck, maybe "Italian 1", and then seperate every card with a semicolon (;) and every front/back side with a binding mark (-), ending the final word with a dot, for instance: Italian; yes-si; thank you-grazie. In this way the user can load in previous flashcard decks but I also want to make it so we can save our current deck of flashcards to that file, this is a TODO.

## Fun_With_Sorting_Algorithms (TODO)
A game where the user will get different animations of sorting algorithms and the goal is to correctly guess the sorting algorithm. This is meant to be a fun gameified learning experience to repeat, or familiarize oneself with the different sorting algorithms one can come across. 

## Mobile Approximater (TODO)
An application that takes in a function and calculates things like extreme values, derivations and/or integrals using numerical methods. The idea is to merge some ideas from Numerical Methods with the Kivy framework to make a calculator designed specifically for approximating such things. With that one can use such a tool when working calculus problems and be reasonably sure to have the correct answer if the approximation is the same as that analytical answer. 

# Images
## text_game.py
<img src="https://user-images.githubusercontent.com/70810124/128862428-69ed0d4f-3f33-49e7-9226-b5b964f77dcc.png" width = "400" height = "300" />
<img src="https://user-images.githubusercontent.com/70810124/128862457-9399dc3a-2fe5-466e-bf64-4de1aa162c34.png" width = "400" height = "300" />


## kivy_calculator.py
<img src="https://user-images.githubusercontent.com/70810124/128889661-2a4b6685-ddae-4c01-86de-9fb4994e75fc.png" width = "400" height = "300" />
<img src="https://user-images.githubusercontent.com/70810124/128889665-b14157c4-8c21-4a41-b5e4-4bede05cfb0e.png" width = "400" height = "300" />

## tic_tac_toe.py
<img src ="https://user-images.githubusercontent.com/70810124/129105178-9f8598c8-587d-450e-87d8-44af13193234.png" width = "400" height = "300" />
<img src ="https://user-images.githubusercontent.com/70810124/129105184-d8a6f964-4a20-4b9f-a2d1-8326e3485df6.png" width = "400" height = "300" />

## memory.py
<img src = "https://user-images.githubusercontent.com/70810124/130773149-cf59e162-21ab-4bc5-91f7-f112c3e143b6.png" width = "400" height = "300" />
<img src = "https://user-images.githubusercontent.com/70810124/130773243-2c5f8ff5-31d4-462a-adc4-fe03ea33a545.png" width = "400" height = "300" />
<img src = "https://user-images.githubusercontent.com/70810124/130773251-cebe116c-2af3-497e-9b73-9b3dde462bf0.png" width = "400" height = "300" />

