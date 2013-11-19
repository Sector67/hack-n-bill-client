from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from HNBC.models import RFIDKey


# Define an inline admin descriptor for RFIDKey model
class RFIDInline(admin.StackedInline):
    model = RFIDKey


# Define a standalone admin descriptor
class RFIDAdmin(admin.ModelAdmin):
    model = RFIDKey
    search_fields = [
        'user__email',
        'user__first_name',
        'user__last_name'
    ]
    list_filter = ('user__email',)

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (RFIDInline, )



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register standalone
admin.site.register(RFIDKey, RFIDAdmin)
