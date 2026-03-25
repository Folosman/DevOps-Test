cmake_minimum_required(VERSION 3.21)
project(pdkdf2 VERSION 1.0.0 LANGUAGES CXX)

option(BUILD_SHARED_LIBS "Build shared libs" OFF)

find_package(OpenSSL REQUIRED)
find_package(Boost REQUIRED COMPONENTS program_options)

add_library(pdkdf2
    src/args_parser.cxx
    src/main.cxx
)

add_library(pdkdf2::pdkdf2 ALIAS pdkdf2)

target_include_directories(pdkdf2
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)

target_compile_features(pdkdf2 PUBLIC cxx_std_17)

target_link_libraries(pdkdf2
    PUBLIC
        Boost::program_options
        OpenSSL::SSL
        OpenSSL::Crypto
)

include(GNUInstallDirs)

install(TARGETS pdkdf2
    EXPORT pdkdf2Targets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

install(EXPORT pdkdf2Targets
    FILE pdkdf2Targets.cmake
    NAMESPACE pdkdf2::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/pdkdf2
)
