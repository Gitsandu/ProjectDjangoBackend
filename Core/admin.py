from django.contrib import admin
from Core.Models.AuthUser import AuthUser
from Core.Models.Location import Location
from Core.Models.CarBrand import CarBrand
from Core.Models.CarModel import CarModel
from Core.Models.CarVariant import CarVariant
from Core.Models.CarDetails import CarDetails
from Core.Models.CarOverview import CarOverview
from Core.Models.Features import Features
from Core.Models.CarSpecification import CarSpecification
from Core.Models.CarImage import CarImage

admin.site.register(AuthUser)
admin.site.register(Location)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(CarVariant)
admin.site.register(CarDetails)
admin.site.register(Features)
admin.site.register(CarOverview)
admin.site.register(CarSpecification)
admin.site.register(CarImage)
