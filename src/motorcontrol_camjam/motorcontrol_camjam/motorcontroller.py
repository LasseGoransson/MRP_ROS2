from gpiozero import CamJamKitRobot 
import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class CamJamMotorController(Node):

    def __init__(self,robot):
        super().__init__('CamJamMotorController')
        self.subscription = self.create_subscription(
            Float32,
            'drive',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.robot = robot

    def setDrive(self, drive_val):
        # Determine direction
        if drive_val > 0:
            self.robot.forward(drive_val)
        elif drive_val == 0:
            self.robot.stop()
        elif drive_val < 0:
            self.robot.reverse(drive_val)



        


def main(args=None):
    rclpy.init(args=args)
    robot = CamJamKitRobot()

    motorcontroller = CamJamMotorController(robot)

    rclpy.spin(motorcontroller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motorcontroller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()