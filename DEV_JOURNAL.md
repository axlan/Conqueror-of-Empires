## 8/31
After considering building my own UI and mapping framework, I decided to just build off of the Conqueror of Empires codebase I found in PyGames project listing. I also considered scraping sprites from advanced wars or other similar games, but the ones in the codebase seem fine to start.

To actually get going I decided to set some small achievale goals:

1. Text screen to give back story
2. Menu to choose to spend money on intelligence

Looking into the program flow, I should add states to project/control/controller.py

I decided to go a little overboard and make a more complex dialogue UI with protraits and some text custimization

## 9/1

Still working on Dialogue UI.
Managed to get a decent first version with some advanced features done.

## 9/2

Got shop dialogue working minimally.
Fixed refactored changes to make the main game work again.
Started looking at the way the map is rendered.

## 9/4

Looking to make a custom map render.
I was able to strip out a bunch of the logic to get a simple board to display
next step is to create a menu to show intelligence, and deploy available troops.
Eventually the game states I'm working on should be a loop that gets fed the level ID
and the load save logic would select the level or resume the current level.

## 9/6

Working on adding overlay to show available spawn points.
Refactored code to have a clearer concept of levels, and include JSON level description
Added spawns of random enemy formations

Need to figure out how to encode the properties of the items purchased. Maybe constant
map like dialogue properties.

First level will be an enemy scout on one side of the lake. Positioning yourself
incorrectly will allow it to invade the city. Placing yourself correctly will block it.


