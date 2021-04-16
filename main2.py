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

print(msg)
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

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # Level
        self.level = 1

    def setup(self,level):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.orders_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.fruit_list = arcade.SpriteList()

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


        msg="We use crates to define boundaries of our game, and put them in the wall_list\n"
        print(msg)
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

        fruit = arcade.Sprite(":resources:images/enemies/wormGreen.png", FRUIT_SCALING)

        fruit.bottom = FRUIT_SIZE * 9.75
        # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
        fruit.left = FRUIT_SIZE * 4

        fruit.boundary_right = FRUIT_SIZE
        fruit.boundary_left = FRUIT_SIZE
        fruit.change_y = -2
        self.fruit_list.append(fruit)
        fruit = arcade.Sprite(":resources:images/enemies/slimeBlue.png", FRUIT_SCALING)

        fruit.bottom = FRUIT_SIZE * 9.75
        # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
        fruit.left = FRUIT_SIZE * 9

        fruit.boundary_right = FRUIT_SIZE
        fruit.boundary_left = FRUIT_SIZE
        fruit.change_y = -4
        self.fruit_list.append(fruit)

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
        if self.level==2:
            lvl_2_orders= ["Our Images/Sample_order_lvl2.1.PNG", "Our Images/Sample_order_lvl2.2.PNG",
                           "Our Images/Sample_order_lvl2.3.PNG"]
            rdm_lvl_2_order = rdm.choice(lvl_2_orders)
            order_coordinate_list = [[950, 570]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(rdm_lvl_2_order, TILE_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)


        # Create the 'physics engine'

        #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        msg="Our final step is to generate the physics engine using,\n\n" \
            "self.physics_engine=arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list),\n\n" \
            " where the first argument is the player and the second argument is what objects the player can not go through.\n"
        print(msg)
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

        # See if the user got to the end of the level
        if len(arcade.check_for_collision_with_list(self.player_sprite, self.fruit_list)) > 0:
            self.level += 1
            # Load the next level
            self.setup(self.level)
            print("yes")
def main():
    """ Main method """
    window = MyGame()
    window.setup(window.level)
    arcade.run()


if __name__ == "__main__":
    main()