import json
def get_person_data():
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list(person_data):
    personlist = []
    for counter in range(len(person_data)):
        personlist.append(person_data[counter]["firstname"]+" "+(person_data[counter]["lastname"]))
    return personlist