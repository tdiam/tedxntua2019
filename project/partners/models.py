from django.db import models
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

class Partner(models.Model):
    '''Model for partners of the TEDxNTUA 2019 organization.

    The `partner_type` attribute is represented as a CharField with limited possible
    values. The definition follows the official documentation example:
    https://docs.djangoproject.com/en/2.1/ref/models/fields/#choices

    The `link` attribute is represented as a URLField. The definition follows
    the official documentation example:
    https://docs.djangoproject.com/en/2.1/ref/models/fields/#urlfield
    '''
    GRAND_SPONSORS_PLUS = 'GSP'
    GRAND_SPONSORS = 'GS'
    SPONSORS = 'SPO'
    SUPPORTERS = 'SUP'
    MEDIA_PARTNERS = 'MP'
    COMMUNITY_PARTNERS = 'CP'
    PARTNER_TYPES = (
        (GRAND_SPONSORS_PLUS, 'Grand Sponsors Plus'),
        (GRAND_SPONSORS, 'Grand Sponsors'),
        (SPONSORS, 'Sponsors'),
        (SUPPORTERS, 'Supporters'),
        (MEDIA_PARTNERS, 'Media Partners'),
        (COMMUNITY_PARTNERS, 'Community Partners'),
    )

    name = models.CharField(max_length=255, verbose_name='name')
    partner_type = models.CharField(max_length=3, choices=PARTNER_TYPES)
    link = models.URLField()

    image = VersatileImageField(
        'Image',
        upload_to='static/',
        width_field='image_width',
        height_field='image_height'
    )
    image_height = models.PositiveIntegerField(editable=False, null=True)
    image_width = models.PositiveIntegerField(editable=False, null=True)

    def __str__(self):
        '''Objects of the Partner class are represented as strings by
        their name
        '''
        return self.name


@receiver(models.signals.post_save, sender=Partner)
def WarmPartnerImages(sender, instance, **kwargs):
    '''Ensures images are created post-save.
    Image sizes are stored in base.VERSATILEIMAGEFIELD_RENDITION_KEY_SETS.
    Using a thumbnail__AxA rendition key, the image fits in a AxA rectangle by
    maintaining the aspect ratio.

    Documentation link:
    https://django-versatileimagefield.readthedocs.io/en/latest/overview.html#create-images-wherever-you-need-them
    '''


    img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='Sizes',
        image_attr='image',
        verbose=True
    )
    num_created, failed_to_create = img_warmer.warm()
