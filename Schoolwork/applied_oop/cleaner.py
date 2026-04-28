def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    new_list = []
    for e in data:
        # check if "e" is an empty string
        val = e.strip()
        if val != "" and val != "NO DATA":
            # type cast val into an int
            new_val = int(val)
            new_list.append(new_val)

    return new_list
