from src.frame import Frame
from src.timeline import TimeLine


def build_motion():
    """Build our motion graphy dynamically!"""

    frame1 = Frame(text='Farhaaaaaaaaaaaaaaaaaaaaaaaaad', background='assets/farhad.png')
    frame1.make_frame()
    frame1.save(filename='FARHAD.png')

    frame2 = Frame(text='Salaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaam', background='assets/saeed.png')
    frame2.make_frame()
    frame2.save(filename='Saeed.png')

    timeline = TimeLine(fps=0.1)
    timeline.add_frame(frame1)
    timeline.add_frame(frame2)

    timeline.build()


if __name__ == '__main__':
    build_motion()
