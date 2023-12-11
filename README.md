A 2D-board game using pygame.
Make use data structure like tree and binary tree to build a game tree for the bot to get the best move.

Game design and rule:
This game is a 2D board game. Initially player 1 has a gem in the top left corner and player 2 has a gem in the bottom right corner. Players take turns adding one gem per turn to the board. A gem can be added to any empty square or any square where the player has at least one gem. If the number of gems in a square reaches the number of neighbours for the cell, the gems overflow into its neighbours, increasing the number of gems and changing the colour of gems to that player's colour.

The game ends if every single gem on the board is the same colour. The player represented by that colour is the winner of the game.
