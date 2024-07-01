from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests

@require_GET
def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = get_client_ip(request)
    location = "New York"  # For simplicity, we'll assume the location is always New York
    temperature = 11  # Hardcoded temperature for demonstration purposes

    response_data = {
        'client_ip': client_ip,
        'location': location,
        'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}'
    }
    return JsonResponse(response_data)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
