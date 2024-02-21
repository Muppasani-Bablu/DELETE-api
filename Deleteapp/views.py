from rest_framework import generics
from Deleteapp.models import delete
from Deleteapp.serializers import deleteserializers
from Deleteapp.utils import api_response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@method_decorator (csrf_exempt,name="dispatch")
class deleteViews(APIView):
  queryset=delete.objects.all()
  serializer_class=deleteserializers
  
  def delete(self,request,*args,**kwargs):
    #get the data form the request
    student_data=self.request.data 
    # Ensure 'sno' is provided in the data
    sno=student_data.get('sno')
    if sno is None:
      # If 'sno' is missing, return an error response
        return Response(400, 'Error: Missing sno in request data', {})
    try:
            # Attempt to get the object to delete
            student_to_delete = delete.objects.get(sno=sno)
    except delete.DoesNotExist:
            # If the object doesn't exist, return a not found response
            return Response({'error': 'Student with provided sno does not exist'}, status=status.HTTP_404_NOT_FOUND)
      
           # Delete a new student instance
    # delete_student=delete.objects.delete(
    # sno=sno,
    # student=student_data.get("student"),
    # classroom=student_data.get("classroom")
    # )
     # Access the delete student's attributes correctly
    student_to_delete.delete()  
    
     
     # Return the response with the created student's information
    return Response({200, 'Successfully created. Please check once'}, status=status.HTTP_204_NO_CONTENT)

          
    