from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_ros2',
            executable='simple_pub.py',
            name='simple_pub'
        ),
        Node(
            package='simple_ros2',
            executable='simple_sub.py',
            name='simple_sub'
        )
    ])
