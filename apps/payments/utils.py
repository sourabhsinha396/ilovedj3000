from django.http import Http404

def get_currency_amount(currency,price):
    if currency=="USD":
        return price / 75
    elif currency == "INR":
        return price*100
    elif price == None:
        raise Http404
    else:
        return price/60