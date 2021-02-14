from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from users.models import User, Customer

class RegisterCustomerForm(UserCreationForm):

    address = forms.CharField(widget=forms.Textarea, required=True)
    phone_number = forms.CharField(widget=forms.Textarea, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        address = self.cleaned_data.get('address')
        phone_number = self.cleaned_data.get('phone_number')
        user = super().save(commit=False)
        user.is_staff = False
        user.phone_number = phone_number
        user.save()
        customer = Customer.objects.create(user=user, address= address)
        return user