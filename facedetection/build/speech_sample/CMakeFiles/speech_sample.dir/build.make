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
include speech_sample/CMakeFiles/speech_sample.dir/depend.make

# Include the progress variables for this target.
include speech_sample/CMakeFiles/speech_sample.dir/progress.make

# Include the compile flags for this target's objects.
include speech_sample/CMakeFiles/speech_sample.dir/flags.make

speech_sample/CMakeFiles/speech_sample.dir/main.cpp.o: speech_sample/CMakeFiles/speech_sample.dir/flags.make
speech_sample/CMakeFiles/speech_sample.dir/main.cpp.o: /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/speech_sample/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object speech_sample/CMakeFiles/speech_sample.dir/main.cpp.o"
	cd /home/pi/opencv/capstone/facedetection/build/speech_sample && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/speech_sample.dir/main.cpp.o -c /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/speech_sample/main.cpp

speech_sample/CMakeFiles/speech_sample.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/speech_sample.dir/main.cpp.i"
	cd /home/pi/opencv/capstone/facedetection/build/speech_sample && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/speech_sample/main.cpp > CMakeFiles/speech_sample.dir/main.cpp.i

speech_sample/CMakeFiles/speech_sample.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/speech_sample.dir/main.cpp.s"
	cd /home/pi/opencv/capstone/facedetection/build/speech_sample && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/speech_sample/main.cpp -o CMakeFiles/speech_sample.dir/main.cpp.s

# Object files for target speech_sample
speech_sample_OBJECTS = \
"CMakeFiles/speech_sample.dir/main.cpp.o"

# External object files for target speech_sample
speech_sample_EXTERNAL_OBJECTS =

armv7l/Release/speech_sample: speech_sample/CMakeFiles/speech_sample.dir/main.cpp.o
armv7l/Release/speech_sample: speech_sample/CMakeFiles/speech_sample.dir/build.make
armv7l/Release/speech_sample: /opt/intel/openvino/deployment_tools/inference_engine/lib/armv7l/libinference_engine_legacy.so
armv7l/Release/speech_sample: /opt/intel/openvino/deployment_tools/inference_engine/lib/armv7l/libinference_engine.so
armv7l/Release/speech_sample: /opt/intel/openvino/deployment_tools/inference_engine/lib/armv7l/libinference_engine_c_api.so
armv7l/Release/speech_sample: armv7l/Release/lib/libgflags_nothreads.a
armv7l/Release/speech_sample: speech_sample/CMakeFiles/speech_sample.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../armv7l/Release/speech_sample"
	cd /home/pi/opencv/capstone/facedetection/build/speech_sample && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/speech_sample.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
speech_sample/CMakeFiles/speech_sample.dir/build: armv7l/Release/speech_sample

.PHONY : speech_sample/CMakeFiles/speech_sample.dir/build

speech_sample/CMakeFiles/speech_sample.dir/clean:
	cd /home/pi/opencv/capstone/facedetection/build/speech_sample && $(CMAKE_COMMAND) -P CMakeFiles/speech_sample.dir/cmake_clean.cmake
.PHONY : speech_sample/CMakeFiles/speech_sample.dir/clean

speech_sample/CMakeFiles/speech_sample.dir/depend:
	cd /home/pi/opencv/capstone/facedetection/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/speech_sample /home/pi/opencv/capstone/facedetection/build /home/pi/opencv/capstone/facedetection/build/speech_sample /home/pi/opencv/capstone/facedetection/build/speech_sample/CMakeFiles/speech_sample.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : speech_sample/CMakeFiles/speech_sample.dir/depend

