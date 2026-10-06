from django.contrib import admin
from .models import ContactMessage, Product , FeaturedProduct
from django.utils.html import format_html

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "reply")

    def reply(self, obj):
        return format_html(
            '<a href="mailto:{}?subject=Response from Smoke City">Reply</a>',
            obj.email
        )

    reply.short_description = "Respond"


# Register your models here.
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Product)
admin.site.register(FeaturedProduct)
