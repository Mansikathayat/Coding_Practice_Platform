from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def test_json(request):
    return JsonResponse({'message': 'JSON working', 'status': 'success'})