from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ImageCreateForm

def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
        # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # hacer algo
            new_item.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    template = "app_img/create.html"
    context_dict = {'section': 'images',
                    'form': form}

    return render(request, template, context_dict)
