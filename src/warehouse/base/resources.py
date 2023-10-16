from import_export import resources
from .models import warehouse

class uploadResources(resources.ModelResource):
    class meta:
        model = warehouse