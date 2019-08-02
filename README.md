# ROS Reality for the PR2

## Notes about this fork

This package is used for teleop with the PR2 so the original repo has been modified for that purpose. Changes made:
- All files related to the Baxter has been deleted
- The URDF of the PR2 has been updated and correctly formatted
- A camera plane that tilts with the tilt of the PR2 has added (useful when a computer doesn't have a powerful enough GPU to render the point cloud from the kinect)

## If you'd like to cite ROS Reality, see this paper:

Whitney, D., Rosen, E., Phillips, E., Konidaris, G. and Tellex, S., 2017. [Comparing Robot Grasping Teleoperation across Desktop and Virtual Reality with ROS Reality.](http://cs.brown.edu/people/gdk/pubs/vr_teleop.pdf) In Proceedings of the International Symposium on Robotics Research.


Hi! Welcome to ROS Reality, a package made by the [Humans to Robots Lab](http://h2r.cs.brown.edu/) at [Brown](https://en.wikipedia.org/wiki/Brown) University. This package connects a ROS network to a Unity scene over the internet, passing messages back and forth. We also wrote a C# [URDF](http://wiki.ros.org/urdf) parser, which you can find demoed in the provided scenes.

## Installation
1. Download and install Unity 2017.4. ([Linux download link](https://beta.unity3d.com/download/fbeab28dc46b/public_download.html) and [instructions](https://askubuntu.com/a/1078159))
2. Install [git LFS](https://git-lfs.github.com/). This is required to download the big PR2 mesh files.
3. Clone this repo in your catkin workspace and build it

## Scenes
There are 2 scenes (Position Control and Trajectory Control); however, we only activley use Position Control. Position Control visualises the PR2 and an image plane from the kinect that moves with the tilt of the PR2's head. Code in `ros_reality/Assets/Scripts` can also be modified to include the kinect's point cloud in the scene.

We currently use [this repo](https://github.com/ipab-rad/htc_vive_teleop_stuff) to control the arms of the PR2.

## Running ROS Reality

Run `roslaunch ros_reality_pr2 ros_reality_pr2.launch` to launch the rosbridge_server and Unity.

Once Unity starts, launch the Position Control scene and then:
- select the WebsocketClient game object and set the IP address to that of the computer running the ros nodes for the PR2 (use `ifconfig` to find the IP) and set the port to `8080`. (Example: `ws://192.168.106.24:8080`)
- select the `RobotFactory` game object and set the Xml Path to `pr2.xml` in `ros_reality/Assets/Resources/URDFs/PR2`. (Example: `/home/user/catkin_ws/src/ros_reality_pr2/ros_reality/Assets/Resources/URDFs/PR2/pr2.xml`)
- save the scene and press play

You should be able to see the PR2 and if not, look at the console in Unity to debug the errors. To move the starting position of the robot, move the camera in the scene (the initial position of the PR2 is set up for our working environmnet).

If your kinect and PR2 topics are different from the default topic names, change them in `CameraListener.cs` in  `ros_reality/Assets/Scripts`.




