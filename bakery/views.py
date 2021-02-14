from django.shortcuts import render
from rest_framework.views import APIView
from bakery.models import BakeryItem, Order
from django.http import JsonResponse
from bakery.custom_exceptions import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from bakery.models import *
import json
from users.models import User
# Create your views here.

@method_decorator([login_required], name='dispatch')
class AllProducts(APIView):

    def get(self, request):

        try:
            all_products = list(BakeryItem.objects.all().values_list('name', flat=True))
            json_response = {
                "products": all_products
            }
            return JsonResponse(json_response, status=200)

        except Exception as e:
            raise InternalServerError()

@method_decorator([login_required], name='dispatch')
class PlaceOrder(APIView):

    def post(self, request, *args, **kwargs):

        try:
            data = request.data
            items = data.get('items', None)
            user = request.user
            order = Order.objects.create(customer=Customer.objects.get(user=user))
            total_amount = 0
            generated_bill = {'Customer Name': user.username, 'address': user.customer_set.first().address, 'items': {}}
            for item, value in items.items():
                quantity = value['quantity']
                discount = value['discount']
                try:
                    bakery_item = BakeryItem.objects.get(name=item)
                except BakeryItem.DoesNotExist:
                    raise BadRequest("Item with name {} Does Not Exist".format(item))
                item_amount = bakery_item.selling_price - (bakery_item.selling_price*(discount/100))
                total_amount = total_amount + item_amount
                order_item = OrderItem.objects.create(item=bakery_item, quantity=quantity, discount=discount)
                order.order_items.add(order_item)
                generated_bill['items'][item] = {'payable': item_amount, 'quantity': quantity, 'discount': discount, 'MRP': bakery_item.selling_price}
            generated_bill['Total Payable Amount'] = total_amount
            order.amount_due = total_amount
            order.bill = json.dumps(generated_bill)
            order.save()
            return JsonResponse(generated_bill, status=200)
        except BadRequest as bad_request:
            raise bad_request
        except Exception as e:
            raise InternalServerError()

@method_decorator([login_required], name='dispatch')
class OrderHistory(APIView):

    def get(self, request):

        try:
            all_orders = Order.objects.filter(customer__user__id=request.user.id)
            json_response = {
                "orders": {}
            }
            for order in all_orders:
                json_response['orders']['id'] = order.id
                json_response['orders']['amount_due'] = order.amount_due
                json_response['orders']['amount_paid'] = order.amount_paid
                json_response['orders']['generated_date'] = order.generated_date
                json_response['orders']['items'] = {}
                for item in order.order_items.all():
                    json_response['orders']['items']['name'] = item.item.name
                    json_response['orders']['items']['quantity'] = item.quantity
                    json_response['orders']['items']['discount'] = item.discount

            return JsonResponse(json_response, status=200)

        except Exception as e:
            print(e)
            raise InternalServerError()
