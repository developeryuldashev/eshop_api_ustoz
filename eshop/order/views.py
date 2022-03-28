import json

from django.http import JsonResponse
from django.shortcuts import render,redirect
from product.models import Product
from utils.utils import get_order_count, get_orders
from .models import *
from utils.decorator import is_verified


def add_cart(request):
    pid = None
    if request.method=='POST':
        data:dict = json.loads(request.body)
        product = Product.objects.get(id=data['product_id'])
        user_orders = request.user.orders.all().order_by('-id')
        pid = product.id
        if user_orders:
            order = user_orders.first()
        else:
            order = Order.objects.create(customer=request.user)
        if product.quantity>0:
            order_detail = Order_detail.objects.filter(
                order = order,
                product = product
            ).first()
        if order_detail:
            order_detail.delete()
            event = 'delete'
        else:
            order_detail = Order_detail.objects.create(
                order = order,
                product=product,
            )
            event = 'added'
    return JsonResponse(
        {
            'order_size':order.item_count(),
            'event':event,
            'pid':pid,
        })

def order(request):
    products = Product.objects.all()[:4]
    return render(
        request=request,
        template_name='order/order.html',
        context={
            'products':products,
        }
    )

def order_complete(request):
    products = Product.objects.all()[:4]
    return render(
        request=request,
        template_name='order/order_complete.html',
        context={
            'products':products,
        }
    )

@is_verified
def in_card(request):
    orders = get_orders(request)
    if orders:
        total_price = request.user.orders.all().last().total_price()
    else:
        total_price = 0
    item_count = get_order_count(request)
    return render(
        request=request,
        template_name='product/in_card.html',
        context={
            'badge_count':item_count,
            'products':orders,
            'total_price':total_price,
        }
    )

def product_quantity(request):
    order_detail = None
    if request.method=='POST':
        data:dict = json.loads(request.body)
        item_id = data.get('item',None)
        action = data.get('data_action',None)
        value = data.get('value',None)
        if item_id and action:
            order_detail = Order_detail.objects.get(id=item_id)
            order_detail.change_quantity(action,value)
    response = {
        'error':False,
        'item_id':item_id,
        'item_quantity':order_detail.quantity if order_detail else 'none',
        'total_price':order_detail.total_price(),
        'total':order_detail.order.total_price(),
    } if order_detail else{
        'error':True
    }
    return JsonResponse(response)


def delete_order(request,id):
    if request.method=='GET':
        order_detail = Order_detail.objects.get(id=id)
        text = order_detail.product.__str__()+' deleted!'
        order = order_detail.order
        order_detail.delete()
        order_size = order.details.all().count()
        total_price = order.total_price()
        return  JsonResponse({'item_id':id,'text':text,'item_count':order_size,'total_price':total_price})
    return  JsonResponse({'item_id':id})
