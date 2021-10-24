from django.views.generic import TemplateView
from django.contrib.auth import get_user_model


class HomePage(TemplateView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'ProjectO/index.html'
