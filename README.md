# Lily's Fruit Quest
#####By Kaylee Roberts, Seth Woodwyk and Tess Scheidel

##Our Project

We decided to create a game in pycharm for our final project. The overall concept for our game was for the player to be
given an order of fruit and for them successfully catch those fruits as they fell, in the specified order while avoiding
other unwanted items. If the player attempted to catch fruit in the incorrect order, the fruit would not be added to the
basket. If the player caught an unwanted item, a fruit would be removed from their basket. 

Along with these objectives, we had goals to add some fun extras to our project. One idea was to utilize physics to 
recognize if the fruits stacked up in a straight line. If the fruit or objects were not stacked well, the basket would
eventually become unbalanced and fall, causing you to lose your fruit stack. Unfortunately, due to time restraints we
were unable to add some of these extras into our final product. However, we like to think that this game is a continuous 
work in progress and we are looking forward to continuing to add to our game in the future.


##Our Process

###Working Collaboratively
From the start, it was clear that CoCalc and Jupyter Notebooks were not going to be the best option to bring our game to 
life. Pycharm is the main environment to create games in Python because we can most easily utilize the arcade library 
(which is essential for game creation). We were all able to download Pycharm on our individual computers but this
presented a problem when it came to working collaboratively. To fix this problem, we created a repository on GitHub, 
where we could update and share changes we each made. None of us had a lot of previous experience working in GitHub so
we ran into a few obstacles (missing changes, merging conflicts, etc.) but we became fairly good at sorting these issues 
out as we went along. Overall, GitHub was a good way for us to work together on our game and can be a very helpful 
tool for collaboration on future coding projects.

After figuring out a way to work together, we were finally able to dive into the creation of our game.

###The Set-Up

To being, we started by brainstorming a list of all the components we wanted to include in our game. This included: a
movable player, randomized fruit orders, randomized positions/speeds of the falling fruit and obstacles, and multiple
levels. We heavily relied on the resources and guidance from the Arcade Academy tutorial/website for the initial set up
of our game screen and movement functions for our player. We utilized crate objects as the boundaries of our screen. The
crates are positioned just out of frame, so our character is still fully visible on screen when they bump into them.From
there, we updated, modified or created functions for each of our other components (specifically the falling fruit and 
suckers).

####*Important functions that we utilized:*

The major functions that we used in our game (and are present in almost every game), were on_draw(), on_key_press()/on_key_release(),
and on_update(). On_draw renders each of our components on the screen. On_key_***() is used for the player movement. 
On_update() is where the most important aspects/changes occur. This is how we check to see if we caught any fruit or
hit any suckers, as well as check conditions for moving onto the next level. More on this later.


####*Original randomized functions we created:*
We also created movement functions for the fruit and suckers. We utilized the random library in each of these functions
to randomize the locations of each of the falling sprites, as well their speed. An extra flair was added to the
sucker sprites, which randomized changes in the side to side (the x position) causing them to sometimes move diagonally
across the screen.

We also created a way to randomize possible orders for each level, by choosing a sprite from a list. They were always 
located in the top, right-hand corner of our screen, and would correspond to the type of fruit that was falling.

From here, we faced our biggest challenge--creating a way for our player to interact with the fruit and the suckers. 
This is where most of our time was spent and included a lot of experimentation as well as trial and error.

###Creating the Interactions


####*Attempt 1*

Initially, we attempted to create lists for each fruit. We tried this approach based on the guides we found on Arcade
Academy. This code was inefficient and ultimately, did not work like we wanted it to. We weren't able to efficiently
interact with each fruit. Every collision and update had to be on a fruit by fruit basis, which was a lot of unneccesary
coding. It was also incredibly hard to make the fruit interact with each other and our player. We attempted to utilize a
behind the scens scoring system, so that each time we hit a fruit, our score would increase and each time we hit a sucker
our score would decrease. This was somewhat successful because we were able to set conditions for moving onto the next
level but we were unable to create visible stacks of fruit on our player. So we changed tactics.

####*Attempt 2*

Our second attempt included creating coin lists for each fruit. From the Aracade Academy tutorial pages, there were example
code chunks that gave us a bit more direction with creating interactions. Specfically, this is where we came across the 
follow_sprite() function in conjunction with the check_for_collisions_in_list(). In this iteration of our game, we 
essentially had two sprites for each fruit. One was the initial fruit, where if it hit the player it would disappear and
add points to our scoring system. The coin fruit, was essentially the "ghost fruit", tied to the location of the original
fruit sprite. This coin fruit was the sprite that would interact with the player and be added to the fruit basket with
the follow_sprite() function. We actually made some pretty decent progress using this tactic. We were able to stack fruits
on the movable player(although they stacked in the positive z-axis, not the positive y-axis). We were also able to move 
to the next levels using the scoring functions.

However, this was still not very efficient code and we still had a lot of issues. The problem with the fruit/coin fruit 
system was that on each update, we had problems with splitting. Intially, the locations for each of the sprites (the 
fruit and the coin fruit) were set equal to each other. However, the respawn locations of each fruit were randomized once
they hit the ground. Oddly, only certain fruits and coins would split on the update. We weren't able to find a pattern as
to why this occurred and it was a bit of a mystery. Once again, we also had trouble with the fruits interacting with each
other. When the fruit coins stacked, they only interacted with the player, causing them to stack in front of each other 
instead of on top of each other. We attempted to make different movement functions for each fruit and fruit coin depending
on their location in the order, so it would update and follow the fruit before it. However, we had to make specific lists 
for each fruit, *for each order*, ***for each level***. This was very inefficient and a lot of variables to keep track of.
So, we once again changed tactics, with a few alterations to our initial goals.

###Some Alterations to our Initial Goals 


###Final Solution

To create this game, we did a lot of experimentation. It took us many attempts and different 
approaches to finally make our final product. To begin, we took baby steps. We worked through making
sprites fall from the sky in randomized locations and at different speeds. We used the random package to
create the different locations and speeds from a given range. From there, we attempted to create a way for 
our player to interact with the falling fruit. This required the arcade.check_for_collisions_with_list()
function. This is where we initially created a lot more work for ourselves.

Our initial attempt was to create lists for each fruit. This code was inefficient and ultimately,
did not work like we wanted it to. Each collision and update had to be on a fruit by fruit basis.
It was also incredibly hard make the fruit interact with each other, and our character. This was where
we changed tactics again. 

We then attempted to create fruit sprites paired coins of the same fruit image. The coins were supposed
to be what interacted with our player. The fruit sprite would be removed and the paired fruit coin would be what 
stacked on our player. We ran into difficulties with keeping the coin and fruit stacked/joined together (they
would often split when they touched the ground). We realized that this wasn't going to work for our game either.

In addition to our struggles with the splitting coins and fruits, we also
faced challenges with the orders. 


No longer more than one fruit movement functions.


Each order had its own list and level and everything.
All of the draw fruit functions are now in one, instead of originally
being 



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