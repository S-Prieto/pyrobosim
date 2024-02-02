from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    # Arguments
    world_file_arg = DeclareLaunchArgument(
        "world_file",
        default_value="",
        description="YAML file name (should be in the pyrobosim/data folder). "
        + "If not specified, a world will be created programmatically.",
    )

    # Nodes
    demo_node = Node(
        package="pyrobosim_ros",
        executable="task_planner.py",
        name="task_planner",
        parameters=[{"world_file": LaunchConfiguration("world_file")}],
    )

    return LaunchDescription([world_file_arg, demo_node])
