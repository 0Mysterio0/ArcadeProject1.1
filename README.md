# Arcade Project


###Actual To Do List:
1. Update all levels to match formatting of level 1 order 2

2. Make sounds when hitting fruit and suckers

3. Fix ending screen to show ending instructions

4. Write Report
###To Do List:
~~1. Import our own pictures to make game *cool*~~

2. ~~Make player move only between bounds~~

3. ~~Have fruit and suckers fall from sky, with random speeds~~

~~4. Randomize fruit orders and display correct fruit~~

~~5. Advance to next level once collected fruit~~

~~6. Have an ending screen~~

~~7. Have title/intro screen~~

9. Make sound when collecting fruit and suckers

10. Have background music

~~11. Made sucker movement different/harder than fruit movement, potentially
utilizing x and y coords.~~

~~12. Randomize initial placement of fruits and suckers~~

~~13. Fruit gets placed into basket, on top of one another~~

~~14. Have order matter when collecting fruits~~

###Extra:
~~Ex1. after losing, the fruit gets sucked up and out of your basket.~~

Ex2. Player animations

Ex3. Player select

Ex4. Balloons appear when you complete a level
###Notes:
textures/directions would be super complex to code

Used a crate for boundaries

References were helpful, yet also not*

So far, when a fruit hits your basket, it gets removed and the score increases.
When you hit 3 fruit that level, it starts the next level.

*Initially we tried to mess with the update settings, but that was not working 
as it updated the score several times as the fruit was passing through the 
player sprite essentially.*

*Initially everything was handled with sprite lists, but this caused unexpected
issues. We had to consider sprites separately for things to actually run properly
as well as have logical operations.* 

*Coins and fruit tied together initially --> moved to just coins*

We decided to create a game in pycharm for our final project. Our overall concept
was to create a game where you are given an order of fruit and you are required to catch 
the falling fruit in that order. To do this we had to set up quite a few different things, 
including fruit orders, a movable player, randomized positions and speeds of the falling 
fruit and 