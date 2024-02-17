from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import UserRegisterForm
from ratelimit.decorators import ratelimit
# Registration view
@ratelimit(key='ip', rate='5/h', method='POST', block=True)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# Login and Logout views will use Django's built-in views. 
# You don't need to add them here if you're not customizing them beyond the template.
