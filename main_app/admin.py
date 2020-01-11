from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from main_app.models import *

admin.site.register(Slide)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CommonPageDescription)
admin.site.register(ContactEmail)
admin.site.register(ContactPhone)


@admin.register(UserEmail)
class UserEmailAdmin(ImportExportModelAdmin):
    pass
