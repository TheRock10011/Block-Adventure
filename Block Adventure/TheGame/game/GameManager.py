"""
  Sprite Move With Walls
  
  Simple program to show basic sprite usage.
  
  Artwork from http://kenney.nl
  
  If Python and Arcade are installed, this example can be run from the command line with:
  python -m arcade.examples.sprite_move_walls
"""

from tkinter.constants import NONE
import arcade
import os
from game.CreateLevel import CreatingLevel
from game.Goal import Goal
from game import constants
from game.move_actors_action import Movement
from game.MakeAllSprites import MakeAllSprites
from game.MusicManager import MusicManager





class MyGame(arcade.Window):
    """ Main application class. """
    def AddArcadeSprite(self, sprite):
        sprite = arcade.SpriteList()
    def MakeSprite(self, sprite, spriteURL):
        sprite = arcade.Sprite(spriteURL, constants.SPRITE_SCALING)

    def __init__(self, width, height, title):

       
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        MakeAllSprites.Inside__init__(self)
        # Sprite lists
        self.LevelIn = 1
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.pit_list = None

        # Set up the player
        self.player_sprite = None
        self.pit_sprite = None
        self.physics_engine = None
        self.conveyerUp_list = None
        self.conveyerDown_list = None
        self.conveyerLeft_list = None
        self.conveyerRight_list = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        #MakeAllSprites.Insidesetup(self)
        # Sprite lists
        MusicManager.play_song(self, self.LevelIn)
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()
        self.conveyerUp_list = arcade.SpriteList()
        self.conveyerDown_list = arcade.SpriteList()
        self.conveyerLeft_list = arcade.SpriteList()
        self.conveyerRight_list = arcade.SpriteList()
        self.goal_sprite = arcade.Sprite("Star.png", 
                                            constants.SPRITE_SCALING)
        # Set up the player
        self.player_sprite = arcade.Sprite("MainBlock.png",
                                           constants.SPRITE_SCALING)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0

        
        self.goal_list.append(self.goal_sprite)

        self.player_list.append(self.player_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list, )
        self.pit_list = arcade.SpriteList() 


        # -- Set up the walls
        # Create a row of boxes
        self.LoadLevel(2)
        

        

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        #MakeAllSprites.Insideon_draw(self)
        self.goal_list.draw()
        # Draw all the sprites.
        self.wall_list.draw()
        self.pit_list.draw()
        self.conveyerUp_list.draw()  
        self.conveyerDown_list.draw()  
        self.conveyerLeft_list.draw()  
        self.conveyerRight_list.draw()  
        self.player_list.draw()
        

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.CheckGameObjects()
       # Call update on all sprites (The sprites don't do much in this
       # example though.)
        self.physics_engine.update()
        #from asciimatics.event import KeyboardEvent
        #MovePlayer = Movement().on_key_release(self.key, self)
        pressedUp = Movement().checkUpKey(self.key)
        pressedDown = Movement().checkDownKey(self.key)
        pressedLeft = Movement().checkLeftKey(self.key)
        pressedRight = Movement().checkRightKey(self.key)
        MovePlayer = Movement().movePlayer(pressedUp, pressedDown, pressedLeft, pressedRight)
        if(pressedUp or pressedDown or pressedLeft or pressedRight):
            self.player_sprite.change_y = MovePlayer[0]
            self.player_sprite.change_x = MovePlayer[1]

        

    def LoadLevel(self, LevelNumberToAdd):
        self.LevelIn += LevelNumberToAdd
        newLevel = CreatingLevel.LoadNextLevel(self, self.LevelIn)
        self.MakeLevel(newLevel)
        
        self.player_sprite.change_y = 0
        self.player_sprite.change_x = 0
        
        #if(self.LevelIn == 3):
           #self.LevelIn = 1
    #Will Load next level

    def DeleteLevel(self):
        for i in range(len(self.wall_list)):
            self.wall_list.pop()
        for i in range(len(self.pit_list)):
            self.pit_list.pop()
        for i in range(len(self.conveyerUp_list)):
            self.conveyerUp_list.pop()
        for i in range(len(self.conveyerDown_list)):
            self.conveyerDown_list.pop()
        for i in range(len(self.conveyerLeft_list)):
            self.conveyerLeft_list.pop()
        for i in range(len(self.conveyerRight_list)):
            self.conveyerRight_list.pop()

    
    def MakeLevel(self, theLevel):
        self.DeleteLevel()
        #Takes a [] to make level.
        #0 for nothing, 1 for wall, 2 for goal, and 3 for player. 4 for pit tile
        #5 for up conveyer, 6 for down conveyer, 7 for left conveyer, and 8 for right converyer. 
        TheX = 0 # 20
        TheY = constants.SCREEN_HEIGHT # 14
        
        
        for x in range(len(theLevel)):#130 should be he number
            
            #Makes a wall
            if theLevel[x] == 1:
                wall = arcade.Sprite("Block.png", constants.SPRITE_SCALING)
                wall.center_x = TheX
                wall.center_y = TheY
                self.wall_list.append(wall)
            #Makes the goal
            if theLevel[x] == 2:
                self.goal_sprite.center_x = TheX
                self.goal_sprite.center_y = TheY
            
                
            if theLevel[x] == 3:
                #Moves The player to the correct location
                self.player_sprite.center_x = TheX
                self.player_sprite.center_y = TheY
            if theLevel[x] == 4:
                pit = arcade.Sprite("pit.png", 
                                            constants.SPRITE_SCALING)
                pit.center_x = TheX
                pit.center_y = TheY
                self.pit_list.append(pit)
                #self.scene.add_sprite("Pit", pit)
            if theLevel[x] == 5:

                conveyerUp = arcade.Sprite("UpConveyer.png", 
                                            constants.SPRITE_SCALING)
                conveyerUp.center_x = TheX
                conveyerUp.center_y = TheY
                self.conveyerUp_list.append(conveyerUp)
            if theLevel[x] == 6:
                conveyerDown = arcade.Sprite("DownConveyer.png", 
                                            constants.SPRITE_SCALING)
                conveyerDown.center_x = TheX
                conveyerDown.center_y = TheY
                self.conveyerDown_list.append(conveyerDown)
            if theLevel[x] == 7:
                conveyerLeft = arcade.Sprite("LeftConveyer.png", 
                                            constants.SPRITE_SCALING)
                conveyerLeft.center_x = TheX
                conveyerLeft.center_y = TheY
                self.conveyerLeft_list.append(conveyerLeft)
            if theLevel[x] == 8:

                conveyerRight = arcade.Sprite("RightConveyer.png", 
                                            constants.SPRITE_SCALING)
                conveyerRight.center_x = TheX
                conveyerRight.center_y = TheY
                self.conveyerRight_list.append(conveyerRight)    

            
            TheX += 64
            if TheX > constants.SCREEN_WIDTH :
                TheY -=64
                TheX = 0


    #Will Do this every frame
    def CheckGameObjects(self):
        hitGoal = Goal.checkGoalCollission(self, self.player_sprite.center_x, self.player_sprite.center_y,
        self.goal_sprite.center_x,self.goal_sprite.center_y)
        if hitGoal:
            self.LoadLevel(1)
        hitPit = False
        hitPit = arcade.check_for_collision_with_list(
            self.player_sprite, self.pit_list)
        if hitPit:
            self.LoadLevel(0)
        
        hitConveyerUp = arcade.check_for_collision_with_list(
            self.player_sprite, self.conveyerUp_list)
        hitConveyerDown = arcade.check_for_collision_with_list(
            self.player_sprite, self.conveyerDown_list)
        hitConveyerLeft = arcade.check_for_collision_with_list(
            self.player_sprite, self.conveyerLeft_list)
        hitConveyerRight = arcade.check_for_collision_with_list(
            self.player_sprite, self.conveyerRight_list)
        if hitConveyerUp:

            self.player_sprite.center_y  += constants.CONVEYOR_SPEED
        if hitConveyerDown:
            self.player_sprite.center_y  += -constants.CONVEYOR_SPEED
        if hitConveyerLeft:
            self.player_sprite.center_x  += -constants.CONVEYOR_SPEED
        if hitConveyerRight:
            self.player_sprite.center_x  += constants.CONVEYOR_SPEED