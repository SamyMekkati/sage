"""
Level 2 minimal Coxeter types.
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
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.combinat.root_system.level2_hyperbolic_matrices import level2_matrices

class CoxeterType_Level2(CoxeterType):
    r"""
    Hyperbolic level 2 Coxeter type.
    """
    def __init__(self, data):
        self._key = tuple(data)
        self._category = data[0]
        self._rank = data[1]
        self._position = data[2]

        super().__init__()

    def _repr_(self):
        """
        Return a string representation of ``self``.

        This method returns a string that describes the Coxeter type,
        including the reference to Chen-Labbé's articles mentioned above.

        EXAMPLES::

            sage: L2 = CoxeterType(["Cy", 5, (5, 2)])
            sage: L2
            Coxeter type of ['Cy', 5] at line 5 column 2
        """
        a, b = self._position

        return (
                f"Coxeter type of ['{self._category}', {self._rank}] "
                f"with position (Row : {a}, Column : {b})"
        )
    
    def rank(self):
        return len(level2_matrices[self._key])

    def coxeter_matrix(self):
        return CoxeterMatrix(level2_matrices[self._key])

    def coxeter_graph(self):
        return self.coxeter_matrix().coxeter_graph()

    def is_hyperbolic(self):
        return False

    def index_set(self):
        return self.coxeter_matrix().index_set()

    def is_affine(self):
        return False

    def is_finite(self):
        return False

    def is_crystallographic(self):
        return self.coxeter_matrix().is_crystallographic()

    def __eq__(self, other):
        return (
            isinstance(other, CoxeterType_Level2)
            and self.coxeter_matrix() == other.coxeter_matrix()
        )
