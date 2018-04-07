
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return render(request, 'payment/canceled.html')


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    if order.payment_method =='1' or order.payment_method == '2':
        return render(request, 'payment/done.html')

    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.get_total_cost()+order.get_total_cost()*Decimal('0.029')+Decimal('0.3'),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
        'return': request.build_absolute_uri(reverse('payment:done')),
        'cancel_return': request.build_absolute_uri(reverse('payment:canceled')),
       }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'order': order,
                                                    'form':form})
