#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostLockfreeConan(base.BoostBaseConan):
    name = "boost_lockfree"
    url = "https://github.com/bincrafters/conan-boost_lockfree"
    lib_short_names = ["lockfree"]
    header_only_libs = ["lockfree"]
    b2_requires = [
        "boost_align",
        "boost_array",
        "boost_assert",
        "boost_atomic",
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_iterator",
        "boost_mpl",
        "boost_parameter",
        "boost_predef",
        "boost_static_assert",
        "boost_tuple",
        "boost_type_traits",
        "boost_utility"
    ]
