from django.shortcuts import render

# Create your views here.
def index_before_login(request):
    return render(request, 'index_before_login.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def class_schedule(request):
    return render(request, 'create_schedule/class-schedule.html')

def study_repository(request):
    return render(request, 'study_repository/home.html')


def time_and_study_methods(request):
    return render(request, 'time-and-study-methods.html')

def goal_tracking(request):
    return render(request, 'goals/goal_list.html')

