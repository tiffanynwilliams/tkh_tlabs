def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.

    We need to skip the 0th row (first row)
    """
    clean_list = []
    
    for row in data[1:]:
        clean_list.append(float(row.strip()))

    return clean_list