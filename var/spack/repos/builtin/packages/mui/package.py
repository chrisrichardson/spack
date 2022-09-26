# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mui(CMakePackage):
    """MUI Multiscale Universal Interface"""

    homepage = "https://mxui.github.io"
    git      = "https://github.com/MxUI/MUI.git"
    url      = "https://github.com/MxUI/MUI/archive/1.2.3.tar.gz"
    maintainers = ['SLongshaw', 'chrisrichardson']

    version('master', branch='master')
    version('1.2.3', sha256='18af78a7e9e2b04552db104dd14f6bf7a7e5425bbca92995a30a0302cdb1d319')

    variant('cwrapper', default=False, description='C wrappers')
    variant('fwrapper', default=False, description='FORTRAN wrappers')
    variant('rbf', default=False, description='Radial basis function support')

    depends_on("cmake@3.18:", type="build")
    depends_on("eigen@3.3:", type=("build", "run"), when="+rbf")

    def cmake_args(self):
        args = [
            "-DC_WRAPPER=%s" % (
                'ON' if "+cwrapper" in self.spec else 'OFF'),
            "-DFORTRAN_WRAPPER=%s" % (
                'ON' if "+fwrapper" in self.spec else 'OFF'),
            "-DUSE_RBF=%s" % (
                'ON' if "+rbf" in self.spec else 'OFF'),
        ]
        return args

