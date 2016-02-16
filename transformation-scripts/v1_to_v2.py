import yaml


UNCHANGED_FIELDS = ['name', 'documentation_complete', 'references']


def add_if_exists(new_data, old_data, field):
    """ Adds the field to the new data if it exists in the old data """
    field_value = old_data.get(field)
    if field_value:
        new_data[field] = field_value


def transport_usable_data(new_data, old_data):
    """ Adds the data structures that haven't changed to the new dictionary """
    for field in UNCHANGED_FIELDS:
        add_if_exists(new_data=new_data, old_data=old_data, field=field)


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


def convert_satsifies(old_satsifies):
    """ Convert satsifies objects from v1 to v2 """
    new_satsifies = []
    for standard_key in old_satsifies:
        for control_key in old_satsifies[standard_key]:
            new_control_dict = {
                'standard_key': standard_key,
                'control_key': control_key
            }
            old_control_dict = old_satsifies[standard_key][control_key]
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
            new_control_dict['covered_by'] = transform_references(
                old_control_dict.get('references', {})
            )
            new_satsifies.append(new_control_dict)
    return new_satsifies


def convert(old_data):
    """ Convert the data from the v2 to v1 """
    new_data = {}
    transport_usable_data(new_data=new_data, old_data=old_data)
    verifications = flatten_verifications(old_data.get('verifications', {}))
    if verifications:
        new_data['verifications'] = verifications
    satsifies = convert_satsifies(old_data.get('satisfies', {}))
    if satsifies:
        new_data['satsifies'] = satsifies
    return new_data


if __name__ == '__main__':
    data = yaml.load(open('v1_example.yaml'))
    data = convert(data)
    with open('v2_from_v1_example.yaml', 'w') as f:
        f.write(yaml.dump(data, default_flow_style=False))
