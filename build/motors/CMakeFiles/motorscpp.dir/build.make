# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mahfouz/fuckin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mahfouz/fuckin_ws/build

# Include any dependencies generated for this target.
include motors/CMakeFiles/motorscpp.dir/depend.make

# Include the progress variables for this target.
include motors/CMakeFiles/motorscpp.dir/progress.make

# Include the compile flags for this target's objects.
include motors/CMakeFiles/motorscpp.dir/flags.make

motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o: motors/CMakeFiles/motorscpp.dir/flags.make
motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o: /home/mahfouz/fuckin_ws/src/motors/src/motors.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mahfouz/fuckin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o"
	cd /home/mahfouz/fuckin_ws/build/motors && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/motorscpp.dir/src/motors.cpp.o -c /home/mahfouz/fuckin_ws/src/motors/src/motors.cpp

motors/CMakeFiles/motorscpp.dir/src/motors.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/motorscpp.dir/src/motors.cpp.i"
	cd /home/mahfouz/fuckin_ws/build/motors && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mahfouz/fuckin_ws/src/motors/src/motors.cpp > CMakeFiles/motorscpp.dir/src/motors.cpp.i

motors/CMakeFiles/motorscpp.dir/src/motors.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/motorscpp.dir/src/motors.cpp.s"
	cd /home/mahfouz/fuckin_ws/build/motors && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mahfouz/fuckin_ws/src/motors/src/motors.cpp -o CMakeFiles/motorscpp.dir/src/motors.cpp.s

motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.requires:

.PHONY : motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.requires

motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.provides: motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.requires
	$(MAKE) -f motors/CMakeFiles/motorscpp.dir/build.make motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.provides.build
.PHONY : motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.provides

motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.provides.build: motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o


# Object files for target motorscpp
motorscpp_OBJECTS = \
"CMakeFiles/motorscpp.dir/src/motors.cpp.o"

# External object files for target motorscpp
motorscpp_EXTERNAL_OBJECTS =

/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: motors/CMakeFiles/motorscpp.dir/build.make
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/libroscpp.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/librosconsole.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/librostime.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /opt/ros/kinetic/lib/libcpp_common.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp: motors/CMakeFiles/motorscpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mahfouz/fuckin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp"
	cd /home/mahfouz/fuckin_ws/build/motors && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/motorscpp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
motors/CMakeFiles/motorscpp.dir/build: /home/mahfouz/fuckin_ws/devel/lib/motors/motorscpp

.PHONY : motors/CMakeFiles/motorscpp.dir/build

motors/CMakeFiles/motorscpp.dir/requires: motors/CMakeFiles/motorscpp.dir/src/motors.cpp.o.requires

.PHONY : motors/CMakeFiles/motorscpp.dir/requires

motors/CMakeFiles/motorscpp.dir/clean:
	cd /home/mahfouz/fuckin_ws/build/motors && $(CMAKE_COMMAND) -P CMakeFiles/motorscpp.dir/cmake_clean.cmake
.PHONY : motors/CMakeFiles/motorscpp.dir/clean

motors/CMakeFiles/motorscpp.dir/depend:
	cd /home/mahfouz/fuckin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mahfouz/fuckin_ws/src /home/mahfouz/fuckin_ws/src/motors /home/mahfouz/fuckin_ws/build /home/mahfouz/fuckin_ws/build/motors /home/mahfouz/fuckin_ws/build/motors/CMakeFiles/motorscpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : motors/CMakeFiles/motorscpp.dir/depend

