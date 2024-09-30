from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import Product

# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "inventory/index.html"
    context_object_name = "products"
    paginate_by = 10
    ordering = 'pk'
    
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "inventory/list.html"
        else:
            return self.template_name
    

