# CRUISER
This is a final project for the Advanced Robotics Class (CSCI 5***) offered at CU Boulder under Professor Chris Heckmann

## Capabilities
1. Completing the pre designated race track in under 20 seconds
2. Backing out of a collision
3. Avoiding a Rolling Ball
4. Stop sign Detection

## Hardware
1. Intel Real Sense D435i
2. Odroid XU4 (Ubuntu 16.04)
3. Polulu
4. Motor
5. Batteries 

# Software Packages and Language
For this project, we are using C++ and Python2.7
1. Intel Real Sense SDK
2. ROS
3. OpenCV

## Nodes along with their capabilities
1. color_stream (pkg camera): C++ node that publishes RGB data with params for image resolution and frame rate
2. depth_stream (pkg camera): C++ node that publishes Depth data from the Intel Re
3. stop_sign (pkg stop_sign)
4. master_state_machine (pkg state_machine)

## Launch Files

### Main launch files
1. For Race: 
``` roslaunch state_machine master.launch```
2. For Backing out of a collision:
``` roslaunch state_machine backoff.launch```
3. For Stop sign detection:
``` roslaunch stop_sign stop_sign.launch```
4. For avoiding a rolling ball:
``` roslaunch state_machine backoff.launch```

### Helper Launch files
5. To test the polulu:
``` roslaunch state_machine tester.launch```
6. To test the camera:
```roslaunch camera camera.launch```

## Topics
1. Depth data: /camera/depth
2. RGB Data: /camera/image
3. Stop Sign: /is_stop_sign
4. TODO: To be added

