from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utilis import *
from .models import Transaction

@api_view(['POST'])
def process_transaction(request):
    amount = float(request.data['amount'])
    currency = request.data['currency']
    fee = calculate_fee(amount)
    reference = generate_reference()


    Transaction.objects.create(
        reference=reference,
        amount=amount,
        currency=currency,
        fee=fee
    )

    return Response({
        "reference": reference,
        "amount": amount,
        "fee": fee,
        "total": amount + fee
    })


@api_view(['GET'])
def convert(request):
    try:
        amount = float(request.GET.get('amount'))
        from_currency = request.GET.get('from_currency')
        to_currency = request.GET.get('to_currency')

        converted = convert_currency(amount, from_currency, to_currency)

        return Response({
            "amount": amount,
            "from": from_currency,
            "to": to_currency,
            "converted_amount": converted
        })
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def validate_number(request):
    number = request.GET['number']
    valid = validate_mobile_money(number)
    return Response({"valid": valid})