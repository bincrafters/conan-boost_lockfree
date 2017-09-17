from conans import ConanFile, tools, os

class BoostLockfreeConan(ConanFile):
    name = "Boost.Lockfree"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-lockfree"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["lockfree"]
    requires =  "Boost.Align/1.65.1@bincrafters/testing", \
                      "Boost.Array/1.65.1@bincrafters/testing", \
                      "Boost.Assert/1.65.1@bincrafters/testing", \
                      "Boost.Atomic/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Integer/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Parameter/1.65.1@bincrafters/testing", \
                      "Boost.Predef/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing", \
                      "Boost.Utility/1.65.1@bincrafters/testing"

                      #align3 array3 assert1 atomic4 config0 core2 integer3 mpl5 parameter10 predef0 static_assert1 tuple4 type_traits3 utility5
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()