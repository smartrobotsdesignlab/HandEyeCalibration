# Copyright (c) 2019 Intel Corporation. All Rights Reserved
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import launch
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import  PathJoinSubstitution, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Declare arguments
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "runtime_config_package",
            default_value="handeye_target_detection",
            description='Package with the calibration bord\'s configuration in "launch" folder. \
        Usually the argument is not set, it enables use of a custom setup.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "config_file",
            default_value="pose_estimation.yaml",
            description="YAML file with the calibration board configuration.",
        )
    )
    # Initialize Arguments
    runtime_config_package = LaunchConfiguration("runtime_config_package")
    config_file = LaunchConfiguration("config_file")

    # .yaml file for configuring the parameters
    detection_config_file = PathJoinSubstitution(
        [
            FindPackageShare(runtime_config_package),
            "launch",
            config_file,
        ]
    )


    estimation_node = Node(
        package="handeye_target_detection",
        executable="pose_estimation",
        output="screen",
        parameters=[detection_config_file],
    )

    nodes = [estimation_node]

    return launch.LaunchDescription(declared_arguments + nodes)