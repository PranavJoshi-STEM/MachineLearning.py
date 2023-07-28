# MachineLearning

# GOAL:
This was a project I created in grade 8 during the spring break.  My goal for this project was to create a modular and advanced program which utilizes machine learning.

# HOW I CREATED IT:
This needs Pygame (available via "sudo pip3 install pygame") and Python 3 to run.  I created the machine-learning system myself.


# THE MACHINE LEARNING:
While I could've used a library such as Tensorflow, I decided to create my own machine-learning system.  This program is very simple and is supposed to get the player square to the Yay square.  How it works is by getting the player to check all adjacent squares (the square above, below, left and right) except (if the ability is turned on) the last square it visisted, it sees which one has the highest score.  Once it compares all adjacent squares except the last square it was just in (if PLAYER = {..., "ignore_previous_square":True, ...} is written in function SQUARE_RESOURCES), and sees the highest-scored tile, it moves to it and adds it to it's list of squares it moved to in its generation.  The player tile continues doing this until it hits either the Kill or Yay square.  If it hits the Kill square, all squares it just visited that generartion will decrease by a point and if it hits the Yay square, all squares it visited in the generation will increase by a point.  Eventually, the robot finds out a way to safely navigate around and get to the Yay square all the time.

To see this in action, check out the "screenshots" folder attached.  Keep in mind these things when the video is playing:
- The robot can only go up, down, left or right but may ignore the last square it just visited (to encourage productivity and movement) and will always choose the square with the highest points.
- The robot will move randomly in generation 1 due to it having no data on the surrounding squares.  
- If it succeeds/fails, all squares it visited in that genration will increase/decrease in a point respectively.
