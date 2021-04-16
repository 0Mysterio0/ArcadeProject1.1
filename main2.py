# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Our Game Space!!
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
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
        self.player_list = None
        self.fruit_list= None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.fruit_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        image_source = "Our Images/Gal.PNG"
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

        fruit = arcade.Sprite(":resources:images/enemies/wormGreen.png", FRUIT_SCALING)

        fruit.bottom = FRUIT_SIZE *9.75
        # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
        fruit.left = FRUIT_SIZE * 4

        fruit.boundary_right = FRUIT_SIZE
        fruit.boundary_left = FRUIT_SIZE
        fruit.change_y = -2
        self.fruit_list.append(fruit)

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
        self.coin_list.draw()
        self.player_list.draw()
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
        self.fruit_list.update()

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()