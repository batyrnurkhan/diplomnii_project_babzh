import random
import string

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PropertyPublishedManager, self)
            .get_queryset()
            .filter(published_status=True)
        )


class Property(TimeStampedUUIDModel):
    class Subject(models.TextChoices):
        CPP = "Cpp", _("cpp") # for sale
        HISTORY = "History", _("History")# for rent
        CYBERSECURITY = "Cyber Security", _("Cyber Security")# auction

    class SubjectType(models.TextChoices):
        TRADITIONAL = "Traditional", _("Traditional")
        ELECTRONIC = "Electronic", _("Electronic")
        OFFICIAL = "Official", _("Official")
        ADDITIONAL = "Additional", _("Additional")
        Practice = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(
        User,
        verbose_name=_("Agent,University or Teacher"),
        related_name="agent_buyer",
        on_delete=models.DO_NOTHING,
    )

    title = models.CharField(verbose_name=_("Course Title"), max_length=250)

    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)

    ref_code = models.CharField(
        verbose_name=_("Course Reference Code"),
        max_length=255,
        unique=True,
        blank=True,
    )

    description = models.TextField(
        verbose_name=_("Description"),
        default="Default description...update me please....",
    )

    country = CountryField(
        verbose_name=_("Country"),
        default="KZ",
        blank_label="(select country)",
    )
    
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Almaty")

    postal_code = models.CharField(
        verbose_name=_("Postal Code"), max_length=100, default="140"
    )

    price = models.DecimalField(
        verbose_name=_("Price"), max_digits=8, decimal_places=2, default=0.0
    )


    course_time = models.DecimalField(
        verbose_name=_("Course Time(hours)"), max_digits=8, decimal_places=2, default=0.0
    )#plot_area
    total_modules = models.IntegerField(verbose_name=_("Number of modules"), default=0)#total floors

    feedback = models.IntegerField(verbose_name=_("Feedback"), default=1)#bedrooms

    lectures = models.DecimalField(
        verbose_name=_("Lectures"), max_digits=8, decimal_places=2, default=1.0#bathrooms
    )

    subject = models.CharField(
        verbose_name=_("Subject"),
        max_length=50,
        choices=Subject.choices,
    )

    subject_type = models.CharField(
        verbose_name=_("Type course"),
        max_length=50,
        choices=SubjectType.choices,
        default=SubjectType.OTHER,
    )

    cover_photo = models.ImageField(
        verbose_name=_("Main Photo"), default="/house_sample.jpg", null=True, blank=True
    )

    photo1 = models.ImageField(
        default="/interior_sample.jpg",
        null=True,
        blank=True,
    )


    published_status = models.BooleanField(
        verbose_name=_("Published Status"), default=False
    )

    views = models.IntegerField(verbose_name=_("Total Views"), default=0)

    objects = models.Manager()
    published = PropertyPublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.capitalize(self.description)
        self.ref_code = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        property_price = self.price
        tax_amount = property_price
        price_after_tax = property_price + tax_amount
        return price_after_tax


class PropertyViews(TimeStampedUUIDModel):
    ip = models.CharField(verbose_name=_("IP Address"), max_length=250)
    property = models.ForeignKey(
        Property, related_name="property_views", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"Total views on - {self.property.title} is - {self.property.views} view(s)"
        )

    class Meta:
        verbose_name = "Total Views on Property"
        verbose_name_plural = "Total Property Views"