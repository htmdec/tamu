from gemd.entity.bounds import RealBounds
from gemd.entity.object import MeasurementSpec
from object_templates import OBJ_TEMPL

OBJ_SPECS = {}

######## Measurement Specs ########
name = 'SEM'
OBJ_SPECS[name] = MeasurementSpec(
    name,
    template=OBJ_TEMPL[name],
    notes='SEM',
)

name = 'XRD'
OBJ_SPECS[name] = MeasurementSpec(
    name,
    template=OBJ_TEMPL[name],
    notes='XRD',
)

name = 'HSR'
OBJ_SPECS[name] = MeasurementSpec(
    name,
    template=OBJ_TEMPL[name],
    notes='HSR',
)

name = 'Microhardness-TAMU'
OBJ_SPECS[name] = MeasurementSpec(
    name,
    template=OBJ_TEMPL[name],
    notes='Microhardness-TAMU',
)

name = 'NI'
OBJ_SPECS[name] = MeasurementSpec(
    name,
    template=OBJ_TEMPL[name],
    notes='NI',
)

name = 'LIPT'
OBJ_SPECS[name] = MeasurementSpec(
    name,
    template=OBJ_TEMPL[name],
    notes='NI',
)

name = 'Tensile'
OBJ_SPECS[name] = MeasurementSpec(
    name,
    template=OBJ_TEMPL[name],
    notes='Tensile',
)
