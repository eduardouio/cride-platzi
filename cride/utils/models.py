from django.db import models


class CRideModel(models.Model):
    """Base model for all models."""
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time when the object was created.'
        )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time when the object was last modified.'
    )
    
    class Meta:
        abstract = True
        
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
