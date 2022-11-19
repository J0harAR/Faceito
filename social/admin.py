from django.contrib import admin
from .models import Profile,Post,Usuario,UserDetails
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin  as AuthUserAdmin
class DetallesUserInline(admin.StackedInline):
    model=UserDetails
    can_delete=False
class AccountUserAdmin(AuthUserAdmin):
    inlines=[DetallesUserInline]


admin.site.unregister(User)
admin.site.register(User,AccountUserAdmin)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Usuario)


    


