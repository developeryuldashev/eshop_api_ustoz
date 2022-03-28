def get_order_count(request):
    if request.user.is_authenticated:
        order = request.user.orders.all()
        if order:
            return order.order_by('-id').first().item_count()
    return 0

def get_orders(request):
    if request.user.is_authenticated:
        order = request.user.orders.all()
        if order:
            return order.order_by('-id').first().details.all()
        else:
            return []
    return []