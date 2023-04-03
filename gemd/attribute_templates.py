#imports
from gemd.entity.template import PropertyTemplate, ParameterTemplate, ConditionTemplate
from gemd.entity.bounds import CategoricalBounds, RealBounds

ATTR_TEMPL = {}

######## Property Templates ########

name = 'Fabrication Method'
ATTR_TEMPL[name] = ConditionTemplate(
    name,
    bounds=CategoricalBounds(['DED', 'VAM']),
    description='Method of Batch Fabrication'
)

name = 'Material Composition'
ATTR_TEMPL[name] = PropertyTemplate(
    name,
    bounds=RealBounds(0,100,''),
    description='Percentage of the total composition that a given Material takes'
)
######## Parameter Templates ########

