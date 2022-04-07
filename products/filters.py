from django_filters import FilterSet, NumberFilter, OrderingFilter

from products.models import ProductGroup


class ProductGroupsFilter(FilterSet):
    sub_category_id = NumberFilter(field_name='subcategory_id', lookup_expr='exact')
    ordering = OrderingFilter(
        fields = (

        )
    )

    class Meta:
        model = ProductGroup
        fields = ''