from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout


class Pdkdf2Conan(ConanFile):
    name = "pdkdf2"
    version = "1.0.0"
    package_type = "library"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = (
        "CMakeLists.txt",
        "src/*",
        "include/*",
    )

    def requirements(self):
        self.requires("boost/1.84.0")
        self.requires("openssl/3.2.1")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.get_safe("shared"):
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.components["pdkdf2"].libs = ["pdkdf2"]
        self.cpp_info.components["pdkdf2"].requires = [
            "boost::program_options",
            "openssl::ssl",
            "openssl::crypto",
        ]
        self.cpp_info.components["pdkdf2"].set_property("cmake_target_name", "pdkdf2::pdkdf2")
