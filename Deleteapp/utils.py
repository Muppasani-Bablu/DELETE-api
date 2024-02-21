from django.http import JsonResponse

def api_response(code,message,data=True):

      
      
    return JsonResponse({
        'code': code,
        'message': message,
        'data': data
    })