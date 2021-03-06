from django.urls import path

# from product.views.product import CreateProductView
# from product.views.variant import VariantView, VariantCreateView, VariantEditView
from . import views
app_name = "product"

urlpatterns = [
    # Variants URLs
    # path('variants/', VariantView.as_view(), name='variants'),
    path('home/', views.home, name='variants'),
    # path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    # path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # # Products URLs
    # path('create/', CreateProductView.as_view(), name='create.product'),
    # path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
    #     'product': True
    # }), name='list.product'),
]
