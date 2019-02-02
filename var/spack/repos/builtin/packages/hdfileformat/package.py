# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install hdfileformat-git
#
# You can edit this file again by typing:
#
#     spack edit hdfileformat-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Hdfileformat(CMakePackage):
    """High-Dimensional File Format"""
    
    homepage = "https://bitbucket.org/cedmav/hdfileformat/src/master/"
    git      = "git@bitbucket.org:cedmav/hdfileformat.git"

    version('2019-01-28', commit='40b115e')

    variant('python', default=False, description='Build the python extension')

    #import_modules = ['hdff']
  
    # FIXME: Add dependencies if required.
    extends('python',when='+python')
    depends_on('python', when='+python')
    depends_on('py-numpy', when='+python')
    
    def cmake_args(self):

        args = []
        if '+python' in self.spec:
            args = ["-DENABLE_PYTHON=1"]

        return args

    
    
    