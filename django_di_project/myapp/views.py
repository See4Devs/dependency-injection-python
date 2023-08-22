from django.http import JsonResponse
from injector import inject
from django.views import View
from myapp.services import DataService  # Import your DataService class

class MyView(View):
    @inject
    def __init__(self, data_service: DataService):
        self.data_service = data_service
        super().__init__()

    def get(self, request):
        data = self.data_service.fetch_data()
        return JsonResponse(data)
