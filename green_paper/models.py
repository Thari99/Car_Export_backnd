from django.db import models
from django.utils import timezone

class GreenPaper(models.Model):
    purchaseDate = models.CharField(max_length=100)
    make = models.CharField(max_length=50)
    buyingPrice = models.IntegerField()
    purchasedBy = models.CharField(max_length=255)
    yardLocation = models.IntegerField()
    auctionSetting = models.IntegerField()
    bidNumber = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    transComment = models.CharField(max_length=100)

    dataSource = models.CharField(max_length=255)
    model = models.IntegerField()
    chassisNo = models.CharField(max_length=50)
    requestedBy = models.CharField(max_length=100)
    yardDate = models.CharField(max_length=50)
    auctionCharges = models.IntegerField()
    country = models.CharField(max_length=255)
    auctionSheet = models.FileField(upload_to='auction_sheets/primary/', null=True, blank=True)   
    auctionSheet2 = models.FileField(upload_to='auction_sheets/tertiary/', null=True, blank=True)
    requestedReason = models.CharField(max_length=255)

    stockNumber = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    defaultFobPrice = models.CharField(max_length=255)
    customerName = models.IntegerField()
    transportCompany = models.CharField(max_length=50)
    auctionName = models.CharField(max_length=100)
    firstRegYear = models.CharField(max_length=100)
    auctionSheet1 = models.FileField(upload_to='auction_sheets/secondary/', null=True, blank=True)
    exteriorColor = models.IntegerField()
    shakenDate = models.CharField(max_length=50)
    
    checkSpareKey = models.BooleanField(default=False)
    checkSdCard = models.BooleanField(default=False)
    removeTheHardCopyOfAuctionSheet = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
