from conans import ConanFile, tools, os

class BoostLockfreeConan(ConanFile):
    name = "Boost.Lockfree"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-lockfree"
    source_url = "https://github.com/boostorg/lockfree"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["lockfree"]
    requires =  "Boost.Align/1.64.0@bincrafters/testing", \
                      "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Atomic/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Parameter/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing"

                      #align3 array3 assert1 atomic4 config0 core2 integer3 mpl5 parameter10 predef0 static_assert1 tuple4 type_traits3 utility5
                      
    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()