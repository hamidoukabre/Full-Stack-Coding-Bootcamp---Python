from django.shortcuts import render 

data = {

    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 6,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },   
        {
            "id": 5,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }        

    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 3,
            "name": "mammifère"
        },
        {
            "id": 4,
            "name": "amphibien"
        },
        {
            "id": 5,
            "name": "arachnide"
        },
        {
            "id": 6,
            "name": "reptile"
        }                        

    ]
}


def home(request):
    context ={
        "data": data,
        }
    return render(request, "info/home.html", context)

def family(request, x):
    list_family_animal = []
    for value in data['animals']:
        if value[family]==x:
            list_family_animal.append(value)

    for val in data[families]:
        if val[id] ==x:
            for va in list_family_animal:
                va[family]= val['name'] + " id: " + str(x)
    context = {

        'list' :list_family_animal,
    }        
    return render(request, "info/family.html", context)    


def animals(request,y):
    list_animals = []
    for values in data['animals']:
        if values['id'] == y:
            list_animals.append(values)
    for val in data["families"]:
        if val["id"] == y:
            for va in list_animal:
                va["family"] = val["name"] +" id: "+ str(y)
    context = {"list":list_animal}
    return render(request, "info/animal.html", context)
    