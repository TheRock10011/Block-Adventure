
class MakeAllSprites:
    
    def Inside__init__(self):
        self.grass_list = None
        self.grass_sprite = None
    def Insidesetup(self):
        from game.GameManager import MyGame
        MyGame.AddArcadeSprite(self, self.grass_list)
        MyGame.MakeSprite(self, self.grass_sprite, ":resources:images/enemies/slimeBlock.png")
        
        #self.players_list = arcade.SpriteList()
        #self.grass_sprite.center_x = 0
        #self.grass_sprite.center_y = 0
        self.grass_list.append(self.player_sprite)
    def Insideon_draw(self):
        self.grass_list.draw()