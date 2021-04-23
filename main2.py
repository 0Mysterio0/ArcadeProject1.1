# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Our Game Space!!
"""
import arcade
import random as rdm
import math

# Constants

#We need to utilize these constants more all around the game!!
#Also maybe increase the size of our game as well just in general.
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"


# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.3
TILE_SCALING = 0.5
COIN_SCALING = 0.5
FRUIT_SCALING = 0.5
SUCKER_SCALING=0.3
# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_START_X = 64
PLAYER_START_Y = 128
msg="Here we define our constants for our game,such as how fast our player will move across the screen," \
    " which in our case is={0}\n".format(PLAYER_MOVEMENT_SPEED)
# Fruits Constants
FRUIT_START_Y = 650
FRUIT_NATIVE_SIZE = 128
FRUIT_SIZE = int(FRUIT_NATIVE_SIZE * FRUIT_SCALING)
# Constants for falling fruit

SUCKER_START_Y = 650
SUCKER_NATIVE_SIZE=128
SUCKER_SIZE = int(SUCKER_NATIVE_SIZE * SUCKER_SCALING)
# Constants for falling suckers
Fruit_follow_speed=10
#print(msg)


#Each of these class sprites are tests basically. The one that actually works and is valuable is the coin one so far.
class TurningSprite(arcade.Sprite):
    """ Sprite that sets its angle to the direction it is traveling in. """
    def update(self):
        """ Move the sprite """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))

class Coin(arcade.Sprite):
    """
    This is an imported and adapted to our game coins class that will have (fruit coins) follow the player. We need to
    fix it so that fruits will stack on top of one another inside the basket somehow.
    Maybe make some predetermined heights or even
    make it so each fruit coin will follow the next fruit coin below it. For instance call the (follow sprite)
    function on each incoming fruit? Whatever we end up doing, we'll probably need to play around with the
    follow_sprite function below too and see what we can have it do.

    """

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of Fruit_follow_speed
        """
        #Unintentionally!! I think this would be another way for us to do ordering of the fruit!
        #where wrong fruits get collected and fall through player or something of that effect?
        #This may actually replace the use of the suckers? so only wrong fruit falls through,
        #and it knocks off one of the right fruit that is currently in the basket!!!!!
        #so the game keeps going while one keeps avoiding the wrong fruit?


        if self.center_y < player_sprite.top:
            self.center_y += min(Fruit_follow_speed, player_sprite.top - self.center_y)
        elif self.center_y > player_sprite.top:
            self.center_y -= min(Fruit_follow_speed, self.center_y - player_sprite.top)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(Fruit_follow_speed, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(Fruit_follow_speed, self.center_x - player_sprite.center_x)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.orders_list = None
        self.instructions_list = None
        self.player_list = None
        self.fruit_list= None
        self.cherry_list = None
        self.junk_list=None

        #Foundation lists to make an order based fruit collecting system.
        self.first_fruit=None
        self.second_fruit=None
        self.third_fruit=None


        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # Level
        self.level = 0

        #Defining Objective System, it gets a little complex here:
        #So far only self.objective is the true score. Anything else is just a foundation
        #for a later system. This might be just one potential option for us. We may be able to utiilze
        #the follow sprite function differently for fruits without referencing any sort of objectives?
        #or maybe this is used with these objectives as well for the whole process? Altogether it looks
        #like we have a few options.

        self.objective=0
        self.first_objective=0
        self.second_objective = 0
        self.third_objective = 0
        self.instr_objective=0
        self.control=0
    def setup(self,level):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.orders_list = arcade.SpriteList(use_spatial_hash=True)
        self.instructions_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList()
        self.fruit_list = arcade.SpriteList()
        self.cherry_list = arcade.SpriteList()
        self.junk_list=arcade.SpriteList()


        #Load all of the fruit images, but dont append them to any list yet:
        Apple = arcade.Sprite("Our Images/Fruits/Apple.png", FRUIT_SCALING * 1.8)
        Bannana = arcade.Sprite("Our Images/Fruits/Bannana.png", FRUIT_SCALING * 1.8)
        Cherry = arcade.Sprite("Our Images/Fruits/Cherry.png", FRUIT_SCALING * 1.8)
        Grapes = arcade.Sprite("Our Images/Fruits/grapes.png", FRUIT_SCALING * 1.8)
        Kiwi = arcade.Sprite("Our Images/Fruits/kiwi.png", FRUIT_SCALING * 1.8)
        Lemon = arcade.Sprite("Our Images/Fruits/lemon.png", FRUIT_SCALING * 1.8)
        Orange = arcade.Sprite("Our Images/Fruits/orange.png", FRUIT_SCALING * 1.8)
        Pear = arcade.Sprite("Our Images/Fruits/pear.png", FRUIT_SCALING * 1.8)
        Pineapple = arcade.Sprite("Our Images/Fruits/Pineapple.png", FRUIT_SCALING * 1.8)
        Plum = arcade.Sprite("Our Images/Fruits/plum.png", FRUIT_SCALING * 1.8)
        Strawberry= arcade.Sprite("Our Images/Fruits/Strawberry.png", FRUIT_SCALING * 1.8)
        Watermelon = arcade.Sprite("Our Images/Fruits/Watermelon.png", FRUIT_SCALING * 1.8)

        # Load all of the sucker images, but dont append them to any list yet:
        Sucker1=arcade.Sprite("Our Images/Suckers/sucker1.png", FRUIT_SCALING * 1.8)
        Sucker2 = arcade.Sprite("Our Images/Suckers/sucker2.png", FRUIT_SCALING * 1.8)
        Sucker3 = arcade.Sprite("Our Images/Suckers/sucker3.png", FRUIT_SCALING * 1.8)
        Sucker4=TurningSprite("Our Images/Suckers/sucker3.png", FRUIT_SCALING * 1.8)


        #Fruit Coin Lists?:
        Grape_coin= Coin("Our Images/Fruits/grapes.png", FRUIT_SCALING * 1.8)
        Cherry_coin = Coin("Our Images/Fruits/Cherry.png", FRUIT_SCALING * 1.8)
        Watermelon_coin = Coin("Our Images/Fruits/Watermelon.png", FRUIT_SCALING * 1.8)
        Orange_coin = Coin("Our Images/Fruits/orange.png", FRUIT_SCALING * 1.8)
        Pear_coin = Coin("Our Images/Fruits/pear.png", FRUIT_SCALING * 1.8)
        Pineapple_coin = Coin("Our Images/Fruits/Pineapple.png", FRUIT_SCALING * 1.8)
        Plum_coin = Coin("Our Images/Fruits/plum.png", FRUIT_SCALING * 1.8)
        Strawberry_coin = Coin("Our Images/Fruits/Strawberry.png", FRUIT_SCALING * 1.8)
        Kiwi_coin = Coin("Our Images/Fruits/kiwi.png", FRUIT_SCALING * 1.8)
        Lemon_coin = Coin("Our Images/Fruits/lemon.png", FRUIT_SCALING * 1.8)
        Apple_coin = Coin("Our Images/Fruits/Apple.png", FRUIT_SCALING * 1.8)
        Bannana_coin = Coin("Our Images/Fruits/Bannana.png", FRUIT_SCALING * 1.8)




        # Set up the player, specifically placing it at these coordinates.
        image_source = "Our Images/Gal_with_basket.PNG"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)



        # We use crates to define boundaries of our game, and put them in the wall_list.
        # This shows using a coordinate list to place sprites
        coordinate_list = [[-30, 96],
                           [1045, 96]]
        for coordinate in coordinate_list:
            #Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)


        def Fruit_Movement(self,fruit):
            """Defining a function that condenses the fruit movement operations, input what fruit you want
            to move down the screen, then it will append that fruit to the fruit list for you. Not sure if we
              use it here, but we need to take advantage of the SCREEN WIDTH variable. """
            # Maybe we make "ghost fruit that follow the other fruit"
            fruit.bottom = FRUIT_SIZE * 9.75
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            fruit.left = FRUIT_SIZE * rdm.randint(0,14)

            fruit.boundary_right = FRUIT_SIZE
            fruit.boundary_left = FRUIT_SIZE
            fruit.change_y =rdm.choice([-5,-4,-3,-2])
            self.fruit_list.append(fruit)
        def Advanced_Fruit_Movement(self,fruit,coin):
            """Ok so here me out. What if there is a (coin fruit)... such that the coin fruit follows the real
             fruit, and it gets picked up and the real fruit that manages the score variables is the one that
              disappears instead.
               Potential Issue so far: If the fruit hits the ground before its collected, the
               fruit coin and the real fruit get separated from each other """

            fruit.bottom = FRUIT_SIZE * 9.75
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            fruit.left = FRUIT_SIZE * rdm.randint(0,14)

            fruit.boundary_right = FRUIT_SIZE
            fruit.boundary_left = FRUIT_SIZE
            fruit.change_y =rdm.choice([-5,-4,-3,-2])
            self.fruit_list.append(fruit)
            coin.bottom = fruit.bottom
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            # This is where we make the  "ghost fruit" or "coin fruit" that follows the real fruit"
            coin.left =  fruit.left

            coin.boundary_right=fruit.boundary_right
            coin.boundary_left=fruit.boundary_left
            coin.change_y=fruit.change_y
            self.coin_list.append(coin)
        def Sucker_Movement(self,sucker):
            """Defining a function that eventually should have the suckers moving different than the fruits, but does
            not work yet.  """
            sucker.bottom = FRUIT_SIZE * 9.75
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            sucker.left = FRUIT_SIZE * rdm.randint(0,14)

            sucker.boundary_right = FRUIT_SIZE
            sucker.boundary_left = FRUIT_SIZE
            sucker.change_y =rdm.choice([-5,-4,-3,-2])
            sucker.change_x= rdm.choice([-1, 0, 1])
            self.junk_list.append(sucker)

        #Instruction screen
        if self.level==0:
            lvl_0="Our Images/Orders/Lvl1/Order1.1.PNG"
            instruction_coordinate_list = [[500, 550]]
            for coordinate in instruction_coordinate_list:
                instructions = arcade.Sprite(lvl_0, TILE_SCALING)
                instructions.position = coordinate
                self.instructions_list.append(instructions)
            fruit="Our Images/Fruits/Cherry.png"
            cherry_coordinate_list = [[925, 175]]
            for coordinate in cherry_coordinate_list:
                cherry_instr = arcade.Sprite(fruit, FRUIT_SCALING*1.8)
                cherry_instr.position = coordinate
                self.cherry_list.append(cherry_instr)

        #Order box in top right corner
        if self.level==1:
            lvl_1_orders= ["Our Images/Orders/Lvl1/Order1.1.PNG", "Our Images/Orders/Lvl1/Order1.2.PNG",
                           "Our Images/Orders/Lvl1/Order1.3.PNG"]
            rdm_lvl_1_order = rdm.choice(lvl_1_orders)
            order_coordinate_list = [[950, 550]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(rdm_lvl_1_order, TILE_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)
            Sucker_Movement(self,Sucker4)
            #Only append fruits that are required for each order:
            #If order one is selected
            if rdm_lvl_1_order=="Our Images/Orders/Lvl1/Order1.1.PNG":
                """So far this will display all fruit and suckers at the same time, which is probably not what
                               we want for the game"""

                Advanced_Fruit_Movement(self, Watermelon, Watermelon_coin)
                Sucker_Movement(self, Sucker1)
                Advanced_Fruit_Movement(self, Bannana, Bannana_coin)
                Sucker_Movement(self, Sucker2)
                Advanced_Fruit_Movement(self, Grapes, Grape_coin)
                Sucker_Movement(self, Sucker3)


            # If order two is selected
            if rdm_lvl_1_order=="Our Images/Orders/Lvl1/Order1.2.PNG":
                """So far this will display all fruit and suckers at the same time, which is probably not what
                               we want for the game"""
                Advanced_Fruit_Movement(self, Strawberry,Strawberry_coin)
                Sucker_Movement(self, Sucker1)
                Advanced_Fruit_Movement(self, Kiwi,Kiwi_coin)
                Sucker_Movement(self, Sucker2)
                Advanced_Fruit_Movement(self, Pineapple,Pineapple_coin)
                Sucker_Movement(self, Sucker3)
            # If order three is selected
            if rdm_lvl_1_order=="Our Images/Orders/Lvl1/Order1.3.PNG":
                """So far this will display all fruit and suckers at the same time, which is probably not what
                we want for the game"""

                Advanced_Fruit_Movement(self, Apple, Apple_coin)
                Sucker_Movement(self, Sucker1)
                Advanced_Fruit_Movement(self, Pear, Pear_coin)
                Sucker_Movement(self, Sucker2)
                Advanced_Fruit_Movement(self, Plum, Plum_coin)
                Sucker_Movement(self, Sucker3)

        if self.level==2:
            lvl_2_orders= ["Our Images/Sample_order_lvl2.1.PNG", "Our Images/Sample_order_lvl2.2.PNG",
                           "Our Images/Sample_order_lvl2.3.PNG"]
            rdm_lvl_2_order = rdm.choice(lvl_2_orders)
            order_coordinate_list = [[950, 550]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(rdm_lvl_2_order, TILE_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)
            if rdm_lvl_2_order == "Our Images/Sample_order_lvl2.1.PNG":

                if self.objective == 0:
                    Fruit_Movement(self, Watermelon)
                    Sucker_Movement(self, Sucker1)
                elif self.objective == 1:
                    Fruit_Movement(self, Orange)
                    Sucker_Movement(self, Sucker1)
                else:
                    Fruit_Movement(self, Grapes)
                    Sucker_Movement(self, Sucker2)
            if rdm_lvl_2_order == "Our Images/Sample_order_lvl2.2.PNG":

                if self.objective == 0:
                    Fruit_Movement(self, Watermelon)
                    Sucker_Movement(self, Sucker1)
                elif self.objective == 1:
                    Fruit_Movement(self, Orange)
                    Sucker_Movement(self, Sucker1)
                else:
                    Fruit_Movement(self, Grapes)
                    Sucker_Movement(self, Sucker2)
            if rdm_lvl_2_order == "Our Images/Sample_order_lvl2.3.PNG":

                if self.objective == 0:
                    Fruit_Movement(self, Watermelon)
                    Sucker_Movement(self, Sucker1)
                elif self.objective == 1:
                    Fruit_Movement(self, Orange)
                    Sucker_Movement(self, Sucker1)
                else:
                    Fruit_Movement(self, Grapes)
                    Sucker_Movement(self, Sucker2)

        if self.level==3:
            lvl_3_orders= ["Our Images/Sample_order_lvl3.1.PNG", "Our Images/Sample_order_lvl3.2.PNG",
                           "Our Images/Sample_order_lvl3.3.PNG"]
            rdm_lvl_3_order = rdm.choice(lvl_3_orders)
            order_coordinate_list = [[950, 530]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(rdm_lvl_3_order, FRUIT_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)


        # Create the 'physics engine'

        self.physics_engine=arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()

        self.fruit_list.draw()
        self.cherry_list.draw()
        self.junk_list.draw()
        self.coin_list.draw()
        self.orders_list.draw()
        self.instructions_list.draw()

        #testing if we can have sprites appear midlvel
        #okay so this tells us that sprites wont be draw physically
        #but still exist in the game the whole time!!
        #if self.objective>0:
           # self.orders_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        Watermelon_coin = Coin("Our Images/Fruits/Watermelon.png", FRUIT_SCALING * 1.8)
        Watermelon = arcade.Sprite("Our Images/Fruits/Watermelon.png", FRUIT_SCALING * 1.8)

        # Move the player with the physics engine
        self.physics_engine.update()



        for fruit in self.fruit_list:
            if arcade.check_for_collision_with_list(fruit, self.wall_list):
                fruit.bottom = FRUIT_SIZE * 9.75
                # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
                fruit.left = FRUIT_SIZE *rdm.randint(1,14)
        self.fruit_list.update()

        for coin in self.coin_list:
            if arcade.check_for_collision_with_list(coin, self.wall_list):
                coin.bottom = FRUIT_SIZE * 9.75
                # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
                coin.left = fruit.left
        self.coin_list.update()

        for sucker in self.junk_list:
            if arcade.check_for_collision_with_list(sucker, self.wall_list):
                sucker.bottom = FRUIT_SIZE * 9.75
                # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
                sucker.left = FRUIT_SIZE *rdm.randint(1,14)
        self.junk_list.update()

        # See if we hit any fruits
        fruit_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.fruit_list)

        # Hit the cherry
        cherry_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.cherry_list)

        # See if we hit any of our Fruit coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        #second_layer_hit_list=arcade.check_for_collision_with_list(self.first_fruit,
                                                            #  self.coin_list)

        #after we hit a fruit coin, it will follow the player around
        #eventually we need to check for collisions between the fruit coins and have them stack
        #on top of each other inside the basket as a whole
        #or we set predetermined heights for each incoming fruit to rest at.

        for coin in coin_hit_list:
            coin.follow_sprite(self.player_sprite)


        #this is where our game truly BEGINS
        #this allows for fruit to be added midlevel, and the self.control variable
        #keeps the spawning in check.
        if self.objective>0 and self.control==0:
            self.control+=1
            #Advanced_Fruit_Movement(self,Watermelon,Watermelon_coin)

        # Loop through each fruit we hit (if any) and remove it
        for fruit in fruit_hit_list:
            # Remove the fruit --> I don't know if this is what we want to have happen... we want it to register
            # that we hit something but if we remove it (and we don't have a way to regenerate the objects falling)
            # we won't be have enough fruit to make it through all of the levels'
            #--->should be resolved with the fruit coin system. --> it is indeed resolved with the coins
            fruit.remove_from_sprite_lists()
            # Play a sound
            #arcade.play_sound(self.collect_coin_sound)
            # Add to the score
            self.objective += 1.5
            self.fruit_list.update()

        for cherry in cherry_hit_list:
            # Remove the fruit --> I don't know if this is what we want to have happen... we want it to register
            # that we hit something but if we remove it (and we don't have a way to regenerate the objects falling)
            # we won't be have enough fruit to make it through all of the levels'
            #--->should be resolved with the fruit coin system. --> it is indeed resolved with the coins
            cherry.remove_from_sprite_lists()
            # Play a sound
            #arcade.play_sound(self.collect_coin_sound)
            # Add to the score
            self.instr_objective += 1
            self.cherry_list.update()

        junk_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.junk_list)

        # Loop through each sucker we hit (if any) and remove it
        for sucker in junk_hit_list:
            # Remove the sucker
            sucker.remove_from_sprite_lists()
            # Play a sound
            # arcade.play_sound(self.collect_coin_sound)
            # Subtract score
            self.objective -= 1.5
            self.junk_list.update()

        # See if the user got to the end of the level
        if self.level==0:
            if self.instr_objective>=1:
                    #once we hit a certain amount of fruit, go to next level
                    self.level += 1
                    # Load the next level
                    self.setup(self.level)
        if self.level==1:
            if self.objective>=3.5:
                    #once we hit a certain amount of fruit, go to next level
                    self.level += 1
                    # Load the next level
                    self.setup(self.level)
        if self.level==2:
            if self.objective==2:
                    #once we hit a certain amount of fruit, go to next level
                    self.level += 1
                    # Load the next level
                    self.setup(self.level)
def main():
    """ Main method """
    window = MyGame()
    window.setup(window.level)
    arcade.run()



if __name__ == "__main__":
    main()