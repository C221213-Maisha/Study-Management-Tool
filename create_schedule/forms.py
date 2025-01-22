# forms.py
from django import forms

class ClassScheduleForm(forms.Form):
    DAY_CHOICES = [
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
    ]
    
    SLOT_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ]

    day = forms.ChoiceField(choices=DAY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    slot = forms.ChoiceField(choices=SLOT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    course_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    teacher_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    classroom_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
