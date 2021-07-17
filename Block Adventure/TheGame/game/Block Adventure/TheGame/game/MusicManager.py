
import arcade

class MusicManager:
    

    def play_song(self, levelCurrentlyIn):
       
        self.music_list = ["cdk_-_cdk_-_Sunday.mp3", "cdkMain.mp3"]

        songNumberToPlay = 0
        VolumeToPlayAt = 0.5
        # auto checks what song to play 
        """
        if levelCurrentlyIn
        """
        
        loopSong = True
        self.music = arcade.Sound(self.music_list[songNumberToPlay], streaming=True)
        self.current_player = self.music.play(VolumeToPlayAt, 0, loopSong)
        
    
        

    




    