from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_ros2',
            executable='minimal_publisher_node',
            name='minimal_publisher_node'
        ),
        Node(
            package='simple_ros2',
            executable='simple_subscriber_node',
            name='simple_subscriber_node'
        )
    ])
