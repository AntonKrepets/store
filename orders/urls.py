from django.urls import path

from orders.views import (CancelledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SuccessTemplateview)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-success/', SuccessTemplateview.as_view(), name='order_success'),
    path('order-cancelled/', CancelledTemplateView.as_view(), name='order_cancelled'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_view')
]
