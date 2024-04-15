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
    names = current_user.split(" ")
    firstname = names[0]
    lastname= names[1]
    person_data = get_person_data()
    for element in person_data:
        if element["firstname"] == firstname and element["lastname"] == lastname:
            return element
        
def get_picture(current_user):
    current_user_infos = find_person_data_by_name(current_user)
    current_user_picture_path = current_user_infos['picture_path']
    image = Image.open(current_user_picture_path)
    return image