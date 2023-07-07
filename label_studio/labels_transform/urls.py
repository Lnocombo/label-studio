from django.urls import path, include


from . import api

app_name = 'label_transform'

_api_urlpatterns = [
    path('', api.transform_list, name='transform-list'),
    path('add/', api.transform_add, name='transform-add'),
    path('update/', api.transform_update, name='transform-update'),
    path('delete/', api.transform_delete, name='transform-delete'),
    path('gray/', api.transform_gray, name='transform-gray'),
]

urlpatterns = [
   path('api/transform/', include((_api_urlpatterns, app_name), namespace='api'))
]