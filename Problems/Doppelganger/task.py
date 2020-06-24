# the object_list has already been defined
# write your code here
from collections.abc import Hashable

same_hash = 0
for _object in object_list:
    if isinstance(_object, Hashable):
        if _object.__hash__ and object_list.count(_object) > 1:
            same_hash += 1
print(same_hash)

# same_objects = []
# count = 0
# start = True
# for el in object_list:
#     if isinstance(el, Hashable) and el not in same_objects:
#         count_state = count
#         for el2 in object_list:
#             if isinstance(el2, Hashable):
#                 if hash(el) == hash(el2):
#                     if not start:
#                         count += 1
#                     start = False
#         if count > count_state:
#             same_objects.append(el)
#             count += 1
#         start = True
#
# print(count)