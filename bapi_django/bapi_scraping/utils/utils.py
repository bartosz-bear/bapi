def from_sql_to_dict(sql_result_set):
    
    temp_dict = {}

    categories = ['skip',
                  'category',
                  'course',
                  'instructor',
                  'description',
                  'enrollment_count',
                  'rating']
    
    print('result_set', sql_result_set[0], 'type ', type(sql_result_set[0]))

    for i, j in enumerate(sql_result_set[0]):
        temp_dict[categories[i]] = j

    temp_dict.pop('skip')

    return [temp_dict]