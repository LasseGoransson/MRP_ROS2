from gpiozero import CamJamKitRobot 
import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class CamJamMotorController(Node):

    def __init__(self,robot):
        super().__init__('CamJamMotorController')
        self.drive_subscription = self.create_subscription(
            Float32,
            'drive',
            self.listener_callback,
            10)
        
        self.drive_publish = self.create_publisher(
            Float32,
            'drive_current'
            10
        )
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.pushDrive)
        self.drive_subscription  # prevent unused variable warning
        self.robot = robot
        self.currentDrive = 0
    
    def pushDrive(self):
        msg = Float32()
        msg.data = self.currentDrive
        self.publisher_.publish(msg)

    def setDrive(self, drive_val):
        # Determine direction
        if drive_val > 0:
            self.robot.forward(drive_val)
        elif drive_val == 0:
            self.robot.stop()
        elif drive_val < 0:
            self.robot.reverse(drive_val)
        self.currentDrive = drive_val



        


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