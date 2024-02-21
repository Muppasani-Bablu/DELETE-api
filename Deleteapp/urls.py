from django. urls import path
from .views import deleteViews
from Deleteapi.views import check_database_connection
urlpatterns=[
    
    path("delete/student/",deleteViews.as_view(), name='delete-view'),
    path("check_database_connection/",check_database_connection,name='check_database_connection'),
]