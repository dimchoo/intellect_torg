from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from files_app.models import File


def file_view(request, name):
    file = get_object_or_404(File, name=name)
    response = HttpResponse(file.text, content_type="text/plain; charset=utf-8")
    return response
