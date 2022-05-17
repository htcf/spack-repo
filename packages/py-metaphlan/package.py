# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMetaphlan(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/biobakery/MetaPhlAn/archive/refs/tags/3.0.14.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.0.14', sha256='6553a0e7e027e4b26feab0fa50418da45331d318bb1406020b8e6a376b1772c0')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    depends_on('python@3:')
    depends_on('py-numpy')
    depends_on('py-h5py')
    depends_on('py-biom-format')
    depends_on('py-biopython')
    depends_on('py-pandas')
    depends_on('py-scipy')
    depends_on('py-requests')
    depends_on('py-dendropy')
    depends_on('py-pysam')
    depends_on('py-cmseq')
    depends_on('py-phylophlan')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
