import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node

def generate_launch_description():

    slam_params = {
        'use_sim_time': True,
        'odom_frame': 'odom',
        'map_frame': 'map',
        'base_frame': 'base_link',
        'scan_topic': '/scan',
        'mode': 'mapping',
        'resolution': 0.05,
        'max_laser_range': 10.0,
        'minimum_travel_distance': 0.1,
        'minimum_travel_heading': 0.1,
        'map_update_interval': 5.0,
        'transform_publish_period': 0.02,
    }

    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[slam_params],
    )

    # Delay SLAM by 5 seconds to let Gazebo + robot_state_publisher start first
    delayed_slam = TimerAction(period=5.0, actions=[slam_node])

    return LaunchDescription([delayed_slam])
