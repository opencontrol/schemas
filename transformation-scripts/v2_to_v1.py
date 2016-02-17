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


def unflatten_verifications(old_verifications):
    """ Convert verifications from v2 to v1 """
    new_verifications = {}
    for verification in old_verifications:
        key = verification['key']
        del verification['key']
        new_verifications[key] = verification
    return new_verifications


def transform_covered_by(covered_by):
    """ Transform covered_by to references as in version 1.0 """
    new_references = []
    for ref in covered_by:
        new_ref = {}
        new_ref['verification'] = ref['verification_key']
        component_key = ref.get('component_key')
        system_key = ref.get('system_key')
        if component_key:
            new_ref['component'] = component_key
        if system_key:
            new_ref['system'] = system_key
        new_references.append(new_ref)
    return new_references


def unflatten_satsifies(old_satsifies):
    """ Convert satsifies from v2 to v1 """
    new_satsifies = {}
    for element in old_satsifies:
        new_element = {}
        # Handle exsiting data
        add_if_exists(new_data=new_element, old_data=element, field='narrative')
        add_if_exists(new_data=new_element, old_data=element, field='implementation_status')
        # Handle covered_by
        refernces = transform_covered_by(element.get('covered_by', {}))
        if refernces:
            new_element['refernces'] = refernces
        # Unflatten
        if element['standard_key'] not in new_satsifies:
            new_satsifies[element['standard_key']] = {}
        if element['control_key'] not in new_satsifies[element['standard_key']]:
             new_satsifies[element['standard_key']][element['control_key']] = new_element
    return new_satsifies

def convert(old_data):
    """ Convert the data from the v2 to v1 """
    new_data = {}
    transport_usable_data(new_data=new_data, old_data=old_data)
    verifications = unflatten_verifications(old_data.get('verifications', {}))
    if verifications:
        new_data['verifications'] = verifications
    satsifies = unflatten_satsifies(old_data.get('satsifies', {}))
    if satsifies:
        new_data['satsifies'] = satsifies
    return new_data


if __name__ == '__main__':
    data = yaml.load(open('v2_example.yaml'))
    data = convert(data)
    with open('v1_from_v2_example.yaml', 'w') as f:
        f.write(yaml.dump(data, default_flow_style=False))
