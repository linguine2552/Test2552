from django.shortcuts import render, HttpResponse
from django.urls import resolve
from django.shortcuts import render
import json
times = 0
def register(request):
    global times
    print('Register Page Opened!')
    times += 1
    current_url = request.path
    print(current_url)
    print(0)
    if request.path == '/register/signup/':
        report_loc = '../signup/'
    else: report_loc = 'signup/'
    return render(request, 'register.html', {'loc':report_loc,'error': ''})



def signup(request):
    print('Register Request Made!')
    print('Reading Data from JSON')

    if request.path == '/register/signup/':
        report_loc = '../signup/'
    else:
        report_loc = 'signup/'

    with open('user_data.json') as json_file:
        data = json.load(json_file)

    existing_users = data.get('u_data', [])
    Email = request.POST.get('Email')
    Password = request.POST.get('Password')
    first_name = request.POST.get('FirstName')
    last_name = request.POST.get('LastName')
    phone = request.POST.get('Phone')
    company = request.POST.get('Company')
    website = request.POST.get('Website')
    registration_type = request.POST.get('Registration_Type__c')

    if Email and Password:
        if Email not in [user.get('Email') for user in existing_users]:
            if Password == Password:
                new_user = {
                    f'{Email}': Password,
                    'FirstName': first_name,
                    'LastName': last_name,
                    'Phone': phone,
                    'Company': company,
                    'Website': website,
                    'Registration_Type__c': registration_type
                }

                existing_users.append(new_user)

                data['u_data'] = existing_users
                with open('user_data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)

                contractor = first_name + ' ' + last_name                    
                contractor_json_filename = f'{contractor}_job_data.json'     
                info = {}
                
                with open(contractor_json_filename, 'w') as file:
                    json.dump(info, file, indent=2)    

                print('Registered new user, returning HTTP response')
                return HttpResponse('You are now registered')
            else:
                print('Passwords do not match, returning HTTP response')
                return render(request, '/register/register.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Sorry. The Passwords do not match.'})
        else:
            print('The Username or Email ID is already taken, returning HTTP response')
            return render(request, '/register/register.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Sorry. The Username or Email ID is already taken.'})
    else:
        print('Email or Password not provided, returning HTTP response')
        return render(request, '/register/register.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Email and Password are required.'})

        
        
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')        
