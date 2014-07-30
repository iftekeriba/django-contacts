from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Contact


class ContactListView(ListView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        return context


class ContactCreateView(CreateView):
    model = Contact
    template_name_suffix = '_create'

    def get_success_url(self):
        return reverse('contacts:list')
