from django.urls import path, include
from .Controllers.TokenView import TokenView
from .Controllers.AuthUserView import AuthUserViewSet
from rest_framework.routers import DefaultRouter
from .Controllers.LocationView import LocationViewSet
from .Controllers.TokenView import TokenValidationViewSet
from .Controllers.BrandView import BrandViewSet
from .Controllers.ModelView import ModelViewSet
from .Controllers.CarDetailsView import CarDetailsViewSet
from .Controllers.VariantView import VariantViewSet
from .Controllers.CarOverViewViewset import CarOverViewViewSet
from .Controllers.FeaturesViewSet import FeaturesViewSet
from .Controllers.CarSpecificationViewSet import CarSpecificationViewSet
from .Controllers.CarImageViewSet import CarImageViewSet

router = DefaultRouter()
router.register(r'Tokens', TokenView, basename='Token')
router.register(r'Token Validation', TokenValidationViewSet, basename='Token Validation')
router.register(r'Auth User', AuthUserViewSet, basename='Auth User')
router.register(r'Location', LocationViewSet, basename='location')
router.register(r'Brands', BrandViewSet, basename='Brands')
router.register(r'Models', ModelViewSet, basename='Models')
router.register(r'CarDetails', CarDetailsViewSet, basename='Car Details')
router.register(r'Variant', VariantViewSet, basename='Variant')
router.register(r'CarOverView', CarOverViewViewSet, basename='CarOverView')
router.register(r'Features', FeaturesViewSet, basename='Features')
router.register(r'CarSpecification', CarSpecificationViewSet, basename="CarSpecification")
router.register(r'CarImages', CarImageViewSet, basename='CarImages')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('users/', UserView.as_view(), name='user-list-api'),                 # GET: List all users, POST: Create a new user
#     path('users/<int:id>/', UserView.as_view(), name='user-detail-api'),      # GET: Retrieve user by ID
#     path('users/create/', UserView.as_view(), name='user-create-api'),         # POST: Create a new user
#     path('users/delete/<str:ids>/', UserView.as_view(), name='user-delete-api'), 
#     path('users/update/', UserView.as_view(), name='user-update-api'),
    
#     path('users/Token/', TokenView.as_view(), name='token-generate-api'), 
    
#     path('AthUser/', AuthUserView.as_view(), name='user-list-api'),                 # GET: List all users, POST: Create a new user
#     path('AthUser/<int:id>/', AuthUserView.as_view(), name='user-detail-api'),      # GET: Retrieve user by ID
#     path('AthUser/create/', AuthUserView.as_view(), name='user-create-api'),         # POST: Create a new user
#     path('AthUser/delete/<str:ids>/', AuthUserView.as_view(), name='user-delete-api'), 
#     path('AthUser/update/', AuthUserView.as_view(), name='user-update-api'),
    
# ]

    # path('users/<int:id>/update/', UserAPIView.as_view(), name='user-update-api'),# PUT: Update user by ID
    # path('users/<int:id>/delete/', UserAPIView.as_view(), name='user-delete-api'),# DELETE: Delete user by ID