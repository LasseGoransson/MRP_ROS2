from gpiozero import CamJamKitRobot 
import time

def main():
    # Main function
    print("Booting MotorController")
    robot = CamJamKitRobot()

    print("Main")
    # Turn the motors on
    robot.forward()

    # Wait for 1 seconds
    time.sleep(1)

    # Turn the motors off
    robot.stop()
