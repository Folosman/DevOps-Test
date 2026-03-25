cmake_minimum_required(VERSION 3.21)
project(test_package LANGUAGES CXX)

find_package(pdkdf2 REQUIRED CONFIG)
find_package(Boost REQUIRED COMPONENTS program_options)

add_executable(test_package src/main.cpp)
target_link_libraries(test_package PRIVATE pdkdf2::pdkdf2 Boost::program_options)

target_compile_features(test_package PRIVATE cxx_std_17)
