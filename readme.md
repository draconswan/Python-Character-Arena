# Python Character Arena

## Installation and Launching
This project was developed on and designed for python version 3.6.  
It requires tkinter and Pillow Graphics to be installed.  
Pillow graphics can be found here: http://pillow.readthedocs.io/en/5.1.x  
There is an information page on their site on how to install Pillow depending on your operating system: http://pillow.readthedocs.io/en/5.1.x/installation.html

Once you have pillow graphics installed, to start the project, execute to Main.py file in the root 'src' folder.

## Functionality
### Details
This application simulates a battle between a player and an opponent.

When you start the program, you will see an empty arena.  To add a player and an opponent, start from the File menu at the top of the screen.

When you select Add Player, you can either create your own player, or select from a list of pre-generated players (loaded from the players.csv file within the project).  
If you choose to create your own player, you will be presenting a small window to enter the details about your player.  This form will ensure you only enter valid values.

### Character (and Opponent) Details:
Here are a few details about the stats of your character:  
**Name** - Your characters's name  
**Class** - Your character's class (only cosmetic at this time)  
**Strength** - The base amount of damage your character deals if they hit an opponent  
**Quickness** - The amount added to your change to hit an opponent  
**Health** - The amount of damage you can take before being defeated  
**Armor** - The number an opponent must meet or beat in order to hit you.  

Once you have your player, you then select with opponent you wish to battle.  The opponents are loaded from the opponents.csv file from within the project.  At this time, you cannot create your own opponent like you can a player.

### Battle
When both a player and an opponent are loaded into the arena, to start the battle click on the "Start Battle" button.  The battle will then run and display the status of each round.  The arena is configured to run a maximum of 10 rounds.

Each round follows this pattern:  
* Player's Turn
  * A random number between 1 and 20 (inclusive) is generated and the Player's quickness is added to this number.  
  * If this "attack roll" is greater than or equal to the Opponent's armor, they hit.  
  * On a successful hit, a random number between 1 and 8 (inclusive) is generated and the Player's strength is added to this number.  
  * The Opponent then takes damage equal to this number.
* Opponent's Turn
  * If the Opponent is not defeated by the Player's attack, they then get a chance to attack the Player.  
  * A random number between 1 and 20 (inclusive) is generated and the Opponent's quickness is added to this number.  
  * If this "attack roll" is greater than or equal to the Player's armor, they hit.  
  * On a successful hit, a random number between 1 and 8 (inclusive) is generated and the Opponents's strength is added to this number.  
  * The Player then takes damage equal to this number.  If the player is defeated, the battle is over.
  
After each round, the health values of the player and the opponent will be updated to reflect their current health and messages from that round will be displayed in the center.  
If the battle runs long enough, the screen will generate a scroll bar to scroll the messages.  At this point, you have to hover over the scroll bar to scroll the middle window.

### Battling Again 
Once you have completed a battle, you can either run the battle simulation again or load a new set of participants and run the battle again.  
Each time "Start Battle" is clicked, the participants are healed back to full health, and the arena resets to round 1.