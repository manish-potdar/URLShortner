from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Link

# Create your views here.
def home_view(request):
    shortened_url = ""
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            # This line gets an existing link or creates a new one
            link, created = Link.objects.get_or_create(original_url=original_url)
            shortened_url = request.build_absolute_uri('/') + link.short_code
    
    return render(request, 'core/index.html', {'shortened_url': shortened_url})


def redirect_view(request, short_code):
    """ 
    View to redirect the short code to the original URL.
    """
    link = get_object_or_404(Link, short_code=short_code)

    return HttpResponseRedirect(link.original_url)
