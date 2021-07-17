from game import constants
import arcade
from asciimatics.event import KeyboardEvent

class Movement():
  
   def checkUpKey(self, key):
      if key == arcade.key.UP:
         return True
      
   def checkDownKey(self, key):
      if key == arcade.key.DOWN:
         return True
   def checkLeftKey(self, key):
      if key == arcade.key.LEFT:
         return True
   def checkRightKey(self, key):
      if key == arcade.key.RIGHT:
         return True
   def movePlayer(self, up, down, left, right):
      NewXY = [0,0]
      if up:
           #self.player_sprite.change_y = constants.MOVEMENT_SPEED
         NewXY[0] = constants.MOVEMENT_SPEED
         
      if down:
            #self.player_sprite.change_y = -constants.MOVEMENT_SPEED
         NewXY[0] = -constants.MOVEMENT_SPEED
         
      if left:
           #self.player_sprite.change_x = -constants.MOVEMENT_SPEED
         NewXY[1] = -constants.MOVEMENT_SPEED
         
      if right:
     
         NewXY[1] = constants.MOVEMENT_SPEED
        
      return NewXY




   #def on_key_press(self, key, modifiers):
      """Called whenever a key is pressed. """
         
      #NewXY = [0,0]
      #if key == arcade.key.UP:
           #self.player_sprite.change_y = constants.MOVEMENT_SPEED
         #NewXY[0] = constants.MOVEMENT_SPEED
        # print("Moved")
     # if key == arcade.key.DOWN:
            #self.player_sprite.change_y = -constants.MOVEMENT_SPEED
         #NewXY[0] = -constants.MOVEMENT_SPEED
         #print("Moved")
      #if key == arcade.key.LEFT:
           #self.player_sprite.change_x = -constants.MOVEMENT_SPEED
         #NewXY[1] = -constants.MOVEMENT_SPEED
         #print("Moved")
      #if key == arcade.key.RIGHT:
           #self.player_sprite.change_x = constants.MOVEMENT_SPEED
         #NewXY[1] = constants.MOVEMENT_SPEED
        # print("Moved")
        # print(NewXY)
      #return NewXY

   def on_key_release(self, key, modifiers):
      """Called when the user releases a key. """
      NewXY = [0,0]
      if key == arcade.key.UP or key == arcade.key.DOWN:
           #self.player_sprite.change_y = 0
         NewXY[0] = 0
           
      elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            #self.player_sprite.change_x = 0
         NewXY[1] = 0
            
      return NewXY
   
