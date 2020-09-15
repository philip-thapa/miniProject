from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse


# Create your views here.


def validateUserSession(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validateUserSession(id, token):
        return JsonResponse({'error': 'Please re-login ', 'code': '1'})

    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']
        total_pro = len(products.split(',')[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=id)

        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User doesnot exists'})

        ordr = Order(user=user, product_names=products, total_products=total_pro, transaction_id=transaction_id,
                     total_amount=amount)
        ordr.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order placed successfully'})


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
