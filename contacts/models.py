from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Contact(models.Model):
    added = models.DateTimeField(_('added'), auto_now_add=True)
    last_mod = models.DateTimeField(_('last mod.'), auto_now=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    # Translators: either gender or number. Used for e-mail templates.
    gender = models.CharField(choices=())
    # Translators: use your country's national identification number.
    nid = models.IntegerField(_('ID'), unique=True, blank=True, null=True,
        help_text=_('national identification number'))
    email = models.EmailField(_('e-mail'), blank=True, null=True,
       help_text=_('telephone number'))
    # To be implemented: tel and address, probably as foreign keys
    # tel1 = models.IntegerField(_('cell phone num.'), blank=True, null=True)
    # tel2 = models.IntegerField(_('tel.'), blank=True, null=True)
    # address = ForeignKey('Address')
    obs = models.TextField(_('observations'), blank=True)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
