from django.shortcuts import render
from .forms import LogForm
from .models import Log

def submit_view(request):
    dropdown_options = ["High", "Medium", "Low"]
    
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Print form data for debugging
            form.save()
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = LogForm()

    context = {
        'form': form,
        'dropdown_options': dropdown_options,
        'name': 'Your Name',
        'date': '2022-01-01'
    }

    return render(request, 'log/submit.html', context)