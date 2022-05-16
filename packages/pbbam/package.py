# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pbbam(MesonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/PacificBiosciences/pbbam/archive/refs/tags/v2.1.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.1.0', sha256='605944f09654d964ce12c31d67e6766dfb1513f730ef5d4b74829b2b84dd464f')

    # FIXME: Add dependencies if required.
    depends_on('zlib')
    depends_on('boost@1.73 ')
    depends_on('htslib', type=('build', 'run'))
    depends_on('samtools')
    depends_on('doxygen+graphviz')

    def setup_build_environment(self, env):
        env.set('BOOST_ROOT', self.spec['boost'].prefix)

    def meson_args(self):
        # FIXME: If not needed delete this function
        args = []
        return args
