from django.shortcuts import render
from .forms import ConversionForm


def conversion(request):
    # 0 represent nothing 1 represent success 2 represent failure
    message = ""
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            data = form.save()
            message = 'success'
        else:
            message = 'failure'
    else:
        form = ConversionForm()
    
    context = {'form': form, 'message':message}

    return render(request, 'conversion.html', context)