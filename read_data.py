import json
from PIL import Image

def get_person_data():
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

def get_person_list(person_data):
    personlist = []
    for counter in range(len(person_data)):
        personlist.append(person_data[counter]["firstname"]+" "+(person_data[counter]["lastname"]))
    return personlist

def find_person_data_by_name(current_user):
    try:
        if current_user == "Julian Huber":
            image = Image.open("data/pictures/tb.jpg")
        elif current_user == "Yannic Heyer":
            image = Image.open("data/pictures/js.jpg")
        elif current_user == "Yunus Schmirander":
            image = Image.open("data/pictures/bl.jpg")
        return image
    except:
        return {}