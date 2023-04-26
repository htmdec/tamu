from gemd.entity.bounds import RealBounds
from gemd.entity.template import ProcessTemplate, MaterialTemplate, MeasurementTemplate
from .attribute_templates import ATTR_TEMPL

OBJ_TEMPL = {}

######## Process Templates ########
name = 'Bayesian Optimization'
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

name = 'Aggregating'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Aggregaging the correct ingredients to produce a mixture that can go through
                fabrication procedure
                ''',
)

name = 'Selecting'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Selecting a composition from suggested compositions by Bayesian inference
                ''',
)

name = 'Mixing'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Mixing individual elements of the composition to make the initial mixture for the alloy 
                ''',
)

name = 'Arc Melting'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='Arc Melting',
)

name = 'Homogenization'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='Homogenization',
)

name = 'Forging'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Forging
                ''',
)

name = 'Setting Traveler'
OBJ_TEMPL[name] = ProcessTemplate(
    name,
    description='''Setting Traveler
                ''',
)

######## Material Templates ########

name = 'Summary Sheet'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Summary sheet of all the experiments conducted in previous batch that will help generate the next compositions spaces and suggest compositions via Bayesian Optimizization',
)

name = 'Inferred Alloy Compositions'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Final selection of the bayesian optimziation algorithm, which can generate different number of compositions (i.e., 16 for VAM, 8 for DED) under various paramereters',
)

name = 'Alloy Composition'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Composition selected to be fabricated and characterized',
)

name = 'Composition Element'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Individual ingredient of a composition',
)

name = 'Alloy'
OBJ_TEMPL[name] = MaterialTemplate(
    name,
    description='Alloy generated with a unique composition and synthesis parameters',
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

######## Measurement Templates ########
name = 'Weighting'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='The process of weighting',
)

name = 'SEM'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='SEM'
)

name = 'XRD'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='XRD'
)

name = 'HSR'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='HSR'
)

name = 'Microhardness-TAMU'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='Microhardness-TAMU'
)

name = 'NI'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='NI'
)

name = 'LIPT'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='NI'
)

name = 'Tensile'
OBJ_TEMPL[name] = MeasurementTemplate(
    name,
    description='Tensile'
)
