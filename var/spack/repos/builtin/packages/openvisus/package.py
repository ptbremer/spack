##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install openvisus
#
# You can edit this file again by typing:
#
#     spack edit openvisus
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Openvisus(Package):
    """Open source distribution of the ViSUS visualization system"""

    # For now we link to the git page. We could also link to visus.org
    homepage = "https://github.com/sci-visus/OpenVisus"
    git      = "https://github.com/sci-visus/OpenVisus.git"

    version('master',branch='master',commit='e3d8d8e')

    variant('static',     default=False,
            description="Builds with a static version of Qt to allow self-contained distribution.")

    extends('python')
    
    depends_on('zlib')
    depends_on('lz4')
    depends_on('tinyxml')
    depends_on('openssl')
    depends_on('curl')
    depends_on('swig')
    depends_on('python@3:')
    depends_on('py-numpy')
 
    depends_on('qt+opengl')
    #depends_on('qt+opengl+static',when='static')
    
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DVISUS_INTERNAL_ZLIB=0',
                '-DVISUS_INTERNAL_LZ4=0',
                '-DVISUS_INTERNAL_TINYXML=0',
                '-DVISUS_INTERNAL_OPENSSL=0',
                '-DVISUS_INTERNAL_CURL=0',
                '-DVISUS_INTERNAL_PYTHON=0',
                '-DCMAKE_SKIP_RPATH=1']
        return args

    
