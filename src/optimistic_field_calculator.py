def calculate_max_num_of_fields(num_of_points):
    correction = (0, 1, 1, 2)
    return (num_of_points // 4) * 3 + correction[num_of_points % 4]