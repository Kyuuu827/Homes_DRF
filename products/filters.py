from django_filters import FilterSet, NumberFilter, OrderingFilter

from products.models import Product, ProductGroup


class ProductGroupsFilter(FilterSet):
    sub_category_id = NumberFilter(field_name='sub_category_id', lookup_expr='exact')
    order_by_field = 'ordering'
    ordering = OrderingFilter(
        fields = ([
            'best_ranking', 
            'review_count', 
            'review_star_point', 
            'discounted_price', 
            'latest_update'
        ])
    )

    class Meta:
        model = ProductGroup
        fields = ''


class ProductGroupFilter(FilterSet):

    class Meta:
        model = Product
        fields = ''