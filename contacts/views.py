from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

from .models import Contact


class ContactListView(ListView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        return context


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        modeldict = model_to_dict(self.object)
        modeldict.pop('id')
        context['fields'] = modeldict.items()
        return context

    # def get_field_verbose_name(self, field=None):
    #     return field


class ContactCreateView(CreateView):
    model = Contact
    template_name_suffix = '_create'

    def get_success_url(self):
        return reverse('contacts:list')
