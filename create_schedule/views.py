# views.py
from django.shortcuts import render, redirect
from .forms import ClassScheduleForm
from .models import ClassSchedule
from django.contrib.auth.decorators import login_required

# Define a mapping from days of the week to their numerical values
DAYS_ORDER = {
    'Friday': 1,
    'Saturday': 2,
    'Sunday': 3,
    'Monday': 4,
    'Tuesday': 5,
    'Wednesday': 6,
    'Thursday': 7,
}

@login_required  # Ensure user is logged in
def class_schedule(request):
    if request.method == 'POST':
        form = ClassScheduleForm(request.POST)
        if form.is_valid():
            # If form is valid, save the data to the database
            day = form.cleaned_data['day']
            slot = form.cleaned_data['slot']
            course_name = form.cleaned_data['course_name']
            teacher_name = form.cleaned_data['teacher_name']
            class_time = form.cleaned_data['class_time']
            classroom_number = form.cleaned_data['classroom_number']

            # Save the data to the database linked with the logged-in user
            schedule = ClassSchedule(
                user=request.user,
                day=day,
                slot=slot,
                course_name=course_name,
                teacher_name=teacher_name,
                class_time=class_time,
                classroom_number=classroom_number
            )
            schedule.save()

            # Redirect to the 'see_schedule' page after saving
            return redirect('see-schedule')
        else:
            # If the form is invalid, re-render the form with errors
            return render(request, 'create_schedule/class-schedule.html', {'form': form})
    else:
        # If it's a GET request, render an empty form
        form = ClassScheduleForm()


    return render(request, 'create_schedule/class-schedule.html', {'form': form})

@login_required  # Ensure user is logged in
def see_schedule(request):
    # Fetch only schedules for the logged-in user
    schedules = ClassSchedule.objects.filter(user=request.user)

    # Sort schedules by the custom day order (Friday to Thursday)
    schedules = sorted(schedules, key=lambda x: DAYS_ORDER.get(x.day, 8))  # Default to 8 for invalid days

    return render(request, 'create_schedule/see-schedule.html', {'schedules': schedules})
