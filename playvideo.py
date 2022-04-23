from texttospeech import texttospeech 
def play_movie(path):
        from os import startfile
        startfile(path)
def playvideo():
    class Video(object):
        def __init__(self,path):
            self.path = path

        def play(self):
            from os import startfile
            startfile(self.path)

    class Movie_MP4(Video):
        type = "MP4"

    movie = Movie_MP4(r"C:\codde\video.mp4")
    movie.play()
    texttospeech("đã mở video")