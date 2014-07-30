from django.views.generic.edit import CreateView

from .models import Contact


class ContactCreateView(CreateView):
    model = Contact
    template_name_suffix = '_create'
