from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city','state', 'payment_method']
        labels = {
            'first_name': ('名字'),
            'last_name': ('姓'),

            'address': ('地址'),
            'postal_code': ('邮编'),
            'city': ('城市'),
            'state': ('州'),
            'payment_method': ('支付方式'),

        }
