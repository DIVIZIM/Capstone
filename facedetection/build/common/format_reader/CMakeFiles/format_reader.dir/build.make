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
include common/format_reader/CMakeFiles/format_reader.dir/depend.make

# Include the progress variables for this target.
include common/format_reader/CMakeFiles/format_reader.dir/progress.make

# Include the compile flags for this target's objects.
include common/format_reader/CMakeFiles/format_reader.dir/flags.make

common/format_reader/CMakeFiles/format_reader.dir/MnistUbyte.cpp.o: common/format_reader/CMakeFiles/format_reader.dir/flags.make
common/format_reader/CMakeFiles/format_reader.dir/MnistUbyte.cpp.o: /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/MnistUbyte.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object common/format_reader/CMakeFiles/format_reader.dir/MnistUbyte.cpp.o"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/format_reader.dir/MnistUbyte.cpp.o -c /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/MnistUbyte.cpp

common/format_reader/CMakeFiles/format_reader.dir/MnistUbyte.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/format_reader.dir/MnistUbyte.cpp.i"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/MnistUbyte.cpp > CMakeFiles/format_reader.dir/MnistUbyte.cpp.i

common/format_reader/CMakeFiles/format_reader.dir/MnistUbyte.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/format_reader.dir/MnistUbyte.cpp.s"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/MnistUbyte.cpp -o CMakeFiles/format_reader.dir/MnistUbyte.cpp.s

common/format_reader/CMakeFiles/format_reader.dir/bmp.cpp.o: common/format_reader/CMakeFiles/format_reader.dir/flags.make
common/format_reader/CMakeFiles/format_reader.dir/bmp.cpp.o: /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/bmp.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object common/format_reader/CMakeFiles/format_reader.dir/bmp.cpp.o"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/format_reader.dir/bmp.cpp.o -c /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/bmp.cpp

common/format_reader/CMakeFiles/format_reader.dir/bmp.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/format_reader.dir/bmp.cpp.i"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/bmp.cpp > CMakeFiles/format_reader.dir/bmp.cpp.i

common/format_reader/CMakeFiles/format_reader.dir/bmp.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/format_reader.dir/bmp.cpp.s"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/bmp.cpp -o CMakeFiles/format_reader.dir/bmp.cpp.s

common/format_reader/CMakeFiles/format_reader.dir/format_reader.cpp.o: common/format_reader/CMakeFiles/format_reader.dir/flags.make
common/format_reader/CMakeFiles/format_reader.dir/format_reader.cpp.o: /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/format_reader.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object common/format_reader/CMakeFiles/format_reader.dir/format_reader.cpp.o"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/format_reader.dir/format_reader.cpp.o -c /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/format_reader.cpp

common/format_reader/CMakeFiles/format_reader.dir/format_reader.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/format_reader.dir/format_reader.cpp.i"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/format_reader.cpp > CMakeFiles/format_reader.dir/format_reader.cpp.i

common/format_reader/CMakeFiles/format_reader.dir/format_reader.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/format_reader.dir/format_reader.cpp.s"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/format_reader.cpp -o CMakeFiles/format_reader.dir/format_reader.cpp.s

common/format_reader/CMakeFiles/format_reader.dir/opencv_wraper.cpp.o: common/format_reader/CMakeFiles/format_reader.dir/flags.make
common/format_reader/CMakeFiles/format_reader.dir/opencv_wraper.cpp.o: /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/opencv_wraper.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object common/format_reader/CMakeFiles/format_reader.dir/opencv_wraper.cpp.o"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/format_reader.dir/opencv_wraper.cpp.o -c /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/opencv_wraper.cpp

common/format_reader/CMakeFiles/format_reader.dir/opencv_wraper.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/format_reader.dir/opencv_wraper.cpp.i"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/opencv_wraper.cpp > CMakeFiles/format_reader.dir/opencv_wraper.cpp.i

common/format_reader/CMakeFiles/format_reader.dir/opencv_wraper.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/format_reader.dir/opencv_wraper.cpp.s"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader/opencv_wraper.cpp -o CMakeFiles/format_reader.dir/opencv_wraper.cpp.s

# Object files for target format_reader
format_reader_OBJECTS = \
"CMakeFiles/format_reader.dir/MnistUbyte.cpp.o" \
"CMakeFiles/format_reader.dir/bmp.cpp.o" \
"CMakeFiles/format_reader.dir/format_reader.cpp.o" \
"CMakeFiles/format_reader.dir/opencv_wraper.cpp.o"

# External object files for target format_reader
format_reader_EXTERNAL_OBJECTS =

armv7l/Release/lib/libformat_reader.so: common/format_reader/CMakeFiles/format_reader.dir/MnistUbyte.cpp.o
armv7l/Release/lib/libformat_reader.so: common/format_reader/CMakeFiles/format_reader.dir/bmp.cpp.o
armv7l/Release/lib/libformat_reader.so: common/format_reader/CMakeFiles/format_reader.dir/format_reader.cpp.o
armv7l/Release/lib/libformat_reader.so: common/format_reader/CMakeFiles/format_reader.dir/opencv_wraper.cpp.o
armv7l/Release/lib/libformat_reader.so: common/format_reader/CMakeFiles/format_reader.dir/build.make
armv7l/Release/lib/libformat_reader.so: /opt/intel/openvino/opencv/lib/libopencv_videoio.so.4.4.0
armv7l/Release/lib/libformat_reader.so: /opt/intel/openvino/opencv/lib/libopencv_imgcodecs.so.4.4.0
armv7l/Release/lib/libformat_reader.so: /opt/intel/openvino/opencv/lib/libopencv_imgproc.so.4.4.0
armv7l/Release/lib/libformat_reader.so: /opt/intel/openvino/opencv/lib/libopencv_core.so.4.4.0
armv7l/Release/lib/libformat_reader.so: common/format_reader/CMakeFiles/format_reader.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/opencv/capstone/facedetection/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX shared library ../../armv7l/Release/lib/libformat_reader.so"
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/format_reader.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
common/format_reader/CMakeFiles/format_reader.dir/build: armv7l/Release/lib/libformat_reader.so

.PHONY : common/format_reader/CMakeFiles/format_reader.dir/build

common/format_reader/CMakeFiles/format_reader.dir/clean:
	cd /home/pi/opencv/capstone/facedetection/build/common/format_reader && $(CMAKE_COMMAND) -P CMakeFiles/format_reader.dir/cmake_clean.cmake
.PHONY : common/format_reader/CMakeFiles/format_reader.dir/clean

common/format_reader/CMakeFiles/format_reader.dir/depend:
	cd /home/pi/opencv/capstone/facedetection/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp /opt/intel/openvino/deployment_tools/inference_engine/samples/cpp/common/format_reader /home/pi/opencv/capstone/facedetection/build /home/pi/opencv/capstone/facedetection/build/common/format_reader /home/pi/opencv/capstone/facedetection/build/common/format_reader/CMakeFiles/format_reader.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : common/format_reader/CMakeFiles/format_reader.dir/depend

