# Copyright (C) 2020 Jørgen Schartum Dokken
#
# This file is part of DOLFINX_MPC
#
# SPDX-License-Identifier:    LGPL-3.0-or-later
"""Main module for DOLFINX_MPC"""

# flake8: noqa

import dolfinx_mpc.cpp

# New local assemblies
from .assemble_matrix import assemble_matrix, assemble_matrix_cpp, \
    create_matrix_nest, assemble_matrix_nest
from .assemble_vector import assemble_vector, create_vector_nest, \
    assemble_vector_nest
from .multipointconstraint import MultiPointConstraint
from .problem import LinearProblem
