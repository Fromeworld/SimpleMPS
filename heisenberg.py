# -*- encoding: utf-8

# SimpleMPS
# Density matrix renormalization group (DMRG) in matrix product state (MPS)

# This file contains the definition of matrix product operators in Heisenberg model,
# then performs ground state search based on MPS.
# For theoretical backgrounds, see the [reference]:
# Ulrich Schollwöck, The density-matrix renormalization group in the age of matrix product states,
# Annals of Physics, 326 (2011), 96-192

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from mps import MatrixProductState, build_mpo_list
# import pauli matrices
from paulimat import *


# coupling constant
J = Jz = 1

# Strength of external field
h = 1

# MPO line by line
_W1 = [S1,    S0,     S0,     S0,    S0]
_W2 = [Sp,    S0,     S0,     S0,    S0]
_W3 = [Sm,    S0,     S0,     S0,    S0]
_W4 = [Sz,    S0,     S0,     S0,    S0]
_W5 = [-h*Sz, J/2*Sm, J/2*Sp, Jz*Sz, S1]

# W shape: 5, 5, 2, 2
W = np.float64([_W1, _W2, _W3, _W4, _W5])
# prohibit writing for safety concerns
W.flags.writeable = False

# number of sites
SITE_NUM = 20

BOND_ORDER = 16

if __name__ == '__main__':
    MatrixProductState(BOND_ORDER, build_mpo_list(W, SITE_NUM)).optimize()