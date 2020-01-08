from django.db import models

# Create your models here.
class Gift(models.Model):
	giftTitle = models.CharField(max_length=100, default="")
	webAddress = models.CharField(max_length=200, default="")
	comment = models.TextField(max_length=200, default="")
	price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	image = models.URLField(null=True)

	def __str__(self):
		return self.giftTitle
		return self.comment
		return self.price
		return self.webAddress
		return self.image
