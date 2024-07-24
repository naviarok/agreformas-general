from django.shortcuts import render
from .forms import MessageForm

def home(request):
    # 0 represent nothing 1 represent success 2 represent failure
    message = ""
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.save()
            message = 'success'
        else:
            message = 'failure'

        context = {'form': form, 'message':message}
        return render(request, 'index.html' , context)
    

    else:
        form = MessageForm()
    
        context = {'form': form, 'message':message}

        return render(request, 'index.html' , context)