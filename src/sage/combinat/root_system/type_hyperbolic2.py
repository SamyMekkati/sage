"""
Hyperbolic Coxeter types.
"""
# ****************************************************************************
#       Copyright (C) 2025 Samy Mekkati <samy.mekkati.1@ens.etsmtl.ca>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#  The full text of the GPL is available at:
#
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from sage.combinat.root_system.coxeter_type import CoxeterType
from sage.combinat.root_system.level2_hyperbolic_matrices import (level2_matrices)


class CoxeterType_Level2_Hyperbolic(CoxeterType):
    r"""
    Hyperbolic level 2 Coxeter type
    """
    def __init__(self, data):

        if data[0] in ["K4", "K4dK2", "K23", "C", "T", "Ct", "Cktt", "Ckt2", "CC"]:
            self._position = tuple(data[2])

        else:
            self._category = data[0]
            self._size = data[1]
            self._position = (data[2])

            if (self._category, self._size, self._position) in level2_matrices:
                self._position = level2_matrices[(self._category, self._size, self._position)]

        super().__init__()

    def rank(self):

        return level2_matrices[self._position].rank()

    def coxeter_matrix(self):

        return level2_matrices[self._position]

    def coxeter_graph(self):

        return self.coxeter_matrix().coxeter_graph()

    def is_hyperbolic(self):

        return True

    def index_set(self):

        return self.coxeter_matrix().index_set()

    def is_affine(self):

        return False

    def is_finite(self):
        return False

    def is_crystallographic(self):

        return self.coxeter_matrix().is_crystallographic()

    def __eq__(self, other):

        if isinstance(other, CoxeterType_Level2Hyperbolic):
            if self.coxeter_matrix() == other.coxeter_matrix():
                return True
        return False
