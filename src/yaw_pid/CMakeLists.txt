cmake_minimum_required(VERSION 2.8.3)
project(yaw_pid)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  dynamic_reconfigure
)

generate_dynamic_reconfigure_options(
    cfg/Pid.cfg
)

catkin_package(
  INCLUDE_DIRS include
   CATKIN_DEPENDS roscpp std_msgs message_runtime dynamic_reconfigure
)

include_directories(include
  ${catkin_INCLUDE_DIRS}
  ${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake
)

add_executable(yaw_controller src/yaw_controller.cpp src/yaw_pid.cpp)
add_executable(yaw_plant_sim src/yaw_plant_sim.cpp)
add_executable(yaw_setpoint_node src/yaw_setpoint_node.cpp)
add_executable(yaw_sim_time src/yaw_sim_time.cpp)
add_executable(yaw_autotune src/yaw_autotune.cpp)

add_dependencies(yaw_controller ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(yaw_plant_sim ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(yaw_setpoint_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(yaw_sim_time ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(yaw_autotune ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(yaw_controller ${catkin_LIBRARIES})
target_link_libraries(yaw_plant_sim ${catkin_LIBRARIES})
target_link_libraries(yaw_setpoint_node ${catkin_LIBRARIES})
target_link_libraries(yaw_sim_time ${catkin_LIBRARIES})
target_link_libraries(yaw_autotune ${catkin_LIBRARIES})

install(TARGETS yaw_controller yaw_plant_sim yaw_setpoint_node yaw_sim_time yaw_autotune
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
  PATTERN ".svn" EXCLUDE
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
