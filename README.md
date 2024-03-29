# Simple Games
Contains multiple basic games coded in Python. Games each consist of a single Python file and no or limited additional requirements; I might eventually make this pip-installable.

**Games**
- Adventure (adventure.py)
- Mr. Flynn's Math Game (math_game.py)
- Tic-Tac-Toe (tictactoe.py)

## Adventure
*A short, text-based adventure. There's a bear and adult language.*

### Design and Implementation
The game was built step by step and changed considerably from the first iteration.
- Design initial game steps/path
- Code with ifs/elifs/elses, add main loop
- Add all room and story descriptions to dictionaries, replace in code with dictionary calls
- Add path dictionary and validation to limit user movement
- Use dedent from textwrap to clean up unwanted multi-line text indents for user
- Testing, minor text changes
- Add variables and related if/elses so user sees different text if they've already encountered the bear, been to the shop, or met the mage

### Next
It's a fairly basic game but solid, I might expand it later with additional puzzles or interactions.

## Mr. Flynn's Math Game
*A basic math game taught to me in 7th grade math with Mr. Flynn and often played with A-10 playing cards.*

Note that this requires the random, time, and regex libraries, although these are all standard Python libraries.

### Design and Implementation
Allegedly, the game has no unsolvable problems, so I didn't start with a backend validator (see my [Automaze](https://github.com/morganjohanna/automaze) repo for how I set up one of these for a maze game). Instead, I started with 3 simple functions in a parent class for ease of shared variables (comment-driven dev):
- **main** controls the game loop, keeps track of time, allows the player to skip a problem, and enables them to control when the next problem is presented and the round begins
- **new_problem** generates the problem
- **solution_check** validates the player's solution
I started with basic functions then tweaked them to ensure robustness for invalid inputs, to respect order of operations, and to prevent divide by 0 errors.
Initially I wanted to use basic keypress functionality to allow the player to skip a problem, but decided not to go too in depth with additional libraries.

### Next
- I have a stretch goal of teaching the computer to also calculate the answer, so that if a player skips a problem, they can still see an answer.
- A version where multiple people can play vs. one another and wins compared would be nice.
- I'll probably add the ability to export one's performance to a csv and may also keep a top 10 list accessible when the game is running.

## Tic-Tac-Toe
*The classic game played in complicated fashion in a terminal.*

### Design and Implementation
The game is managed by global variables and a nested list that serves as the board; it's intended to be played by 2 humans who input row (1-3) and column (A-C) choices to place an X or O. Every turn, the game iterates through different win conditions before prompting the next player.

I start by writing win conditions as part of a simple challenge, then decided to just code the entire game. The win conditions became a function (wincheck) and I added player functions (now merged into a single one, player_turn) to prompt players to choose their move and validate it as legal, global variables to manage the game (which player's turn it is, what to do if the board is full), and the main game loop.

### Next
I might later make it so the user can play vs. the computer.