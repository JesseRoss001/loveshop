from django.shortcuts import render, redirect
from .forms import ContactUsForm


def contact_success(request):

    """ Render the Contact Success HTML page """

    return render(request, 'contact_success')


def contact_page(request):
    """ View function for the contact us form """

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact/contact_success.html')
    else:
        form = ContactUsForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact_page.html', context)

