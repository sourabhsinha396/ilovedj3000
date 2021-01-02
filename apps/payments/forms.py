from django import forms


class PaymentDetailForm(forms.Form):
    currency_choices = (
        ('USD','usd'),
        ('INR','inr'),
    )
    currency = forms.ChoiceField(choices=currency_choices,help_text="In which currency, You want to pay?")