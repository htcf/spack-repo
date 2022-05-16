# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Foo(PythonPackage):
    """Foo"""

    homepage = "https://foo.com/"
    pypi     = "foo/foo-1.0.0.tar.gz"

    version('1.0.0', sha256='1234')

    depends_on('python@3.4.0:', type=('build', 'run'))
    depends_on('py-tqdm', type=('build', 'run'))
    depends_on('py-h5py', type=('build', 'run'))
    depends_on('py-numba@0.54.0', type=('build', 'run'))

