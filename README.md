# Simple Games
Contains multiple basic games coded in Python. Games each consist of a single Python file and no additional requirements; I might eventually make this pip-installable.

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

## Tic-Tac-Toe
*The classic game played in complicated fashion in a terminal*

### Design
The game is managed by global variables and a nested list that serves as the board; it's intended to be played by 2 humans who input a row (1-3) and column (A-C) to place an X or O. Every turn, the game iterates through different win conditions before prompting the next player.

### Next
I'll fix the input issue (so it doesn't crash when user inputs something unaccepted). I might later make it so the user can play vs. the computer.