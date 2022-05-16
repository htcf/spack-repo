# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bam2fastx(MesonPackage):
    "Conversion of PacBio BAM files into gzipped fasta and fastq files, including splitting of barcoded data"

    homepage = "https://github.com/PacificBiosciences/bam2fastx"
    url      = "https://github.com/PacificBiosciences/bam2fastx/archive/refs/tags/1.3.1.tar.gz"

    version('1.3.1', sha256='4a6e305a631002b2da5bc57341a85f5cf424be832c2c80a6775d0d86965f8ed1')

    depends_on('boost')
    depends_on('pbbam')

    def setup_build_environment(self, env):
        env.set('BOOST_ROOT', self.spec['boost'].prefix)

    def meson_args(self):
        # FIXME: If not needed delete this function
        args = []
        return args

