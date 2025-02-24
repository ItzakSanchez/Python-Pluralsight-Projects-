import velocity 

class robot:

    def __init__(self, velocity):
        self.velocity = velocity
    
    def motion_evaluation(self, nearfieldDetected = False):
        if nearfieldDetected and self.velocity.speed > 0:
            self.velocity.speed -= 1
