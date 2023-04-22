# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]
# list_ = []
# for visits in geo_logs:
#     for countries in visits.values():
#         if 'Россия' in countries:
#             list_.append(visits)
# print(*list_,sep="\n")


import pytest

def filter_visits(geo_logs):
    list_ = []
    for visits in geo_logs:
        for countries in visits.values():
            if 'Россия' in countries:
                list_.append(visits)
    return list_

@pytest.mark.parametrize('geo_logs, expected_output', [
    ([{'visit1': ['Москва', 'Россия']}, 
      {'visit2': ['Дели', 'Индия']}, 
      {'visit3': ['Владимир', 'Россия']}, 
      {'visit4': ['Лиссабон','Португалия']}, 
      {'visit5': ['Париж', 'Франция']}, 
      {'visit6': ['Лиссабон','Португалия']}, 
      {'visit7': ['Тула', 'Россия']}, 
      {'visit8': ['Тула', 'Россия']}, 
      {'visit9': ['Курск', 'Россия']}, 
      {'visit10': ['Архангельск', 'Россия']}], 
     [{'visit1': ['Москва', 'Россия']},
      {'visit3': ['Владимир', 'Россия']},
      {'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']},
      {'visit9': ['Курск', 'Россия']},
      {'visit10': ['Архангельск', 'Россия']}])
])
def test_filter_visits(geo_logs, expected_output):
    assert filter_visits(geo_logs) == expected_output