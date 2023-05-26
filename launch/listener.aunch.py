from launch import LaunchDescription
from launch.action import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'demo_nodes_py',
            executable= 'listener'
        )
    ])