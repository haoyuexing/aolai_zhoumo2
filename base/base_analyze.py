import yaml


def analyze_data(file_name, case_key):
    with open("./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f, yaml.FullLoader)[case_key]
        temp_list = list()
        temp_list.extend(data.values())
        return temp_list