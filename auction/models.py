from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True, unique=True)
    password = models.CharField(max_length=128)  
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class AdministrativeStaffMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class CustomerRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class EndUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    anonymize = models.BooleanField(default=False)


class Alert(models.Model):
    end_user_id = models.ForeignKey(EndUser, on_delete=models.CASCADE) 
    timestamp = models.DateTimeField()
    message = models.CharField(max_length=3000)

    class Meta:
        unique_together = ('end_user_id', 'message')


class Question(models.Model):
    ques_id = models.CharField(max_length=255, primary_key=True)
    ques_text = models.CharField(max_length=500)
    ans_text = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, default='pending')
    timestamp_asked = models.DateTimeField()
    timestamp_resolved = models.DateTimeField(blank=True, null=True)
    end_user = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    customer_rep = models.ForeignKey(CustomerRepresentative, on_delete=models.SET_NULL, blank=True, null=True)


class Category(models.Model):
    cat_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)

class Subcategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('cat_id', 'subcat_id')
        indexes = [models.Index(fields=['cat_id', 'subcat_id'])]


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField()
    desc_1 = models.CharField(max_length=100, blank=True, null=True)
    desc_2 = models.CharField(max_length=100, blank=True, null=True)
    desc_3 = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(EndUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('item_id','subcategory')


class Auction(models.Model):
    auction_id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    starting_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    initial_price = models.IntegerField()
    increment_price = models.IntegerField()
    minimum_price = models.IntegerField(blank=True, null=True)
    curr_winner = models.ForeignKey(EndUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='won_auctions')
    curr_price = models.IntegerField(blank=True, null=True)


class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    amount = models.IntegerField()

class AutoBid(models.Model):
    user_id = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    upper_limit = models.IntegerField()

    class Meta:
        unique_together = ('user_id', 'auction_id')


class Wishlist(models.Model):
    user_id = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('user_id', 'item_id','subcategory')
