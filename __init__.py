# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .bom import *


def register():
    Pool.register(
        BOM,
        ProductionBomOrcad,
        module='production_bom_orcad_import', type_='model')
