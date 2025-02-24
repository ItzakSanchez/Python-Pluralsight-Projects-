class velocity():

    def __init__(self, heading, speed):
        self.heading = heading % 360

        if speed < 0:
            raise Exception("Speed can not be below 0")
        
        self.speed = speed