""" These are shared functions between v2_to_v1 and v1_to_v2 """

def add_if_exists(new_data, old_data, field):
    """ Adds the field to the new data if it exists in the old data """
    if field in old_data:
        new_data[field] = old_data.get(field)
