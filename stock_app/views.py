from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User, Stock, Transaction
from .serializers import UserSerializer, StockSerializer, TransactionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        ticker_id = request.data.get('ticker')
        transaction_type = request.data.get('transaction_type')
        volume = request.data.get('volume')

        user = User.objects.get(id=user_id)
        stock = Stock.objects.get(id=ticker_id)
        transaction_price = stock.price * int(volume)

        if transaction_type == 'buy' and user.balance < transaction_price:
            return Response({"error": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)

        if transaction_type == 'buy':
            user.balance -= transaction_price
        else:  # sell transaction
            user.balance += transaction_price

        user.save()

        transaction = Transaction.objects.create(
            user=user,
            ticker=stock,
            transaction_type=transaction_type,
            volume=volume,
            transaction_price=transaction_price
        )

        serializer = self.get_serializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
