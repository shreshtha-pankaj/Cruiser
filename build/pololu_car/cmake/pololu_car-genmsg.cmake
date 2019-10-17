# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(FATAL_ERROR "Could not find messages which '/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorState.msg' depends on. Did you forget to specify generate_messages(DEPENDENCIES ...)?
Cannot locate message [MotorCalibration]: unknown package [ros_pololu_servo] on search path [{'pololu_car': ['/home/karan/advanced_robotics_ws/src/pololu_car/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}]")
message(FATAL_ERROR "Could not find messages which '/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorStateList.msg' depends on. Did you forget to specify generate_messages(DEPENDENCIES ...)?
Cannot locate message [MotorState]: unknown package [ros_pololu_servo] on search path [{'pololu_car': ['/home/karan/advanced_robotics_ws/src/pololu_car/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}]")
message(STATUS "pololu_car: 4 messages, 0 services")

set(MSG_I_FLAGS "-Ipololu_car:/home/karan/advanced_robotics_ws/src/pololu_car/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg;-Itrajectory_msgs:/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(pololu_car_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg" NAME_WE)
add_custom_target(_pololu_car_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pololu_car" "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg" ""
)

get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg" NAME_WE)
add_custom_target(_pololu_car_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pololu_car" "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_car
)
_generate_msg_cpp(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_car
)

### Generating Services

### Generating Module File
_generate_module_cpp(pololu_car
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_car
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(pololu_car_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(pololu_car_generate_messages pololu_car_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_cpp _pololu_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_cpp _pololu_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_car_gencpp)
add_dependencies(pololu_car_gencpp pololu_car_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_car_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_car
)
_generate_msg_eus(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_car
)

### Generating Services

### Generating Module File
_generate_module_eus(pololu_car
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_car
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(pololu_car_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(pololu_car_generate_messages pololu_car_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_eus _pololu_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_eus _pololu_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_car_geneus)
add_dependencies(pololu_car_geneus pololu_car_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_car_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_car
)
_generate_msg_lisp(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_car
)

### Generating Services

### Generating Module File
_generate_module_lisp(pololu_car
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_car
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(pololu_car_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(pololu_car_generate_messages pololu_car_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_lisp _pololu_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_lisp _pololu_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_car_genlisp)
add_dependencies(pololu_car_genlisp pololu_car_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_car_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_car
)
_generate_msg_nodejs(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_car
)

### Generating Services

### Generating Module File
_generate_module_nodejs(pololu_car
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_car
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(pololu_car_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(pololu_car_generate_messages pololu_car_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_nodejs _pololu_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_nodejs _pololu_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_car_gennodejs)
add_dependencies(pololu_car_gennodejs pololu_car_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_car_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_car
)
_generate_msg_py(pololu_car
  "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_car
)

### Generating Services

### Generating Module File
_generate_module_py(pololu_car
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_car
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(pololu_car_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(pololu_car_generate_messages pololu_car_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCalibration.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_py _pololu_car_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/karan/advanced_robotics_ws/src/pololu_car/msg/MotorCommand.msg" NAME_WE)
add_dependencies(pololu_car_generate_messages_py _pololu_car_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pololu_car_genpy)
add_dependencies(pololu_car_genpy pololu_car_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pololu_car_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_car)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pololu_car
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(pololu_car_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(pololu_car_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()
if(TARGET trajectory_msgs_generate_messages_cpp)
  add_dependencies(pololu_car_generate_messages_cpp trajectory_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_car)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pololu_car
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(pololu_car_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(pololu_car_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()
if(TARGET trajectory_msgs_generate_messages_eus)
  add_dependencies(pololu_car_generate_messages_eus trajectory_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_car)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pololu_car
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(pololu_car_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(pololu_car_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()
if(TARGET trajectory_msgs_generate_messages_lisp)
  add_dependencies(pololu_car_generate_messages_lisp trajectory_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_car)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pololu_car
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(pololu_car_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(pololu_car_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()
if(TARGET trajectory_msgs_generate_messages_nodejs)
  add_dependencies(pololu_car_generate_messages_nodejs trajectory_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_car)
  install(CODE "execute_process(COMMAND \"/home/karan/anaconda3/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_car\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pololu_car
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(pololu_car_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(pololu_car_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
if(TARGET trajectory_msgs_generate_messages_py)
  add_dependencies(pololu_car_generate_messages_py trajectory_msgs_generate_messages_py)
endif()
