# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Our Game Space!!
"""
import arcade
import random as rdm

# Constants
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

#print(msg)
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
        self.player_list = None
        self.fruit_list= None
        self.junk_list=None
        #self.wrong_fruit.list=None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # Level
        self.level = 1
        self.objective=0
    def setup(self,level):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.orders_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.fruit_list = arcade.SpriteList()
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






        # Set up the player, specifically placing it at these coordinates.
        image_source = "Our Images/Gal_with_basket.PNG"
        image_source_1="Our Images/Gal_left.PNG"
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
                           [1000, 96]]
        for coordinate in coordinate_list:
            #Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
        # Attempting to create fruit image at the top of the page but is currently green worm

        #@tess, is it safe to delete this code now? see fruit movement function below --> Yes! This can be deleted

        fruit = arcade.Sprite(":resources:images/enemies/wormGreen.png", FRUIT_SCALING)

        fruit.bottom = FRUIT_SIZE * 9.75
        # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
        fruit.left = FRUIT_SIZE * 4

        fruit.boundary_right = FRUIT_SIZE
        fruit.boundary_left = FRUIT_SIZE
        fruit.change_y = -2
        #self.fruit_list.append(fruit)
        fruit = arcade.Sprite(":resources:images/enemies/slimeBlue.png", FRUIT_SCALING)

        fruit.bottom = FRUIT_SIZE * 9.75
        # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
        fruit.left = FRUIT_SIZE * 9

        fruit.boundary_right = FRUIT_SIZE
        fruit.boundary_left = FRUIT_SIZE
        fruit.change_y = -4
        #self.fruit_list.append(fruit)

        def Fruit_Movement(self,fruit):
            """Defining a function that condenses the fruit movement operations, input what fruit you want
            to move down the screen, then it will append that fruit to the fruit list for you.  """
            fruit.bottom = FRUIT_SIZE * 9.75
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            fruit.left = FRUIT_SIZE * rdm.randint(4,16)

            fruit.boundary_right = FRUIT_SIZE
            fruit.boundary_left = FRUIT_SIZE
            fruit.change_y =rdm.choice([-5,-4,-3,-2])
            self.fruit_list.append(fruit)
        def Sucker_Movement(self,sucker):
            """Defining a function that condenses the sucker movement operations, however does not work as expected
             yet.  """
            sucker.bottom = FRUIT_SIZE * 9.75
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            sucker.left = FRUIT_SIZE * rdm.randint(4,16)

            sucker.boundary_right = FRUIT_SIZE
            sucker.boundary_left = FRUIT_SIZE
            sucker.change_y =rdm.choice([-5,-4,-3,-2])
            self.junk_list.append(sucker)
        #Order box in top right corner
        if self.level==1:
            lvl_1_orders= ["Our Images/Sample_order_lvl1.1.PNG", "Our Images/Sample_order_lvl1.2.PNG",
                           "Our Images/Sample_order_lvl1.3.PNG"]
            rdm_lvl_1_order = rdm.choice(lvl_1_orders)
            order_coordinate_list = [[950, 570]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(rdm_lvl_1_order, TILE_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)

            #Only append fruits that are required for each order:
            #If order one is selected
            if rdm_lvl_1_order=="Our Images/Sample_order_lvl1.1.PNG":
                """So far this will display all fruit and suckers at the same time, which is probably not what
                               we want for the game"""
                Fruit_Movement(self, Watermelon)
                Sucker_Movement(self, Sucker1)
                Fruit_Movement(self, Orange)
                Sucker_Movement(self, Sucker2)
                Fruit_Movement(self, Grapes)
                Sucker_Movement(self, Sucker3)
                """Below here was the setup to get certain fruit to appear at certain times, but was not working yet"""
                #if self.objective==10:
                    #Fruit_Movement(self, Watermelon)
                    #Sucker_Movement(self, Sucker1)
                #elif self.objective==10:
                    #Fruit_Movement(self, Orange)
                    #Sucker_Movement(self, Sucker1)
                #else:
                    #Fruit_Movement(self, Grapes)
                   # Sucker_Movement(self, Sucker2)

            # If order two is selected
            if rdm_lvl_1_order=="Our Images/Sample_order_lvl1.2.PNG":
                """So far this will display all fruit and suckers at the same time, which is probably not what
                               we want for the game"""
                Fruit_Movement(self, Apple)
                Sucker_Movement(self, Sucker1)
                Fruit_Movement(self, Kiwi)
                Sucker_Movement(self, Sucker2)
                Fruit_Movement(self, Grapes)
                Sucker_Movement(self, Sucker3)
                #if self.objective == -10:
                   # Fruit_Movement(self, Apple)
                    #Sucker_Movement(self, Sucker2)
                #elif self.objective == -1:
                   # Fruit_Movement(self, Kiwi)
                    #Sucker_Movement(self, Sucker2)
                #else:
                   # Fruit_Movement(self, Grapes)
                    #Sucker_Movement(self, Sucker2)
            # If order three is selected
            if rdm_lvl_1_order=="Our Images/Sample_order_lvl1.3.PNG":
                """So far this will display all fruit and suckers at the same time, which is probably not what
                we want for the game"""

                Fruit_Movement(self, Bannana)
                Sucker_Movement(self, Sucker1)
                Fruit_Movement(self, Cherry)
                Sucker_Movement(self, Sucker2)
                Fruit_Movement(self, Grapes)
                Sucker_Movement(self, Sucker3)

                #if self.objective == -10:
                    #Fruit_Movement(self,Bannana)
                    #Sucker_Movement(self, Sucker3)
                #elif self.objective == -1:
                    #Fruit_Movement(self,Cherry)
                    #Sucker_Movement(self, Sucker3)
                #else:
                   # Fruit_Movement(self, Grapes)
                    #Sucker_Movement(self, Sucker2)
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

        #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        #msg="Our final step is to generate the physics engine using,\n\n" \
            #"self.physics_engine=arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list),\n\n" \
            #" where the first argument is the player and the second argument is what objects the player can not go through.\n"

        self.physics_engine=arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.orders_list.draw()
        self.fruit_list.draw()
        self.junk_list.draw()

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

        # Move the player with the physics engine
        self.physics_engine.update()

        for fruit in self.fruit_list:
            if arcade.check_for_collision_with_list(fruit, self.wall_list):
                fruit.bottom = FRUIT_SIZE * 9.75
                # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
                fruit.left = FRUIT_SIZE *rdm.randint(2,12)
        self.fruit_list.update()

        for sucker in self.junk_list:
            if arcade.check_for_collision_with_list(sucker, self.wall_list):
                sucker.bottom = FRUIT_SIZE * 9.75
                # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
                sucker.left = FRUIT_SIZE *rdm.randint(2,12)
        self.junk_list.update()

        # See if we hit any coins
        fruit_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.fruit_list)

        # Loop through each fruit we hit (if any) and remove it
        for fruit in fruit_hit_list:
            # Remove the fruit --> I don't know if this is what we want to have happen... we want it to register
            # that we hit something but if we remove it (and we don't have a way to regenerate the objects falling)
            # we won't be have enough fruit to make it through all of the levels
            fruit.remove_from_sprite_lists()
            # Play a sound
            #arcade.play_sound(self.collect_coin_sound)
            # Add to the score
            self.objective += 1.5
            self.fruit_list.update()

        junk_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.junk_list)

        # Loop through each sucker we hit (if any) and remove it
        for sucker in junk_hit_list:
            # Remove the sucker
            sucker.remove_from_sprite_lists()
            # Play a sound
            # arcade.play_sound(self.collect_coin_sound)
            # Subtract score
            self.objective -= 0.5
            self.junk_list.update()

        # See if the user got to the end of the level
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