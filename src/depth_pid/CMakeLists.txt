cmake_minimum_required(VERSION 2.8.3)
project(depth_pid)

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

add_executable(depth_controller src/depth_controller.cpp src/depth_pid.cpp)
add_executable(depth_plant_sim src/depth_plant_sim.cpp)
add_executable(depth_setpoint_node src/depth_setpoint_node.cpp)
add_executable(depth_sim_time src/depth_sim_time.cpp)
add_executable(depth_autotune src/depth_autotune.cpp)

add_dependencies(depth_controller ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(depth_plant_sim ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(depth_setpoint_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(depth_sim_time ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(depth_autotune ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(depth_controller ${catkin_LIBRARIES})
target_link_libraries(depth_plant_sim ${catkin_LIBRARIES})
target_link_libraries(depth_setpoint_node ${catkin_LIBRARIES})
target_link_libraries(depth_sim_time ${catkin_LIBRARIES})
target_link_libraries(depth_autotune ${catkin_LIBRARIES})

install(TARGETS depth_controller depth_plant_sim depth_setpoint_node depth_sim_time depth_autotune
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
