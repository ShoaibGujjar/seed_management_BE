from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Seed, Purchase, Sale, Feed
from .serializers import CustomerSerializer, SeedSerializer, PurchaseSerializer,SaleSerializer, SaleSaveSerializer,PurchaseSaveSerializer,FeedSaveSerializer,FeedSerializer
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.generics import ListAPIView

# Customer views
def test(request):
    print(request)

@api_view(['GET', 'POST'])
def CustomerListView(request):
    print(request)
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def PurchaseListView(request):
    if request.method == 'GET':
        customers = Purchase.objects.all()
        serializer = PurchaseSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = PurchaseSaveSerializer(data=request.data ,many= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def SeedListView(request):
    if request.method == 'GET':
        customers = Seed.objects.all()
        serializer = SeedSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        data = request.data
        code = data['code']
        seed = Seed.objects.filter(code = code)
        if seed:
            message = {'code already exist'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer = SeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def SaleListView(request):
    if request.method == 'GET':
        customers = Sale.objects.all()
        serializer = SaleSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = SaleSaveSerializer(data=request.data, many=True)  # Use many=True
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def FeedListView(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = FeedSaveSerializer(data=request.data, many=True)  # Use many=True
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesByCustomer(APIView):
    def get(self,request,id,*args, **kwargs):
        sales=Sale.objects.filter(user=id)
        serializer=SaleSerializer(sales,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class PurchaseByCustomer(APIView):
    def get(self,request,id,*args, **kwargs):
        purchases=Purchase.objects.filter(user=id)
        serializer=PurchaseSerializer(purchases,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class FeedByCustomer(APIView):
    def get(self,request,id,*args, **kwargs):
        feeds=Feed.objects.filter(user=id)
        serializer=FeedSerializer(feeds,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


#not in use at that time
@api_view(['GET', 'PUT', 'DELETE'])
def PurchaseDetailView(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SaleListViewTotal(ListAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        # Filter Sales related to Seeds
        queryset = Sale.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Calculate the totals
        total_sales = queryset.aggregate(
            total_quantity_kg=Sum('quantity_kg'),
            total_price=Sum('price'),
            # total_commission=Sum('commission'),
            total_amount=Sum('amount'),
            total_rent=Sum('rent'),
            total_commission_amount=Sum('commission_amount'),
            total_net_amount=Sum('net_amount')
        )

        # Create a dictionary with the totals
        totals_dict = {
            'total_quantity_kg': total_sales['total_quantity_kg'] or 0,
            'total_price': total_sales['total_price'] or 0,
            # 'total_commission': total_sales['total_commission'] or 0,
            'total_amount': total_sales['total_amount'] or 0,
            'total_rent': total_sales['total_rent'] or 0,
            'total_commission_amount': total_sales['total_commission_amount'] or 0,
            'total_net_amount': total_sales['total_net_amount'] or 0,
        }

        # Create a response with the totals
        response_data = {
            'totals': totals_dict,
            'sales': SaleSerializer(queryset, many=True).data
        }

        return Response(response_data)



@api_view(['GET', 'PUT', 'DELETE'])
def test(request):

    response={
        'sales': []
    }
    seed_instances = Seed.objects.all()
    for i in seed_instances:
        sale = i.total_sales_amount(),
        purchase = i.total_purchase_amount()
        # total = purchase - sale
        response_data = {
           'total_sales': sale,
           'total_purchases': purchase,
           'remain': 0,
        }
        response["sales"].append(response_data)
    return Response(response)




        # print(total_sales)

    # # # Create a dictionary with the totals
    # totals_dict = {
    #     'total_quantity_kg': total_sales['total_quantity_kg'] or 0,
    #     'total_price': total_sales['total_price'] or 0,
    #     # 'total_commission': total_sales['total_commission'] or 0,
    #     'total_amount': total_sales['total_amount'] or 0,
    #     'total_rent': total_sales['total_rent'] or 0,
    #     'total_commission_amount': total_sales['total_commission_amount'] or 0,
    #     'total_net_amount': total_sales['total_net_amount'] or 0,
    # }

    # Create a response with the totals
        # response_data = {
        #     # 'totals': list,
        #
        # }

