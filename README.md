# HandEyeCalibration

## Configuration

The calibration configuration file is `handeye_target_detection/launch/pose_estimation.yaml`.

The parameters descripiton:

- pattern

    You can review the patterns on `handeye_target_detection/data/pattern`.

    And the example result on  `handeye_target_detection/data/detected`.

    By default, we are using the *CHARUCO*, this pattern looks could be directly printed by A4 size paper. If you have other standard calibration pattern board, you could also set the parameters reference on the file `handeye_target_detection/src/pose_estimation_node.cpp`, under the "Get parameters" comments.
    Such as: chessboard_square_size and dictionary.

- image_topic

    The image from camera. Please check this topic when running the camera by `ros2 topic list`.

- camera_info_topic

    The camera intrinsic parameters topic. Usually, it will be published by the camera ros node. Also check it on the topic list.

- publish_image_topic

    The result for preview, usually don't need to change it. You need show this image result on the rviz for real-time monitori.

- width & height & dictionary & charuco_board**

    The pattern parameters. Details reference the pattern.

## How to use

After change the configuration file, please remember `colcon build` the workspace, default ros2 dosen't update the yaml files automatically.

*Moveit is recommanded here. Remember to switch the trajectory controller for moveit.*

### Run the detect node.

  `ros2 run handeye_target_detection pose_estimation`

  After that, you could add the detect display on the Moveit rviz2 for monitoring the detected result.

### Launch the dashboard.

`ros2 launch handeye_dashboard handeye_dashboard.launch.py`

On the dashboard, you need to set the TF informations, this is very important!

- Change the installation method from "fixed beside robot" or "attached on robot".
- Check the tf frame of your camera carefully.
- Set the camera frame, end effector frame and robot base frame.
- You don't need to care about object frame, leave it default.

### Start calibration

Moving the robot until the result is shown well on the result image topic. Then click the calibration button. If everything setup well, you could see the transformation result on the terminal, and it is not Identity matrix.

Then repeat it as 8-10 times.

Make sure that there are different orientations and positions.


### Result

After 8-10 times, click the get result, it will calculates the extrinsic parameters by regression. And the result will be shown on the dashboard.

You could also click the pub_tf button, to preview the camera position on the rviz2, by adding the tf plugin.

The result file is on the `/tmp/camera-robot.txt`, it saves the transformations, quaternion and Eular angular.

## Something should be noted

The result usually could not be directly used, such as this matrix multiplying a point on the camera frame. It might be some error on the rotation. For example, the realsense, it has camera_color_frame, and camera_optical_frame.

You could show these frames on the rviz2 for better understanding.

And you could also configure the camera on the urdf by using the transformation and Eular angular.
