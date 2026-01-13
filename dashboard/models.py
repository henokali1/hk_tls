from django.db import models

class ExternalApp(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=200, help_text="Relative URL or absolute path (e.g., /dead-hang/)")
    icon = models.CharField(max_length=50, help_text="Emoji or icon class name (e.g., ⏱️)")
    color = models.CharField(max_length=7, default="#38bdf8", help_text="Hex color code")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "External App"
        verbose_name_plural = "External Apps"

    def __str__(self):
        return self.name
