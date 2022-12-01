def get_data(input_file_path):
    input_file = open(input_file_path)
    data = input_file.readlines()
    input_file.close()
    return data
