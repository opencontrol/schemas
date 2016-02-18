""" Python script to convert Open Controls schema version v1.0 to v2.0 """

import yaml
import glob

from utils import add_if_exists, transport_usable_data


def flatten_verifications(old_verifications):
    """ Convert verifications from v1 to v2 """
    new_verifications = []
    for key in old_verifications:
        verification = old_verifications[key]
        verification['key'] = key
        new_verifications.append(verification)
    return new_verifications


def transform_references(old_references):
    """ Covert old reference format to new reference format """
    new_references = []
    for ref in old_references:
        new_ref = {}
        new_ref['verification_key'] = ref['verification']
        component_key = ref.get('component')
        system_key = ref.get('system')
        if component_key:
            new_ref['component_key'] = component_key
        if system_key:
            new_ref['system_key'] = system_key
        new_references.append(new_ref)
    return new_references


def convert_satisfies(old_satisfies):
    """ Convert satisfies objects from v1 to v2 """
    new_satisfies = []
    for standard_key in old_satisfies:
        for control_key in old_satisfies[standard_key]:
            new_control_dict = {
                'standard_key': standard_key,
                'control_key': control_key
            }
            old_control_dict = old_satisfies[standard_key][control_key]
            add_if_exists(
                new_data=new_control_dict,
                old_data=old_control_dict,
                field='narrative'
            )
            add_if_exists(
                new_data=new_control_dict,
                old_data=old_control_dict,
                field='implementation_status'
            )
            print(old_control_dict)
            new_control_dict['covered_by'] = transform_references(
                old_control_dict.get('references', {})
            )
            new_satisfies.append(new_control_dict)
    return new_satisfies


def convert(old_data):
    """ Convert the data from the v2 to v1 """
    new_data = {}
    transport_usable_data(new_data=new_data, old_data=old_data)
    verifications = flatten_verifications(old_data.get('verifications', {}))
    if verifications:
        new_data['verifications'] = verifications
    satisfies = convert_satisfies(old_data.get('satisfies', {}))
    if satisfies:
        new_data['satisfies'] = satisfies
    # Tag new schema version
    new_data['schema_version'] = 2.0
    return new_data
