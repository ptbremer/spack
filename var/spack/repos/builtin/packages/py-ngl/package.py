# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNgl(PythonPackage):
    """A Python utility that compute Nearest Neighbor Graphs"""

    homepage = "http://www.ngraph.org/"
    git      = "ssh://git@cz-bitbucket.llnl.gov:7999/nddav/ngl.git"

    version('2019-01-28', commit='12ce4f4754f')

    depends_on('py-numpy')
