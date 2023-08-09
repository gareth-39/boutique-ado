from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    For product categories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Returns products and their details
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.sku:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Add comments to a product
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order the comments by recently created first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
