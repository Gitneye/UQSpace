from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('my_robot'),
        'config',
        'params.yaml'
    )

    my_node = Node(
        package="my_robot_controller",
        executable="test_node",
        name="test_params",
        namespace="ns1",
        parameters=[config]
    )

    talker_node = Node(
        package="demo_nodes_cpp",
        executable="talker",
        name="my_talker",
        remappings= [
            ("chatter","my_chatter")
        ],
        parameters= [
            {"param_name": "value"},
            {"param2": 19}
        ]
    )

    listener_node = Node(
        package="demo_nodes_py",
        executable="listener",
        remappings= [
            ("chatter","my_chatter")
        ]
    )

    ld.add_action(talker_node)
    ld.add_action(listener_node)

    return ld

