#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools


class LibnameConan(ConanFile):
    name = "anax"
    scm = {
        "type": "git",
        "subfolder": "anax",
        "url": "https://github.com/miguelmartin75/anax.git",
        "revision": "11d310cdcae8a343171dd9b03b573781893d27f1"
    }
    version = scm["revision"][:7]
    description = "An open source C++ entity system"
    url = "https://github.com/bincrafters/conan-anax"
    homepage = "https://github.com/miguelmartin75/anax"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"fPIC": [True, False]}
    default_options = "fPIC=True"
    build_subfolder = "build_subfolder"

    def configure(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = False
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src="anax")
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
