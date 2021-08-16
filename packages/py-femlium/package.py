# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyFemlium(PythonPackage):
    '''Interactive visualization of finite element simulations on geographic
    maps with folium.
    '''

    homepage = 'https://femlium.github.io/'
    url      = 'https://github.com/FEMlium/FEMlium/'
    git      = 'https://github.com/FEMlium/FEMlium/'
    
    version('develop', branch='master')

    variant('firedrake', default=True, description='Use the Firedrake backend')

    depends_on('py-branca')  # TODO
    depends_on('py-firedrake', when='+firedrake')
    depends_on('py-folium')  # TODO
    depends_on('py-geojson')  # TODO
    depends_on('py-matplotlib')
    depends_on('py-numpy')
    depends_on('py-pyproj')
    depends_on('py-setuptools', type='build')
