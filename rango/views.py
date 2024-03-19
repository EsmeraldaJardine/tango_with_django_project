from django.shortcuts import render
from django.http import HttpResponse

# view functions are request handlers
# Create your views here.
# With the view created, you’re only part of the way to allowing a user to access it. For
# a user to see your view, you must map a Uniform Resource Locator (URL)⁹ to the view

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'name': 'Esmeralda'}
    return render(request, 'rango/about.html', context=context_dict)
