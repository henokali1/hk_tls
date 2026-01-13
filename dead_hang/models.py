from django.db import models

class HangSession(models.Model):
    duration = models.FloatField(help_text="Duration in seconds")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.duration}s on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
