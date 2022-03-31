from django_filters import FilterSet, NumberFilter, OrderingFilter


class ProductGroupsFilter(FilterSet):
    sub_category_id = NumberFilter()
    ordering = OrderingFilter(
        fields = (
            
        )
    )