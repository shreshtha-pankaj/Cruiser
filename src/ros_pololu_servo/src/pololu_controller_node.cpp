/* Copyright (c) 2014, OpenCog Foundation
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the OpenCog Foundation nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#include <ros_pololu_servo/PololuController.h>

int main(int argc,char**argv)
{
    ros::init(argc, argv, "pololu_servo");
    PololuController controller;

    if(!controller.initialize())
    {
        ROS_INFO("Failed to initialize ros_polou_controller_node");
        return EXIT_FAILURE;
    }
    else
    {
        ROS_INFO("Successfully initialized ros_polou_controller_node");
    }

    ros::Rate rate(controller.get_rate_hz());

	while(ros::ok())
	{
//	    ROS_INFO("Publishing motor speed");
	    controller.publish_motor_state();
		ros::spinOnce();
        rate.sleep();
	}

	//controller.~PololuController();

	ROS_INFO("Exited ros_polou_controller_node");

	return EXIT_SUCCESS;
}
