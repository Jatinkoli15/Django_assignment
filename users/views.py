from django.http import HttpResponse
from django.shortcuts import render 


dummy_data = [
    {"id": 1, "name": "John Doe", "age": 25, "city": "New York"},
    {"id": 2, "name": "Jane Smith", "age": 30, "city": "Los Angeles"},
    {"id": 3, "name": "Alice Brown", "age": 22, "city": "Chicago"},
    {"id": 4, "name": "Bob Johnson", "age": 28, "city": "San Francisco"},
    {"id": 5, "name": "Charlie Davis", "age": 35, "city": "Miami"},
    {"id": 6, "name": "Diana Evans", "age": 26, "city": "Dallas"},
    {"id": 7, "name": "Edward Miller", "age": 40, "city": "Seattle"},
    {"id": 8, "name": "Fiona Wilson", "age": 33, "city": "Austin"},
    {"id": 9, "name": "George Martinez", "age": 23, "city": "Chicago"},
    {"id": 10, "name": "Hannah Taylor", "age": 27, "city": "Boston"},
    {"id": 11, "name": "Ian Anderson", "age": 31, "city": "Denver"},
    {"id": 12, "name": "Jack Roberts", "age": 29, "city": "Phoenix"},
    {"id": 13, "name": "Kimberly Lee", "age": 24, "city": "Houston"},
    {"id": 14, "name": "Liam Walker", "age": 38, "city": "Portland"},
    {"id": 15, "name": "Megan Scott", "age": 32, "city": "San Diego"},
    {"id": 16, "name": "Nathan Young", "age": 36, "city": "Las Vegas"},
    {"id": 17, "name": "Olivia King", "age": 34, "city": "Sacramento"},
    {"id": 18, "name": "Paul Turner", "age": 30, "city": "Detroit"},
    {"id": 19, "name": "Quinn Perez", "age": 28, "city": "Atlanta"},
    {"id": 20, "name": "Rachel Hernandez", "age": 27, "city": "Philadelphia"}
]


def home(request):
    return render(request,'users/home.html')

def all_users(request):
    return render(request,'users/all_users.html',{'users' : dummy_data})

def user_detail(request, user_id):
    user_D= {}
    print(type(user_id))
    for user in dummy_data:
        if (user['id'] == int(user_id)):
            user_D = user
            break
    return render(request,'users/user_detail.html',{'user' : user_D})

