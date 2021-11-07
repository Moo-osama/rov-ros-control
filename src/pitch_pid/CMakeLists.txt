cmake_minimum_required(VERSION 2.8.3)
project(pitch_pid)

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

add_executable(pitch_controller src/pitch_controller.cpp src/pitch_pid.cpp)
add_executable(pitch_plant_sim src/pitch_plant_sim.cpp)
add_executable(pitch_setpoint_node src/pitch_setpoint_node.cpp)
add_executable(pitch_sim_time src/pitch_sim_time.cpp)
add_executable(pitch_autotune src/pitch_autotune.cpp)

add_dependencies(pitch_controller ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(pitch_plant_sim ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(pitch_setpoint_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(pitch_sim_time ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(pitch_autotune ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(pitch_controller ${catkin_LIBRARIES})
target_link_libraries(pitch_plant_sim ${catkin_LIBRARIES})
target_link_libraries(pitch_setpoint_node ${catkin_LIBRARIES})
target_link_libraries(pitch_sim_time ${catkin_LIBRARIES})
target_link_libraries(pitch_autotune ${catkin_LIBRARIES})

install(TARGETS pitch_controller pitch_plant_sim pitch_setpoint_node pitch_sim_time pitch_autotune
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
