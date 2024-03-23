# Shut The Box Simulator
https://www.mastersofgames.com/rules/shut-box-rules.htm

## The Game
### Rules of the game:
1. Start with 1-9 number tiles available for user
2. Roll 2 dice (2 random number generator between 1-6)
3. Add numbers together
4. Determine number tiles to knock down
5. Check if winner. If not, repeat steps 2-4

### Goal of the game:
Knock down all number tiles
Obtain the smallest possible number when the remaining tiles are concatenated together


## Running the Simulator
### Preparation
In main.py, there are 2 main inputs to update before running the simulator:
1. Strategies to try out
   1. Update the list of strategies at the top of the main function
   2. These can be selected from the options in the src/strategies/StrategyName class
2. Iterations per strategy
   1. Number of times each strategy will be run in order to get a true understanding of the strategies effectiveness
   
### Execution
* Run main.py
* Output
  * CSV with the game results will be outputted to the output directory
    * Output game moves as a CSV with the following columns:
      * Player name, date and time of game, weather, location (home, bar, tournament)
      * 9 sections with tiles remaining, dice roll, tiles selected to knock down
