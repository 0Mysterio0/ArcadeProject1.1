Lily's Fruit Quest
======================
By Kaylee Roberts, Seth Woodwyk and Tess Scheidel

Our Project
---------------------

We decided to create a game in pycharm for our final project. The overall concept for our game was for the player to be
given an order of fruit and for them successfully catch those fruits as they fell, in the specified order while avoiding
other unwanted items. If the player attempted to catch fruit in the incorrect order, the fruit would not be added to the
basket. If the player caught an unwanted item, a fruit would be removed from their basket. 

Along with these objectives, we had goals to add some fun extras to our project. One idea was to utilize physics to 
recognize if the fruits stacked up in a straight line. If the fruit or objects were not stacked well, the basket would
eventually become unbalanced and fall, causing you to lose your fruit stack. Unfortunately, due to time restraints we
were unable to add some of these extras into our final product. However, we like to think that this game is a continuous 
work in progress and we are looking forward to continuing to add to our game in the future.


Our Process
----------------------------

###Working Collaboratively
From the start, it was clear that CoCalc and Jupyter Notebooks were not going to be the best option to bring our game to 
life. Pycharm is the environment we chose to create games in Python because we can most easily utilize the arcade library 
(which is essential for game creation). We were all able to download Pycharm on our individual computers but this
presented a problem when it came to working collaboratively. To fix this problem, we created a repository on GitHub, 
where we could update and share changes we each made. None of us had a lot of previous experience working in GitHub so
we ran into a few obstacles (missing changes, merging conflicts, etc.) but we became fairly good at sorting these issues 
out as we went along. Overall, GitHub was a good way for us to work together on our game and can be a very helpful 
tool for collaboration on future coding projects.

After figuring out a way to work together, we were finally able to dive into the creation of our game.

###The Set-Up

To begin, we started by brainstorming a list of all the components we wanted to include in our game. This included: a
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


####*Randomized functions we created:*
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
interact with each fruit. Every collision and update had to be on a fruit by fruit basis, which was a lot of unnecessary
coding. It was also incredibly hard to make the fruit interact with each other and our player. We attempted to utilize a
behind the scenes scoring system, such that each time we hit a fruit, our score would increase and each time we hit a sucker
our score would decrease. This was somewhat successful because we were able to set conditions for moving onto the next
level, but we were unable to create visible stacks of fruit on our player. So we changed tactics.

####*Attempt 2*

Our second attempt included creating coin lists for each fruit. From the Arcade Academy tutorial pages, there were example
code chunks that gave us a bit more direction with creating interactions. Specifically, this is where we came across the 
follow_sprite() function in conjunction with the check_for_collisions_in_list(). In this iteration of our game, we 
essentially had two sprites for each fruit. One was the initial fruit, where if it hit the player it would disappear and
add points to our scoring system. The coin fruit, was essentially the "ghost fruit", tied to the location of the original
fruit sprite. This coin fruit was the sprite that would interact with the player and be added to the fruit basket with
the follow_sprite() function. We actually made some pretty decent progress using this tactic. We were able to stack fruits
on the movable player(although they stacked in the positive z-axis, not the positive y-axis). We were also able to move 
to the next levels using the scoring functions.

This was still not very efficient code and we still faced a lot of issues. The problem with the fruit/coin fruit 
system was that on each update, we had problems with splitting. Initially, the locations for each of the sprites (the 
fruit and the coin fruit) were set equal to each other. However, the respawn locations of each fruit were randomized once
they hit the ground. Once again, we also had trouble with the 
fruits interacting with each other. When the fruit coins stacked, they only interacted with the player, causing them to 
stack in front of each other instead of on top of each other. We attempted to make different movement functions for each
fruit and fruit coin depending on their location in the order, so it would update and follow the fruit before it. However,
we had to make specific lists for each fruit, *for each order*, ***for each level***. This was very inefficient, and a lot
of variables to keep track of. So, we once again changed tactics, with a few alterations to our initial goals.

###Some Epiphanies and Alterations to our Initial Goals 

We realized working through our second attempt, that randomized orders were ambitious for our skill set and time frame.
They needlessly complicated our code and made things much more inefficient. We only wanted the specific fruits in the 
order to fall to avoid overcrowding the screen, and coding that for each possible order for each level in the way 
we were currently doing so, would have been a
lot of extra, unneeded work for little reward. So, moving forward, we only coded for one specific order for each level.

We also came to the realization that we didn't need both a fruit and a fruit coin for each object. The fruits were 
essentially used for addition to the behind the scenes score. That scoring system had a few flaws (if you caught too many 
suckers you weren't able to move on, etc.) So, if we were able to come up with a way to utilize the positioning and amount 
of fruit coins following the player, we wouldn't have a need for the original fruit or the score system. With these ideas
in mind, we moved forward and created the final system for our game.

###Final Solution

Our final code for the project is much more streamlined and efficient than any of our previous attempts. Each fruit is 
updated in an overall fruit list which is drawn, but also is associated with a tier list. These lists of coins correspond
to the different fruits in each order (so tier_list_1 will include the first fruit from the first order, the second order
and the third order) but will only be appended during specific levels. This condenses the amount of lists and variables we
have to keep track of. There are only 6 overall lists (5 tier lists and one overall list), instead of one for each fruit 
of each level. These lists also allow us to better utilize the collision function/interactions. As each fruit is its own
coin, appended to different lists, we can check for the interaction of a single fruit coin with a specific list. This also
allows for more overall control of interactions. Each fruit coin/list can either be falling, stacked or shaken. Fruits can
only interact with another fruit in a list if the stacked condition evaluates True. 

For example, in level one, the kiwi is the only fruit coin that can interact with the player because it is in the first
tier list. If it collides with the player, it follows the player and  its stacked condition evaluates True. Now, the 
pineapple coin can interact with the kiwi. When the pineapple coin collides with the kiwi, it will now follow that sprite
and its stacked condition will evaluate true. Furthermore, these functions are generalized to any of the fruit in 
the tier lists, such that if you wanted to update or change the order, you would only have to change the 
loaded sprite coin in the function list.

We used sucker movement and the dropping of fruit in a similar way. If a sucker interacts with any of the fruit and 
*it's stacked condition is True*, the shake condition evaluates True and causes the fruit to fall off of the player's 
basket. By utitlizing a series of elif statements, we allow the suckers to only shake of the fruit of the highest
tier level, instead of the player losing their entire fruit stack.

Now, to advance to the next level, the player must reach a specific number of fruit coins that have their stacked condition
evaluate as True. If they do, the player moves onto the next level. This allowed us to remove the old scoring system, and 
with it the issues of collecting too many suckers.

Our final approach streamlined our code *so much* and made everything much more intuitive. We no longer had
three different functions doing the same thing, multiple draw statements for each fruit or 20+ lists to keep track of. It
definitely took us a bit to get to this code but each step in our exploration was important as we began to better understand
the utilization of lists, collision syntax and update functions. We're really proud of how far we came and all of the progress
we made.

###Fun Extras We Were Able to Include
- Beginning and ending screens with intstructions --> we used similar code to the placement of orders on each level screen to do this
- Background music!
- Sounds for when we picked up fruits, when we hit suckers and when a fruit we had previously picked up fell on the ground
- Balloons that floated down on the ending screen --> similar to the falling fruit functions!
- The ability to leave the game (through the door) or restart the game by picking up the cherry on the ending screen
- Cheat keys --> if you press the "P" key, you can automatically advance levels and if you press the "O" key you can go back a level


###References
[Python Arcade Academy Home Page](https://arcade.academy/)

[Python Arcade Academy Resource Page](https://arcade.academy/resources.html)

[Python Arcade Academy Sprite Resource](https://arcade.academy/_modules/arcade/sprite.html)

[Python Arcade Academy Follow Sprite Function Resource](https://arcade.academy/examples/sprite_follow_simple_2.html)

[Python Arcade Academy Coins Resource](https://arcade.academy/examples/platform_tutorial/step_06.html)

*The links to the sounds we utilized can be found within our code*



###Final Notes

We had a lot of fun making this game but with it came some unexpected challenges and lots of trial and error, as well as
some pretty funny moments when we accidentally broke our game. If you'd like to see some screenshots of our progress,
you can find them in our GitHub repository in the "Game Screenshots" folder. We hope you enjoy playing our game as much as
we enjoyed making it!



