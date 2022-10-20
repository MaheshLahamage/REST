import json
from sys import api_version
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    data = {}
    model_data = Product.objects.all().order_by("?").first()
    data = model_to_dict(model_data)
    print(data)
    return Response(data)