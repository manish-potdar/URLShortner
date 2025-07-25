from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Link

# Create your views here.
def home_view(request):
    """
    View to create a new short URL.
    """
    shortend_url = ""
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            # create a new Link object and save it
            link = Link.objects.create(original_url = original_url)
            # Build the full shortend URL to display to the user
            shortend_url = request.build_absolute_uri('/') + link.short_code

    return render(request, 'core/index.html', {'shortened_url': shortend_url})


def redirect_view(request, short_code):
    """ 
    View to redirect the short code to the original URL.
    """
    link = get_object_or_404(Link, short_code=short_code)

    return HttpResponseRedirect(link.original_url)
