cmake_minimum_required(VERSION 3.5)
project(simple_ros2)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(include)

add_library(simple_ros2 
			include/simple_ros2/minimal_publisher.hpp include/simple_ros2/minimal_publisher.cpp
			include/simple_ros2/simple_subscriber.hpp include/simple_ros2/simple_subscriber.cpp) 
ament_target_dependencies(simple_ros2 rclcpp std_msgs)
ament_export_targets(simple_ros2 HAS_LIBRARY_TARGET)

install(DIRECTORY include/simple_ros2
  DESTINATION include
)

install(DIRECTORY
  scripts
  src
  launch
  DESTINATION share/${PROJECT_NAME}
)

add_executable(minimal_publisher_node src/minimal_publisher_node.cpp)
target_link_libraries(minimal_publisher_node PUBLIC simple_ros2) 

add_executable(simple_subscriber_node src/simple_subscriber_node.cpp)
target_link_libraries(simple_subscriber_node PUBLIC simple_ros2) 

install(TARGETS 
	minimal_publisher_node
	simple_subscriber_node
  	DESTINATION lib/${PROJECT_NAME}/
)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  scripts/simple_pub.py
  scripts/simple_sub.py
  DESTINATION lib/${PROJECT_NAME}
)

install()
  
install(
  TARGETS simple_ros2
  EXPORT simple_ros2
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  RUNTIME DESTINATION bin
  INCLUDES DESTINATION include
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
