# create your dictionary here
from collections.abc import Hashable

objects_dict = {}
for _obj in objects:
    if isinstance(_obj, Hashable):
        objects_dict[_obj] = hash(_obj)