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


#Constants for Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Lily's Fruit Quest"


# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.3
TILE_SCALING = 0.5
COIN_SCALING = 0.5
FRUIT_SCALING = 0.5
SUCKER_SCALING = 0.3
# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
PLAYER_START_X = 64
PLAYER_START_Y = 128

# Fruits Constants
FRUIT_START_Y = 650
FRUIT_NATIVE_SIZE = 128
FRUIT_SIZE = int(FRUIT_NATIVE_SIZE * FRUIT_SCALING)

# Constants for falling suckers
SUCKER_START_Y = 650
SUCKER_NATIVE_SIZE = 128
SUCKER_SIZE = int(SUCKER_NATIVE_SIZE * SUCKER_SCALING)

Fruit_follow_speed = 20

sound_effect_volume=0.03
#Was testing out different classes of sprite, one sucker now turns.
class TurningSprite(arcade.Sprite):
    """ Sprite that sets its angle to the direction it is traveling in. """

    def update(self):
        """ Move the sprite """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))


class Coin(arcade.Sprite):
    """
    This is an imported and adapted to our game coins class that will have (fruit coins) follow the player.
    """

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of Fruit_follow_speed
        """

        if self.top < player_sprite.top:
            self.top += min(Fruit_follow_speed, player_sprite.top - self.center_y)
        elif self.top > player_sprite.top:
            self.top -= min(Fruit_follow_speed, self.center_y - player_sprite.top)

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
        self.wall_list = None
        self.orders_list = None
        self.instructions_list = None
        self.intro_list = None
        self.player_list = None
        # Surprise
        self.Orange_boi = arcade.Sprite("Our Images/Outro/Bois/Orange Boi.png", FRUIT_SCALING * 1.8)
        self.Blue_boi = arcade.Sprite("Our Images/Outro/Bois/Blue Boi.png", FRUIT_SCALING * 1.8)
        self.Purple_boi = arcade.Sprite("Our Images/Outro/Bois/Purple Boi.png", FRUIT_SCALING * 1.8)
        self.Red_boi = arcade.Sprite("Our Images/Outro/Bois/Red Boi.png", FRUIT_SCALING * 1.8)
        self.Yellow_boi = arcade.Sprite("Our Images/Outro/Bois/Yellow Boi.png", FRUIT_SCALING * 1.8)

        self.cherry_list = None
        self.cherry_list_2 = None
        self.door_list = None
        self.outro_list=None

        self.Sucker_list = None
        #Revamped fruit list holds all fruit in every level
        self.revamped_fruit_list = None
        #Each tier list is used for stacking operations
        self.tier_1_fruit_list = None
        self.tier_2_fruit_list = None
        self.tier_3_fruit_list = None
        self.tier_4_fruit_list = None
        self.tier_5_fruit_list = None
        # Separate variable that holds the player sprite
        self.player_sprite = None


        # Load sounds
        self.picking_up_sound = arcade.load_sound(":resources:sounds/upgrade1.wav")

        self.losing_fruit_sound = arcade.load_sound("Sounds/sucker hit.wav")
        #Source: https://freesound.org/people/cabled_mess/sounds/350986/

        self.burst_sound=arcade.load_sound("Sounds/pop.wav")
        #Source:https://freesound.org/people/CBJ_Student/sounds/545200/

        self.fruit_hit_ground=arcade.load_sound("Sounds/splat.wav")
        # Source: https://freesound.org/people/Breviceps/sounds/445117/

        self.intro_theme=arcade.load_sound("Sounds/Intro Theme.wav")
        # Source: https://freesound.org/people/Mrthenoronha/sounds/521656/

        self.background_music=arcade.load_sound("Sounds/Background music.wav")
        # Source: https://freesound.org/people/BloodPixel/sounds/567193/
        self.background_playing = False
        # Level
        self.level = 0

        # Bools for the intro and outro objectives
        self.instr_objective = False
        self.restart_objective = False

        # When game is over, this allows for the game to close
        self.game_over = False

        # We use these bools when each fruit is stacked
        self.Stacked_1 = False
        self.Stacked_2 = False
        self.Stacked_3 = False
        self.Stacked_4 = False
        self.Stacked_5 = False
        # List for fruit in the stack
        self.stacked_fruit = None
        # These bools are for when a sucker is hit, it will shake the fruit off.

        #These bools are for when a sucker is hit, it will shake the fruit off.
        self.Shake_1 = False
        self.Shake_2 = False
        self.Shake_3 = False
        self.Shake_4 = False
        self.Shake_5 = False

        #Skip levels for testing
        self.skip_level = False
        self.reverse_level = False

    def setup(self, level):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.orders_list = arcade.SpriteList(use_spatial_hash=True)
        self.instructions_list = arcade.SpriteList(use_spatial_hash=True)
        self.intro_list = arcade.SpriteList(use_spatial_hash=True)

        self.cherry_list = arcade.SpriteList()
        self.cherry_list_2 = arcade.SpriteList()
        self.door_list = arcade.SpriteList()
        self.outro_list=arcade.SpriteList()
        #We use this list for each level of fruits
        self.revamped_fruit_list = arcade.SpriteList()

        # Consider a list for each tier of fruit in the tower, but don't actually draw
        # from this list
        # Think of these as categories for operations
        self.tier_1_fruit_list = arcade.SpriteList()
        self.tier_2_fruit_list = arcade.SpriteList()
        self.tier_3_fruit_list = arcade.SpriteList()
        self.tier_4_fruit_list = arcade.SpriteList()
        self.tier_5_fruit_list = arcade.SpriteList()
        self.stacked_fruit = arcade.SpriteList()
        # This sucker list works for every level
        self.Sucker_list = arcade.SpriteList()


        self.Sucker1 = arcade.Sprite("Our Images/Suckers/sucker1.png", FRUIT_SCALING * 1.8)
        self.Sucker2 = arcade.Sprite("Our Images/Suckers/sucker2.png", FRUIT_SCALING * 1.8)
        self.Sucker3 = arcade.Sprite("Our Images/Suckers/sucker3.png", FRUIT_SCALING * 1.8)
        self.Sucker4 = TurningSprite("Our Images/Suckers/sucker3.png", FRUIT_SCALING * 1.8)


        #We only need individual fruit coins instead!
        self.Grape_coin = Coin("Our Images/Fruits/grapes.png", FRUIT_SCALING * 1.8)
        self.Cherry_coin = Coin("Our Images/Fruits/Cherry.png", FRUIT_SCALING * 1.8)
        self.Watermelon_coin = Coin("Our Images/Fruits/Watermelon.png", FRUIT_SCALING * 1.8)
        self.Orange_coin = Coin("Our Images/Fruits/orange.png", FRUIT_SCALING * 1.8)
        self.Pear_coin = Coin("Our Images/Fruits/pear.png", FRUIT_SCALING * 1.8)
        self.Pineapple_coin = Coin("Our Images/Fruits/Pineapple.png", FRUIT_SCALING * 1.8)
        self.Plum_coin = Coin("Our Images/Fruits/plum.png", FRUIT_SCALING * 1.8)
        self.Strawberry_coin = Coin("Our Images/Fruits/Strawberry.png", FRUIT_SCALING * 1.8)
        self.Kiwi_coin = Coin("Our Images/Fruits/kiwi.png", FRUIT_SCALING * 1.8)
        self.Lemon_coin = Coin("Our Images/Fruits/lemon.png", FRUIT_SCALING * 1.8)
        self.Apple_coin = Coin("Our Images/Fruits/Apple.png", FRUIT_SCALING * 1.8)
        self.Bannana_coin = Coin("Our Images/Fruits/Bannana.png", FRUIT_SCALING * 1.8)



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
            # Add a crate on the ground
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        def Basic_Fruit_Movement(fruit):
            """Defining a function that condenses the fruit movement operations, input what fruit you want
            to move down the screen"""
            fruit.bottom = FRUIT_SIZE * 9.75
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            fruit.left = FRUIT_SIZE * rdm.randint(0, 14)

            fruit.boundary_right = FRUIT_SIZE
            fruit.boundary_left = FRUIT_SIZE
            fruit.change_y = rdm.choice([-4, -3, -2])

        # Still use this sucker movement.
        def Sucker_Movement(sucker):
            """Defining a function that has the suckers moving different than the fruits"""
            sucker.bottom = FRUIT_SIZE * 9.75
            # fruit.left will have to by FRUIT_SIZE * an random integer --> use random here
            sucker.left = FRUIT_SIZE * rdm.randint(0, 14)

            sucker.boundary_right = FRUIT_SIZE
            sucker.boundary_left = FRUIT_SIZE
            sucker.change_y = rdm.choice([-5, -4, -3, -2])
            sucker.change_x = rdm.choice([-1, 0, 1])

        # Instruction screen
        if self.level == 0:
            arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
            self.intro_player=arcade.play_sound(self.intro_theme,volume=0.02)
            self.intro_playing=True
            lvl_0="Our Images/Intro/Title.PNG"
            intro_coordinate_list = [[500, 550]]
            for coordinate in intro_coordinate_list:
                intro = arcade.Sprite(lvl_0, TILE_SCALING)
                intro.position = coordinate
                self.intro_list.append(intro)
            lvl_0_instr = "Our Images/Intro/Instructions.png"
            instruction_coordinate_list = [[500, 360]]
            for coordinate in instruction_coordinate_list:
                instructions = arcade.Sprite(lvl_0_instr, TILE_SCALING * .3)
                instructions.position = coordinate
                self.instructions_list.append(instructions)
            # Placing fruit to take us into the game when collected
            fruit = "Our Images/Fruits/Cherry.png"
            cherry_coordinate_list = [[925, 175]]
            for coordinate in cherry_coordinate_list:
                cherry_instr = arcade.Sprite(fruit, FRUIT_SCALING * 1.8)
                cherry_instr.position = coordinate
                self.cherry_list.append(cherry_instr)

        # This level is the "model" level. Refer to this level and specifically
        # for any formatting and concerns.
        # Better yet, lets only have one option per level, and save us
        # a lot of extra hassle!
        if self.level == 1:
            # Originially we picked random orders for each level, but this made
            # the code needlessly longer and more of a hassle.

            # lvl_1_orders= ["Our Images/Orders/Lvl1/Order1.1.PNG", "Our Images/Orders/Lvl1/Order1.2.PNG",
            # "Our Images/Orders/Lvl1/Order1.3.PNG"]
            # rdm_lvl_1_order = rdm.choice(lvl_1_orders)
            if self.intro_playing:
                arcade.stop_sound(self.intro_player)
                self.intro_playing=False
            if not self.background_playing:
                self.background_music_player=arcade.play_sound(self.background_music, volume=0.02,looping=True)
                self.background_playing=True
            # Now, we use only one order per level.
            lvl_1_order = "Our Images/Orders/Lvl1/Order1.2.PNG"
            # Place Order:
            order_coordinate_list = [[950, 550]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(lvl_1_order, TILE_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)
            # Setup suckers
            self.Sucker_list.append(self.Sucker1)
            self.Sucker_list.append(self.Sucker2)
            self.Sucker_list.append(self.Sucker3)
            self.Sucker_list.append(self.Sucker4)
            for sucker in self.Sucker_list:
                Sucker_Movement(sucker)

                """This is the model level setup """
            self.revamped_fruit_list.append(self.Kiwi_coin)
            self.tier_1_fruit_list.append(self.Kiwi_coin)
            self.revamped_fruit_list.append(self.Pineapple_coin)
            self.tier_2_fruit_list.append(self.Pineapple_coin)
            self.revamped_fruit_list.append(self.Strawberry_coin)
            self.tier_3_fruit_list.append(self.Strawberry_coin)
            # Apply movement function to each fruit in the level
            for fruit in self.revamped_fruit_list:
                Basic_Fruit_Movement(fruit)
            arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        if self.level == 2:
            arcade.set_background_color(arcade.csscolor.LIGHT_YELLOW)
            lvl_2_order = "Our Images/Orders/Lvl2/Order1.2.PNG"
            # Place Order:
            order_coordinate_list = [[950, 530]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(lvl_2_order, TILE_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)

            # Setup suckers
            self.Sucker_list.append(self.Sucker1)
            self.Sucker_list.append(self.Sucker2)
            self.Sucker_list.append(self.Sucker3)
            self.Sucker_list.append(self.Sucker4)
            for sucker in self.Sucker_list:
                Sucker_Movement(sucker)

            """This is the model level setup """
            self.revamped_fruit_list.append(self.Watermelon_coin)
            self.tier_1_fruit_list.append(self.Watermelon_coin)
            self.revamped_fruit_list.append(self.Bannana_coin)
            self.tier_2_fruit_list.append(self.Bannana_coin)
            self.revamped_fruit_list.append(self.Grape_coin)
            self.tier_3_fruit_list.append(self.Grape_coin)
            self.revamped_fruit_list.append(self.Cherry_coin)
            self.tier_4_fruit_list.append(self.Cherry_coin)
            # Apply movement function to each fruit in the level
            for fruit in self.revamped_fruit_list:
                Basic_Fruit_Movement(fruit)

        if self.level == 3:
            arcade.set_background_color(arcade.csscolor.ORANGE)
            lvl_3_order = "Our Images/Orders/Lvl3/Lvl3Order1.1.PNG"
            # Place Order:
            order_coordinate_list = [[950, 510]]
            for coordinate in order_coordinate_list:
                orders = arcade.Sprite(lvl_3_order, TILE_SCALING)
                orders.position = coordinate
                self.orders_list.append(orders)

            # Setup suckers
            self.Sucker_list.append(self.Sucker1)
            self.Sucker_list.append(self.Sucker2)
            self.Sucker_list.append(self.Sucker3)
            self.Sucker_list.append(self.Sucker4)
            for sucker in self.Sucker_list:
                Sucker_Movement(sucker)

            # Set up fruits
            self.revamped_fruit_list.append(self.Pineapple_coin)
            self.tier_1_fruit_list.append(self.Pineapple_coin)
            self.revamped_fruit_list.append(self.Apple_coin)
            self.tier_2_fruit_list.append(self.Apple_coin)
            self.revamped_fruit_list.append(self.Plum_coin)
            self.tier_3_fruit_list.append(self.Plum_coin)
            self.revamped_fruit_list.append(self.Pear_coin)
            self.tier_4_fruit_list.append(self.Pear_coin)
            self.revamped_fruit_list.append(self.Orange_coin)
            self.tier_5_fruit_list.append(self.Orange_coin)
            # Apply movement function to each fruit in the level
            for fruit in self.revamped_fruit_list:
                Basic_Fruit_Movement(fruit)

        #End Screen
        if self.level==4:
            arcade.stop_sound(self.background_music_player)
            self.intro_player=arcade.play_sound(self.intro_theme,volume=0.02)
            arcade.set_background_color(arcade.csscolor.PALE_VIOLET_RED)
            # Placing everything related to the ending
            lvl_4 = "Our Images/Outro/Outro.PNG"
            ending_coordinate_list = [[500, 450]]
            for coordinate in ending_coordinate_list:
                ending = arcade.Sprite(lvl_4, TILE_SCALING * .37)
                ending.position = coordinate
                self.instructions_list.append(ending)
            fruit = "Our Images/Fruits/Cherry.png"
            cherry_coordinate_list = [[150, 175]]
            for coordinate in cherry_coordinate_list:
                cherry_instr = arcade.Sprite(fruit, FRUIT_SCALING * 1.8)
                cherry_instr.position = coordinate
                self.cherry_list_2.append(cherry_instr)
            door = "Our Images/Outro/pixel door.png"
            door_coordinate_list = [[890, 143]]
            for coordinate in door_coordinate_list:
                door_ = arcade.Sprite(door, FRUIT_SCALING * .75)
                door_.position = coordinate
                self.door_list.append(door_)
            self.player_sprite.set_position(500,PLAYER_START_Y)
            self.outro_list.append(self.Orange_boi)
            self.outro_list.append(self.Yellow_boi)
            self.outro_list.append(self.Blue_boi)
            self.outro_list.append(self.Purple_boi)
            self.outro_list.append(self.Red_boi)
            for item in self.outro_list:
                Basic_Fruit_Movement(item)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.orders_list.draw()
        self.instructions_list.draw()
        self.intro_list.draw()
        self.door_list.draw()
        self.cherry_list.draw()
        self.cherry_list_2.draw()
        self.outro_list.draw()
        #Draw suckers for levels not in the intro or outro
        if self.level != 0 or self.level != 4:
            self.Sucker_list.draw()

        # This will always draw the fruit for each level now:
        for fruit in self.revamped_fruit_list:
            fruit.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.ESCAPE:
            self.game_over = True
        elif key == arcade.key.P:
            self.skip_level = True
        elif key == arcade.key.O:
            self.reverse_level = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
        elif key == arcade.key.P:
            self.skip_level = False
        elif key == arcade.key.O:
            self.reverse_level = False

    def on_update(self, delta_time):
        """ Movement and game logic """
        if not self.game_over:
            # Move the player with the physics engine
            self.physics_engine.update()

            # Updating suckers
            self.Sucker_list.update()

            # Condensing our fruit update operations
            self.revamped_fruit_list.update()

            # New hitting ground function to optimize some things
            def Hitting_ground(fruits):
                """When fruit hits ground, this function will reset it"""
                fruits.bottom = FRUIT_SIZE * 9.75
                fruits.left = FRUIT_SIZE * rdm.randint(1, 14)
                fruits.change_y = rdm.randint(-4, -2)

            # Update suckers when they hit the ground
            for sucker in self.Sucker_list:
                if arcade.check_for_collision_with_list(sucker, self.wall_list):
                    Hitting_ground(sucker)
                    sucker.update()

            # Update each tier of fruit separately to manage shake and stacked conditions, which is still condensed
            # compared to updating every fruit on their own. All tiers can now be setup this way, with no need to
            # reference particular levels.
            for fruit in self.tier_1_fruit_list:
                if arcade.check_for_collision_with_list(fruit, self.wall_list):
                    Hitting_ground(fruit)
                    if self.Shake_1:
                        arcade.play_sound(self.fruit_hit_ground,volume=sound_effect_volume)
                    self.Shake_1 = False
                    self.Stacked_1 = False
                    fruit.update()
            for fruit in self.tier_2_fruit_list:
                if arcade.check_for_collision_with_list(fruit, self.wall_list):
                    Hitting_ground(fruit)
                    if self.Shake_2:
                        arcade.play_sound(self.fruit_hit_ground,volume=sound_effect_volume)
                    self.Shake_2 = False
                    self.Stacked_2 = False
                    fruit.update()
            for fruit in self.tier_3_fruit_list:
                if arcade.check_for_collision_with_list(fruit, self.wall_list):
                    Hitting_ground(fruit)
                    if self.Shake_3:
                        arcade.play_sound(self.fruit_hit_ground,volume=sound_effect_volume)
                    self.Shake_3 = False
                    self.Stacked_3 = False
                    fruit.update()
            for fruit in self.tier_4_fruit_list:
                if arcade.check_for_collision_with_list(fruit, self.wall_list):
                    Hitting_ground(fruit)
                    if self.Shake_4:
                        arcade.play_sound(self.fruit_hit_ground,volume=sound_effect_volume)
                    self.Shake_4 = False
                    self.Stacked_4 = False
                    fruit.update()
            for fruit in self.tier_5_fruit_list:
                if arcade.check_for_collision_with_list(fruit, self.wall_list):
                    Hitting_ground(fruit)
                    if self.Shake_5:
                        arcade.play_sound(self.fruit_hit_ground,volume=sound_effect_volume)
                    self.Shake_5 = False
                    self.Stacked_5 = False
                    fruit.update()

            # Stacking operations, each successive fruit will follow the previous fruit.
            # Occurs only when the previous fruit is stacked.
            for tier_1_fruit in self.tier_1_fruit_list:
                if arcade.check_for_collision(tier_1_fruit, self.player_sprite) and not self.Shake_1:
                    # Play good sound here when this occurs
                    tier_1_fruit.follow_sprite(self.player_sprite)
                    if not self.Stacked_1:
                        arcade.play_sound(self.picking_up_sound, volume=sound_effect_volume)
                    self.Stacked_1 = True
                for tier_2_fruit in self.tier_2_fruit_list:
                    if arcade.check_for_collision_with_list(tier_2_fruit, self.tier_1_fruit_list) and not self.Shake_2 \
                            and self.Stacked_1:
                        # Play good sound here when this occurs
                        tier_2_fruit.follow_sprite(tier_1_fruit)
                        if not self.Stacked_2:
                            arcade.play_sound(self.picking_up_sound, volume=sound_effect_volume)
                        self.Stacked_2 = True
                    for tier_3_fruit in self.tier_3_fruit_list:
                        if arcade.check_for_collision_with_list(tier_3_fruit, self.tier_2_fruit_list) \
                                and not self.Shake_3 \
                                and self.Stacked_2:
                            # Play good sound here when this occurs
                            tier_3_fruit.follow_sprite(tier_2_fruit)
                            if not self.Stacked_3:
                                arcade.play_sound(self.picking_up_sound, volume=sound_effect_volume)
                            self.Stacked_3 = True
                        for tier_4_fruit in self.tier_4_fruit_list:
                            if arcade.check_for_collision_with_list(tier_4_fruit, self.tier_3_fruit_list) \
                                    and not self.Shake_4 \
                                    and self.Stacked_3:
                                # Play good sound here when this occurs
                                tier_4_fruit.follow_sprite(tier_3_fruit)
                                if not self.Stacked_4:
                                    arcade.play_sound(self.picking_up_sound, volume=sound_effect_volume)
                                self.Stacked_4 = True
                            for tier_5_fruit in self.tier_5_fruit_list:
                                if arcade.check_for_collision_with_list(tier_5_fruit, self.tier_4_fruit_list) \
                                        and not self.Shake_5 \
                                        and self.Stacked_4:
                                    # Play good sound here when this occurs
                                    tier_5_fruit.follow_sprite(tier_4_fruit)
                                    if not self.Stacked_5:
                                        arcade.play_sound(self.picking_up_sound, volume=sound_effect_volume)
                                    self.Stacked_5 = True

            # Revamped collision system, if a sucker collides with fruit that is stacked, it will knock ONLY the top one off.
            for sucker in self.Sucker_list:
                if (((arcade.check_for_collision_with_list(sucker, self.tier_1_fruit_list)
                      and self.Stacked_1)) or
                    (arcade.check_for_collision_with_list(sucker, self.tier_2_fruit_list)
                     and self.Stacked_2) or
                    (arcade.check_for_collision_with_list(sucker, self.tier_3_fruit_list)
                     and self.Stacked_3) or
                    (arcade.check_for_collision_with_list(sucker, self.tier_4_fruit_list)
                     and self.Stacked_4)) \
                        and (not self.Shake_1 or not self.Shake_2 or not self.Shake_3 or not self.Shake_4
                             or not self.Shake_5):
                    if self.Stacked_4:
                        # Play bad sound here when this occurs.
                        if not self.Shake_4:
                            arcade.play_sound(self.losing_fruit_sound, volume=sound_effect_volume)
                        self.Shake_4=True
                    elif self.Stacked_3:
                        # Play bad sound here when this occurs.
                        if not self.Shake_3:
                            arcade.play_sound(self.losing_fruit_sound, volume=sound_effect_volume)
                        self.Shake_3=True
                    elif self.Stacked_2:
                        if not self.Shake_2:
                            # Play bad sound here when this occurs.
                            arcade.play_sound(self.losing_fruit_sound, volume=sound_effect_volume)
                        self.Shake_2 =True
                    elif self.Stacked_1:
                        if not self.Shake_1:
                            # Play bad sound here when this occurs.
                            arcade.play_sound(self.losing_fruit_sound, volume=sound_effect_volume)
                        self.Shake_1=True


            if len(arcade.check_for_collision_with_list(self.player_sprite,self.cherry_list)) > 0:
                self.instr_objective=True
            if len(arcade.check_for_collision_with_list(self.player_sprite,self.cherry_list_2)) > 0:
                self.restart_objective=True
            for item in self.outro_list:
                if arcade.check_for_collision_with_list(item,self.wall_list):
                    arcade.play_sound(self.burst_sound, volume=sound_effect_volume)
                    item.kill()
            self.outro_list.update()

            # See if the user got to the end of the level
            if self.level == 0:
                if self.instr_objective or self.skip_level:
                    # once we hit the cherry, go to next level
                    self.skip_level = False
                    self.instr_objective = False
                    self.level = 1
                    # Load the next level
                    self.setup(self.level)
            if self.level == 1:
                if self.reverse_level:
                    self.reverse_level=False
                    self.level=0
                    if self.background_playing:
                        arcade.stop_sound(self.background_music_player)
                        self.background_playing=False
                    self.setup(self.level)
                if self.Stacked_3 or self.skip_level:
                    self.skip_level = False
                    # once we hit 3 fruits, go to next level
                    self.level = 2
                    # Load the next level
                    self.setup(self.level)
                    self.Stacked_1 = False
                    self.Stacked_2 = False
                    self.Stacked_3 = False
                    self.Stacked_4 = False
                    self.Stacked_5 = False
            if self.level == 2:
                if self.reverse_level:
                    self.level=1
                    self.reverse_level=False
                    self.setup(self.level)
                if self.Stacked_4 or self.skip_level:
                    self.skip_level = False
                    # once we hit 4 fruits, go to next level
                    self.level = 3
                    # Load the next level
                    self.setup(self.level)
                    self.Stacked_1 = False
                    self.Stacked_2 = False
                    self.Stacked_3 = False
                    self.Stacked_4 = False
                    self.Stacked_5 = False
            if self.level == 3:
                if self.reverse_level:
                    self.reverse_level=False
                    self.level=2
                    self.setup(self.level)
                if self.Stacked_5 or self.skip_level:
                    self.skip_level = False
                    # once we hit 5 fruits, go to next level
                    self.level = 4
                    # Load the next level
                    self.setup(self.level)
                    self.Stacked_1 = False
                    self.Stacked_2 = False
                    self.Stacked_3 = False
                    self.Stacked_4 = False
                    self.Stacked_5 = False
            if self.level == 4:
                if self.restart_objective:
                        self.restart_objective=False
                        #once we hit the cherry, restart at level 1
                        self.level = 0
                        self.Stacked_1=False
                        self.Stacked_2=False
                        self.Stacked_3=False
                        self.Stacked_4=False
                        self.Stacked_5=False
                        # Load the next level
                        self.background_playing = False
                        arcade.stop_sound(self.intro_player)
                        self.setup(self.level)
            # See if the player walks to the door. If so, game over.
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.door_list)) > 0:
                self.game_over = True
        else:
            MyGame.close(self)


def main():
    """ Main method """
    window = MyGame()
    window.setup(window.level)
    arcade.run()



if __name__ == "__main__":
    main()