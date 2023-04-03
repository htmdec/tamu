from gemd.entity.bounds import RealBounds
from gemd.entity.template import ProcessTemplate, MaterialTemplate, MeasurementTemplate
from attribute_templates import ATTR_TEMPL

OBJ_TEMPL = {}

######## Process Templates ########
name = 'Bayezian Optimization'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Applying Bayezian Optimization based on multi-inputs/multi-output
                objectives to generated new composition space, with data extracted 
                from summary sheet aggregated by various experimental teams
                ''',
)

name = 'Fabrication'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Applying Bayezian Optimization based on multi-inputs/multi-output
                objectives to generated new composition space, with data extracted 
                from summary sheet aggregated by various experimental teams
                ''',
    conditions = [
        ATTR_TEMPL['Fabrication Method']
    ]
)

name = 'Setting'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Set up the selected alloy, including traveler creation, processing, etc
                ''',
)

######## Material Templates ########
name = 'Composition'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Composition suggested by the Bayesian Optimization results',
)


name = 'Alloy'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Alloy generated with its own composition and synthesis parameters',
)

name = 'Alloy Traveler'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Traveler containing different version of the same alloy to be distributed and analyzed concurrently',
)

name = 'Alloy Sample'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Sample of the alloy, extracted from traveler, and destined for specific characterization based on its sample number (=placement in the traveler)',
)
