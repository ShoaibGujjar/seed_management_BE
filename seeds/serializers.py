from rest_framework import serializers
from .models import Customer, Seed, Purchase, Sale, Feed, Ledger


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SeedSerializer(serializers.ModelSerializer):
    total_sales_amount = serializers.SerializerMethodField()
    total_purchase_amount = serializers.SerializerMethodField()
    total_feed_amount = serializers.SerializerMethodField()
    profit = serializers.SerializerMethodField()
    total_sale_stock = serializers.SerializerMethodField()
    total_purchase_stock = serializers.SerializerMethodField()
    total_feed_stock = serializers.SerializerMethodField()
    stock = serializers.SerializerMethodField()
    class Meta:
        model = Seed
        fields = ['id', 'name', 'code', 'amount', 'total_sales_amount', 'total_purchase_amount', 'total_feed_amount', 'profit', 'total_purchase_stock','total_sale_stock', 'total_feed_stock', 'stock']

    def get_total_sales_amount(self, obj):
        # Calculate and return the total sales amount for this seed
        total_sales = obj.total_sales_amount()
        return total_sales

    def get_total_purchase_amount(self, obj):
        # Calculate and return the total purchase amount for this seed
        total_purchases = obj.total_purchase_amount()
        return total_purchases

    def get_total_feed_amount(self, obj):
        # Calculate and return the total purchase amount for this seed
        total_feeds = obj.total_purchase_amount()
        return total_feeds

    def get_profit(self, obj):
        # Calculate and return the profit for this seed
        total_sales = obj.total_sales_amount()
        total_purchases = obj.total_purchase_amount()
        total_feeds = obj.total_feed_amount()
        return total_purchases - total_sales - total_feeds

    def get_total_sale_stock(self, obj):
        total_sales_stock = obj.total_sale_stock()
        return total_sales_stock

    def get_total_purchase_stock(self, obj):
        total_purchases_stock = obj.total_purchase_stock()
        return total_purchases_stock

    def get_total_feed_stock(self, obj):
        total_feeds_stock = obj.total_purchase_stock()
        return total_feeds_stock

    def get_stock(self, obj):
        # Calculate and return the profit for this seed
        sales_stock = obj.total_sale_stock()
        purchases_stock = obj.total_purchase_stock()
        feeds_stock = obj.total_feed_stock()

        return purchases_stock - sales_stock - feeds_stock



class CustomerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name']

class SeedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = ['name']

class PurchaseSerializer(serializers.ModelSerializer):
    user =CustomerNameSerializer(read_only=True)
    item = SeedNameSerializer(read_only=True)
    class Meta:
        model = Purchase
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    user = CustomerNameSerializer(many=False)
    item = SeedNameSerializer(many=False)

    class Meta:
        model = Sale
        fields = '__all__'



class PurchaseSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user
        serializer = CustomerNameSerializer(user, many=False)
        return serializer.data

    def get_item(self, obj):
        item = obj.item
        serializer = SeedNameSerializer(item, many=False)
        return serializer.data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = self.get_user(instance)
        data['item'] = self.get_item(instance)

        return data

class SaleSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user
        serializer = CustomerNameSerializer(user, many=False)
        return serializer.data

    def get_item(self, obj):
        item = obj.item
        serializer = SeedNameSerializer(item, many=False)
        return serializer.data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = self.get_user(instance)
        data['item'] = self.get_item(instance)

        return data

class FeedSerializer(serializers.ModelSerializer):
    user = CustomerNameSerializer(many=False)
    item = SeedNameSerializer(many=False)

    class Meta:
        model = Feed
        fields = '__all__'
class FeedSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user
        serializer = CustomerNameSerializer(user, many=False)
        return serializer.data

    def get_item(self, obj):
        item = obj.item
        serializer = SeedNameSerializer(item, many=False)
        return serializer.data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = self.get_user(instance)
        data['item'] = self.get_item(instance)

        return data
    

class LedgerSerializer(serializers.ModelSerializer):
    user = CustomerNameSerializer(many=False)

    class Meta:
        model = Ledger
        fields = '__all__'


class LedgerSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ledger
        fields = '__all__'

    def get_user(self, obj):
        user = obj.user
        serializer = CustomerNameSerializer(user, many=False)
        return serializer.data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = self.get_user(instance)

        return data