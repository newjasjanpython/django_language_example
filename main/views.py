from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.utils.translation import get_language,activate,gettext
from django.conf import settings

# Create your views here.


@require_POST
def change_language_view(request):
    language = request.POST.get('language', 'uz')
    activate(language)
    return redirect(request.POST.get('next'))


@require_GET
def index_page(request):
    return render(request, "index.html", {})

