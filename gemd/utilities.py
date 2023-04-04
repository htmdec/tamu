from gemd.entity.value import NominalCategorical, NominalReal
from gemd.entity.attribute import Property, Parameter, Condition, PropertyAndConditions
from gemd.entity.object import MaterialSpec, ProcessSpec, IngredientSpec, MeasurementSpec
from object_templates import OBJ_TEMPL
from attribute_templates import ATTR_TEMPL

def generate_composition(conditions=[], parameters=[], output_mat_name='', output_mat_properties=[], tags=[]):
    generate_composition_process_spec = ProcessSpec(
        'Generating a specific composition from candidates inferred via Bayesian optimization',
        template=OBJ_TEMPL['Bayesian Optimization'],
        conditions=conditions,
        parameters=parameters,
        tags=tags
    )
        
    composition_space_material_spec = MaterialSpec(
        output_mat_name,
        template=OBJ_TEMPL['Composition'],
        process=generate_composition_process_spec,
        properties=output_mat_properties,
        tags=tags
    )
    
    return composition_space_material_spec

def fabricate_alloy(ingredients=[],conditions=[], parameters=[], output_mat_name='', output_mat_properties=[]):
    fabrication_process_spec = ProcessSpec(
        'Fabricating an alloy with specific, unique composition (suggested by BO) and synthesis parameters',
        template=OBJ_TEMPL['Fabrication'],
        conditions=conditions,
        parameters=parameters,
    )
    
    for material in ingredients:
        IngredientSpec(
        f'{material.name} Ingredient',
        material=material,
        process=fabrication_process_spec
    )
        
    batch_material_spec = MaterialSpec(
        output_mat_name,
        template=OBJ_TEMPL['Alloy'],
        process=fabrication_process_spec,
        properties=output_mat_properties
    )
    
    return batch_material_spec

def setting_alloy_traveler(ingredients=[],conditions=[], parameters=[], output_mat_name='', output_mat_properties=[]):
    setting_alloy_process_spec = ProcessSpec(
        'Selecting alloy from the produced batch and setting up the traveler for individual cuts and characterizations',
        template=OBJ_TEMPL['Setting'],
        conditions=conditions,
        parameters=parameters,
    )
    
    for material in ingredients:
        IngredientSpec(
        f'{material.name} Ingredient',
        material=material,
        process=setting_alloy_process_spec
    )
        
    alloy_traveler_material_spec = MaterialSpec(
        output_mat_name,
        template=OBJ_TEMPL['Alloy Traveler'],
        process=setting_alloy_process_spec,
        properties=output_mat_properties
    )
    
    return alloy_traveler_material_spec

def setting_alloy_sample(ingredients=[],conditions=[], parameters=[], output_mat_name='', output_mat_properties=[]):
    setting_alloy_process_spec = ProcessSpec(
        'Setting sample in traveler to be studied differently based on its sample number',
        template=OBJ_TEMPL['Setting'],
        conditions=conditions,
        parameters=parameters,
    )
    
    for material in ingredients:
        IngredientSpec(
        f'{material.name} Ingredient',
        material=material,
        process=setting_alloy_process_spec
    )
        
    alloy_sample_material_spec = MaterialSpec(
        output_mat_name,
        template=OBJ_TEMPL['Alloy Sample'],
        process=setting_alloy_process_spec,
        properties=output_mat_properties
    )
    
    return alloy_sample_material_spec

# def aggregate_materials(composition_material_spec):
    
#     setting_alloy_process_spec = ProcessSpec(
#         'Aggregating materials for {} and their respective quantities'.format(),
#         template=OBJ_TEMPL['Aggregate'],
#         conditions=conditions,
#         parameters=parameters,
#     )