# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

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
CMAKE_SOURCE_DIR = /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/opencv/capstone/facedetection/build

# Include any dependencies generated for this target.
include classification_sample_async/CMakeFiles/classification_sample_async.dir/depend.make

# Include the progress variables for this target.
include classification_sample_async/CMakeFiles/classification_sample_async.dir/progress.make

# Include the compile flags for this target's objects.
include classification_sample_async/CMakeFiles/classification_sample_async.dir/flags.make

classification_sample_async/CMakeFiles/classification_sample_async.dir/main.cpp.o: classification_sample_async/CMakeFiles/classification_sample_async.dir/flags.make
classification_sample_async/CMakeFiles/classification_sample_async.dir/main.cpp.o: /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/classification_sample_async/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object classification_sample_async/CMakeFiles/classification_sample_async.dir/main.cpp.o"
	cd /home/pi/opencv/capstone/facedetection/build/classification_sample_async && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/classification_sample_async.dir/main.cpp.o -c /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/classification_sample_async/main.cpp

classification_sample_async/CMakeFiles/classification_sample_async.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/classification_sample_async.dir/main.cpp.i"
	cd /home/pi/opencv/capstone/facedetection/build/classification_sample_async && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/classification_sample_async/main.cpp > CMakeFiles/classification_sample_async.dir/main.cpp.i

classification_sample_async/CMakeFiles/classification_sample_async.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/classification_sample_async.dir/main.cpp.s"
	cd /home/pi/opencv/capstone/facedetection/build/classification_sample_async && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/classification_sample_async/main.cpp -o CMakeFiles/classification_sample_async.dir/main.cpp.s

# Object files for target classification_sample_async
classification_sample_async_OBJECTS = \
"CMakeFiles/classification_sample_async.dir/main.cpp.o"

# External object files for target classification_sample_async
classification_sample_async_EXTERNAL_OBJECTS =

armv7l/Release/classification_sample_async: classification_sample_async/CMakeFiles/classification_sample_async.dir/main.cpp.o
armv7l/Release/classification_sample_async: classification_sample_async/CMakeFiles/classification_sample_async.dir/build.make
armv7l/Release/classification_sample_async: /opt/intel/openvino/deployment_tools/inference_engine/lib/armv7l/libinference_engine_legacy.so
armv7l/Release/classification_sample_async: /opt/intel/openvino/deployment_tools/inference_engine/lib/armv7l/libinference_engine.so
armv7l/Release/classification_sample_async: /opt/intel/openvino/deployment_tools/inference_engine/lib/armv7l/libinference_engine_c_api.so
armv7l/Release/classification_sample_async: armv7l/Release/lib/libformat_reader.so
armv7l/Release/classification_sample_async: armv7l/Release/lib/libgflags_nothreads.a
armv7l/Release/classification_sample_async: classification_sample_async/CMakeFiles/classification_sample_async.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../armv7l/Release/classification_sample_async"
	cd /home/pi/opencv/capstone/facedetection/build/classification_sample_async && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/classification_sample_async.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
classification_sample_async/CMakeFiles/classification_sample_async.dir/build: armv7l/Release/classification_sample_async

.PHONY : classification_sample_async/CMakeFiles/classification_sample_async.dir/build

classification_sample_async/CMakeFiles/classification_sample_async.dir/clean:
	cd /home/pi/opencv/capstone/facedetection/build/classification_sample_async && $(CMAKE_COMMAND) -P CMakeFiles/classification_sample_async.dir/cmake_clean.cmake
.PHONY : classification_sample_async/CMakeFiles/classification_sample_async.dir/clean

classification_sample_async/CMakeFiles/classification_sample_async.dir/depend:
	cd /home/pi/opencv/capstone/facedetection/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/classification_sample_async /home/pi/opencv/capstone/facedetection/build /home/pi/opencv/capstone/facedetection/build/classification_sample_async /home/pi/opencv/capstone/facedetection/build/classification_sample_async/CMakeFiles/classification_sample_async.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : classification_sample_async/CMakeFiles/classification_sample_async.dir/depend

