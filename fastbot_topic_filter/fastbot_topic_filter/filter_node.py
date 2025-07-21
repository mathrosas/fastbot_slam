#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

class DuplicateFilter(Node):
    def __init__(self):
        super().__init__('duplicate_filter')
        self.last_odom_stamp = None
        self.last_scan_stamp = None

        self.odom_pub = self.create_publisher(Odometry, '/fastbot_1/odom_filtered', 10)
        self.scan_pub = self.create_publisher(LaserScan, '/fastbot_1/scan_filtered', 10)

        self.create_subscription(Odometry,   '/fastbot_1/odom', self.odom_callback, 10)
        self.create_subscription(LaserScan, '/fastbot_1/scan', self.scan_callback, 10)

    def odom_callback(self, msg):
        if self.last_odom_stamp != msg.header.stamp:
            self.last_odom_stamp = msg.header.stamp
            self.odom_pub.publish(msg)

    def scan_callback(self, msg):
        if self.last_scan_stamp != msg.header.stamp:
            self.last_scan_stamp = msg.header.stamp
            self.scan_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DuplicateFilter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
