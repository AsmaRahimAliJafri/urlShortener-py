# data structure to store shortened and expanded urls
global dataStruct_dict
dataStruct_dict = {}
# dataStruct_dict = {}

def add_url(unique_id, original_url):
  dataStruct_dict[unique_id] = original_url
  # dataStruct_dict[unique_id] = original_url

def get_all_items():
    return dataStruct_dict.items()

def get_expanded_url(unique_id):
    print("dictionary.py ------------------ All items in a dataStruct_dict = ", dataStruct_dict.items())
    # return dictionary[unique_id]
    return dataStruct_dict.get(unique_id)

