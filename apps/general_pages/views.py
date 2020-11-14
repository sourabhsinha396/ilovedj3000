from django.views.generic import CreateView
from django.urls import reverse
from django.contrib import messages

from apps.general_pages.models import ContactMe
from apps.general_pages.forms import ContactMeModelForm


class ContactMeCreateView(CreateView):
	form_class = ContactMeModelForm
	template_name = "general_pages/contactme.html"
	
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Successfully submitted.')
		return reverse("blogs:home")
	