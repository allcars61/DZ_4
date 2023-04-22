# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
#
#
# res = list({key for val in ids.values() for key in val})
# print(res)


import pytest

def test_unique_values():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    expected_res = [213, 15, 54, 119, 98, 35]
    assert list({key for val in ids.values() for key in val}) == expected_res

def test_empty_dict():
    ids = {}

    assert list({key for val in ids.values() for key in val}) == []

def test_same_values():
    ids = {'user1': [1, 1, 1],
           'user2': [2, 2, 2],
           'user3': [3, 3, 3]}

    expected_res = [1, 2, 3]
    assert list({key for val in ids.values() for key in val}) == expected_res

@pytest.mark.parametrize("ids, expected_res", [
    ({'user1': [1], 'user2': [2], 'user3': [3]}, [1, 2, 3]),
    ({'user1': [1, 1], 'user2': [2, 2], 'user3': [3, 3]}, [1, 2, 3]),
    ({'user1': [1, 2], 'user2': [2, 3], 'user3': [3, 1]}, [1, 2, 3]),
])
def test_parameterized(ids, expected_res):
    assert list({key for val in ids.values() for key in val}) == expected_res