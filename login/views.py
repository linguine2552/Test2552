from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json
from datetime import datetime

def assign_job_posting(request):
    if request.method == 'POST':
        comp_name = request.POST.get('comp_name')
        primary_name=request.POST.get('primary_name')
        comp_phone=request.POST.get('comp_phone')
        comp_email=request.POST.get('comp_email')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        tools=request.POST.get('tools')
        transport=request.POST.get('transport')
        language=request.POST.get('language')
        application_deadline = request.POST.get('application_deadline')

        contractor = request.POST.get('first_name') + ' ' + request.POST.get('last_name')
        print(contractor)
        
        # read the job data from the POST req
        job_data = {
            'comp_name': comp_name,
            'primary_name': primary_name,
            'comp_phone': comp_phone,
            'comp_email': comp_email,
            'job_title': job_title,
            'job_description': job_description,
            'location': location,
            'salary': salary,
            'tools': tools,
            'transport': transport,
            'language': language,
            'application_deadline': application_deadline,
            'posted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        contractor_json_filename = f'{contractor}_job_data.json'
        try:
            with open(contractor_json_filename, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        if job_data not in existing_data:
            existing_data.append(job_data)

            with open(contractor_json_filename, 'w') as file:
                json.dump(existing_data, file, indent=2)

            all_job_data_filename = 'job_data.json'
            try:
                with open(all_job_data_filename, 'r') as all_job_data_file:
                    all_job_data = json.load(all_job_data_file)
                    print(all_job_data)

                all_job_data = [job for job in all_job_data if job['job_title'] == existing_data[0]['job_title']]

                with open(all_job_data_filename, 'w') as file:
                    json.dump(all_job_data, file, indent=2)

            except FileNotFoundError:
                with open(all_job_data_filename, 'w') as file:
                    json.dump(existing_data, file, indent=2)
            response_data = {
                'success': True,
                'message': f'{job_title} assigned to {contractor}',
            }
            return JsonResponse(response_data)
        else:
            response_data = {
                'success': False,
                'message': 'Job already assigned to the contractor',
            }        
            return JsonResponse(response_data)
    else:
        response_data = {
            'success': False,
            'message': 'Invalid request method',
        }       
        return JsonResponse(response_data)
        

def create_job_posting(request):
    if request.method == 'POST':
        comp_name = request.POST.get('comp_name')
        primary_name=request.POST.get('primary_name')
        comp_phone=request.POST.get('comp_phone')
        comp_email=request.POST.get('comp_email')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        tools=request.POST.get('tools')
        transport=request.POST.get('transport')
        language=request.POST.get('language')
        application_deadline = request.POST.get('application_deadline')

        job_data = {
            'comp_name': comp_name,
            'primary_name': primary_name,
            'comp_phone': comp_phone,
            'comp_email': comp_email,
            'job_title': job_title,
            'job_description': job_description,
            'location': location,
            'salary': salary,
            'tools': tools,
            'transport': transport,
            'language': language,
            'application_deadline': application_deadline,
            'posted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        try:
            with open('job_data.json', 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        if job_data not in existing_data:
            existing_data.append(job_data)

            with open('job_data.json', 'w') as file:
                json.dump(existing_data, file, indent=2)

            return HttpResponse('Job Posted!')
        else:
            return HttpResponse('Job posting already exists')
    else:
        return HttpResponse('Invalid request method')



times = 0
def login(request):
    global times
    print('Login Page Opened!')
    times += 1
    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else: report_loc = 'signin/'
    return render(request, 'login.html', {'loc':report_loc,'error': ''})
    
    
def signin(request):
    print('Login Request Made!')
    print('Reading Data from JSON')

    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else:
        report_loc = 'signin/'

    with open('user_data.json') as user_json_file:
        user_data = json.load(user_json_file)

    existing_users = user_data.get('u_data', [])

    email = request.POST.get('email')
    password = request.POST.get('password')

    active_contractors = []

    for user in existing_users:
        user_type = user.get('Registration_Type__c', '')

        if user_type == 'Interested in becoming a Titan Construction Partner (new contractors)':
            active_contractors.append(user)

    with open('job_data.json') as job_json_file:
        job_data = json.load(job_json_file)

    if email and password:
        for user in existing_users:
            if email in user:
                if user[email] == password:
                    # render dashboard based on account type to prevent IDOR
                    user_type = user.get('Registration_Type__c', '')
                    ufN = user.get('FirstName', '')  
                    ulN = user.get('LastName', '')  
                    user_name = ufN + ' ' + ulN                      
                    if user_type == 'Interested in contracting Titan Construction Partners':
                        # Render the client dashboard template with user and job data
                        return render(request, 'clientDashboard.html', {'user_data': user})
                    elif user_type == 'Interested in becoming a Titan Construction Partner (new contractors)':
                        with open(f'{user_name}_job_data.json') as job_json_file:
                            job_data = json.load(job_json_file)                    
                        return render(request, 'contractorDashboard.html', {'user_data': user, 'job_data': job_data})
                    elif user_type == 'Admin':
                        return render(request, 'adminDashboard.html', {'user_data': user, 'job_data': job_data, 'active_contractors': active_contractors})
                    else:
                        return HttpResponse('Unknown user type')

                else:
                    print('Email != Password, returning HTTP response')
                    return render(request, 'login.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Sorry. The Email and Password do not match.'})

        print('Account does not exist, returning HTTP response')
        return render(request, 'login.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Sorry. No such account exists. Consider signing up!'})
    else:
        print('Email or Password not provided, returning HTTP response')
        return render(request, 'login.html', {'loc': report_loc, 'errorclass': 'alert alert-danger', 'error': 'Email and Password are required.'})
        
        
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')        