from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Goal
from .forms import GoalForm
from django.contrib import messages

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    total_goals = goals.count()
    completed_goals = goals.filter(completed=True).count()
    progress_percentage = (completed_goals / total_goals * 100) if total_goals else 0

    # Check if all goals are completed
    all_completed = total_goals > 0 and completed_goals == total_goals

    if all_completed:
        messages.success(request, "🎉 Congratulations! You've completed all your goals! 🎉")
        # Do not delete goals immediately; they'll remain visible until the next page load

    return render(request, 'goals/goal_list.html', {
        'goals': goals,
        'progress_percentage': progress_percentage,
        'all_completed': all_completed,
        'total_goals': total_goals,
    })

def delete_goal(request, goal_id):
    if request.method == "POST":
        goal = get_object_or_404(Goal, id=goal_id)
        goal.delete()
        messages.success(request, "Goal deleted successfully.")
    return redirect('goal_list')  # Redirect to the goal list page

@login_required
def clear_completed_goals(request):
    # Optional: Allow clearing all completed goals explicitly if needed
    Goal.objects.filter(user=request.user, completed=True).delete()
    return redirect('goal_list')


# View to create a new goal for the logged-in user
@login_required
def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user  # Associate the goal with the logged-in user
            goal.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'goals/create_goal.html', {'form': form})

# View to mark a goal as completed for the logged-in user
@login_required
def toggle_goal(request, pk):
    goal = Goal.objects.get(pk=pk, user=request.user)  # Ensure the goal belongs to the current user
    goal.completed = not goal.completed
    goal.save()
    return redirect('goal_list')
