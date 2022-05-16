# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from os import symlink
from spack import *


class Novoalign(Package):
    """Powerful tool designed for mapping of short reads onto a reference
       genome from Illumina, Ion Torrent, and 454 NGS platforms."""

    homepage = "http://www.novocraft.com/products/novoalign/"
    url      = "file:///opt/htcf/src/novocraftV3.09.01.Linux3.10.0.tar.gz"

    version('4.03.02.Linux3.10.0', sha256='15da9c6f42ae88c0f9b67d8ebc94550a49c56b06cdaaf4a9268f4d0ccf6005a7')
    version('4.00.01.Linux3.10.0', sha256='dd37eb34523a775be9d7c6016d874bde184067247a3d108ee38da53f120036bc')
    version('4.00.00.Linux3.10.0', sha256='b2b79bb068a28b0edcba454cf9ba5b8caa138bac798a707f70741d99ebd38644')
    version('3.09.01.Linux3.10.0', sha256='08c9cef29ba9c10f81946e7287912982b009a54fb47a226302d99399c19a5b97')
    version('3.08.02.Linux3.10.0', sha256='2cebfab93567be203da693f592031f7557707cdb005382a0f9932a76e1129ba0')

    def install(self, spec, prefix):
        symlink('/opt/htcf/lic/novoalign.lic', 'novoalign.lic')
        install_tree('.', prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', self.prefix)
