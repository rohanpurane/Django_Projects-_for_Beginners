from django.shortcuts import render
from .models import *
from .forms import *
import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ColdCoffeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount'] * 100

        #Create Razorpay client
        client = razorpay.Client(auth=('........','.........'))

        # create order
        response_payment = client.order.create(dict(amount=amount,currency='INR'))
        print(response_payment)

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            cold_coffee = ColdCoffee(name=name,amount = amount,order_id = order_id,)
            cold_coffee.save()
            response_payment['name'] = name

            return render(request, 'home.html',{'form':form, 'payment':response_payment})

    else:
        form = ColdCoffeeForm()
    return render(request, 'home.html',{'form':form})

# print(response_payment)
# {'id': 'order_KxDaSHxZGtDM43', 'entity': 'order', 'amount': 1000, 'amount_paid': 0, 'amount_due': 1000, 'currency': 'INR', 'receipt': None, 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1672206048}


@csrf_exempt
def payment_status(request):
    response = request.POST
    print(response)
    params_dict = {
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_signature' : response['razorpay_signature'],
    }

    # client instance
    try:
        client = razorpay.Client(auth=('.........','...........'))
        status = client.utility.verify_payment_signature(params_dict)
        cold_coffee = ColdCoffee.objects.get(order_id = response['razorpay_order_id'])
        cold_coffee.razorpay_payment_id = response['razorpay_payment_id']
        cold_coffee.paid = True
        cold_coffee.save()
        return render(request, 'payment_status.html', {'status': True})
    except:
        return render(request, 'payment_status.html', {'status': False})
# Forbidden (Origin checking failed - null does not match any trusted origins.): /payment_status/
