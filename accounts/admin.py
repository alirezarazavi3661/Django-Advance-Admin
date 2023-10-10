from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User,Profile



"""
this is a Custom form that is not needed for now
"""
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("email",)


class CustomUserAdmin(UserAdmin):
    """
    this is a class which customize the admin panel for more information about the user
    """
    model = User
    #add_form = CustomUserCreationForm
    list_display = ('email','first_name','is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('email',)  # Corrected 'searching_fields' to 'search_fields'
    ordering = ('email',)
    fieldsets = (
        ("Authentication", {
            "fields": ("email", "password"),
        }),
        ("Permissions", {
            "fields": ("is_staff", "is_active", "is_superuser","first_name","last_name"),
        }),
        ("Group_Permissions", {
            "fields": ("groups","user_permissions"),
        }),
        ("important_date", {
            "fields": ("last_login",),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )


"""
registration for adding the above class to panel
"""
admin.site.register(User,CustomUserAdmin)
"""
registration for adding the Profile section to admin 
"""
admin.site.register(Profile)







