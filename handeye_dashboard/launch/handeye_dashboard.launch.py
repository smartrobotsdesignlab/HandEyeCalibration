import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import  PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare



def generate_launch_description():

    # URDF file to be loaded by Robot State Publisher
    rqt_config = os.path.join(
        get_package_share_directory('handeye_dashboard'), 
            'config', 'Default.perspective'
    )
    
    return LaunchDescription( [
        # Include Hand Eye Server
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare("handeye_target_detection"), 'launch', 'pose_estimation.launch.py'])),
        ),
        # Robot State Publisher
        Node(package='handeye_tf_service', executable='handeye_tf_server',
             output='screen'),

        # Rviz2
        Node(package='rqt_gui', executable='rqt_gui',
             output='screen', arguments=['--perspective-file', rqt_config]),
    ])