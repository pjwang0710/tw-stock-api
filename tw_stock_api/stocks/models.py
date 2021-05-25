from django.db import models


class TaiwanStockInfo(models.Model):
    industry_category = models.CharField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=100, null=False)
    stock_name = models.CharField(max_length=150, null=False)
    type = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'TaiwanStockInfo'
        unique_together = (('industry_category', 'stock_id'),)

    def __str__(self):
        return self.stock_id
