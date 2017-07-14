from glob import iglob
from pykwalify.core import Core
import yaml

def get_schema(version):
    path = 'schemas/kwalify/component/v{}.yaml'.format(version)
    contents = open(path)
    return yaml.load(contents)

def create_validator(source_data):
    version = source_data.get('schema_version', '3.1.0')
    schema = get_schema(version)
    validator = Core(source_data={}, schema_data=schema)
    validator.source = source_data
    return validator

def test_data_valid():
    """ Check that the content of data fits with masonry schema v2 """
    for component_file in iglob('*/component.yaml'):
        source_data = yaml.load(open(component_file))
        validator = create_validator(source_data)
        try:
            validator.validate(raise_exception=True)
        except:
            assert False, "Error found in: {0}".format(component_file)
