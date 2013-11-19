from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from HNBC.models import RFIDKey, RFIDLog


# Define an inline admin descriptor for RFIDKey model
class RFIDInline(admin.StackedInline):
    model = RFIDKey


# Define a standalone admin descriptor
class RFIDAdmin(admin.ModelAdmin):
    model = RFIDKey
    list_display = [
        'code',
        'user',
    ]
    search_fields = [
        'user__email',
        'user__first_name',
        'user__last_name',
    ]
    list_filter = (
        'user__email',
    )


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (RFIDInline, )


# Log for RFID scans- eventually we'll want to replace this with a more full-featured
# set of models for handling charges, products, etc.
class RFIDLogAdmin(admin.ModelAdmin):
    model = RFIDLog


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register standalones
admin.site.register(RFIDKey, RFIDAdmin)
admin.site.register(RFIDLog, RFIDLogAdmin)
