"""
    A container for all frames.
"""
from src.frame import Frame


class TimeLine:

    def __init__(self, fps):
        self.frames = []  # list of Frame class
        self.fps = fps

    def add_frame(self, frame: Frame):
        self.frames.append(frame)

    def get_frame(self, frame_id):
        return self.frames[frame_id]

    def build(self):
        """Join all frames"""
        print(">> Building...")
        import os
        import moviepy.video.io.ImageSequenceClip

        image_folder = '/home/farhad/Downloads/motion-builder/motion-builder/'
        image_files = [os.path.join(image_folder, img)
                       for img in os.listdir(image_folder)
                       if img.endswith(".png")]

        print(image_files)

        # image_files = ['FARHAD.png',
        #                '/home/farhad/Downloads/motion-builder/motion-builder/Saeed.png']
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=self.fps)
        clip.write_videofile('my_video.mp4')
