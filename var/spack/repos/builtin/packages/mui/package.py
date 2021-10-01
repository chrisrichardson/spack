# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mui(CMakePackage):
    """MUI Multiscale Universal Interface"""

    homepage = "https://mxui.github.io"
    git      = "https://github.com/MxUI/MUI.git"
    url      = "https://github.com/MxUI/MUI"
    maintainers = ['SLongshaw', 'chrisrichardson']

    version('master', branch='master')

    variant('cwrapper', default=False, description='C wrappers')

    depends_on("cmake@3.18:", type="build")

    def cmake_args(self):
        args = [
            "-DC_WRAPPER=%s" % (
                'ON' if "+cwrapper" in self.spec else 'OFF'),
        ]
        return args

