import json

def get_person_list():
    # Opening JSON file
    file = open("data/person_db.json")
    # Loading the JSON File in a dictionary
    person_data = json.load(file)
    personlist = []
    for counter in range(len(person_data)):
        personlist.append(person_data[counter]["firstname"]+" "+(person_data[counter]["lastname"]))
    return personlist