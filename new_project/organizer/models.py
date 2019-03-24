"""Django data models for organizing startup company data
Django Model Documentation:
https://docs.djangoproject.com/en/2.1/topics/db/models/
https://docs.djangoproject.com/en/2.1/ref/models/options/
https://docs.djangoproject.com/en/2.1/internals/contributing/writing-code/coding-style/#model-style
Django Field Reference:
https://docs.djangoproject.com/en/2.1/ref/models/fields/
https://docs.djangoproject.com/en/2.1/ref/models/fields/#charfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#datefield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#emailfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#foreignkey
https://docs.djangoproject.com/en/2.1/ref/models/fields/#manytomanyfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#slugfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#textfield
https://docs.djangoproject.com/en/2.1/ref/models/fields/#urlfield
AutoSlugField Reference:
https://django-extensions.readthedocs.io/en/latest/field_extensions.html
"""


from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    URLField,
)


class Tag(Model):

    name = CharField(
        max_length=31,
        unique=True,
    )
    slug = SlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config."
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Startup(Model):

    name = CharField(
        max_length=31,
        db_index=True,
    )
    slug = SlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config."
    )
    description = TextField()
    founded_date = DateField("date founded")
    contact = EmailField()
    website = URLField(max_length=255)
    tags = ManyToManyField(Tag)

    class Meta:
        get_latest_by = "founded_date"
        ordering = ["name"]

    def __str__(self):
        return self.name


class NewsLink(Model):
    name = CharField(max_length=31)
    slug = SlugField(max_length=31)
    pub_date = DateField("date published")
    link = URLField(max_length=255)
    startup = ForeignKey(
        Startup, on_delete=CASCADE
    )

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = ("slug", "startup")
        verbose_name = "news article"

    def __str__(self):
        return f"{self.startup}: {self.title}"


