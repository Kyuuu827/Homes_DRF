from django.db.models              import Avg, F, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets   import GenericViewSet
from rest_framework.mixins     import ListModelMixin
from rest_framework.response   import Response
from rest_framework.decorators import action
from products.defaultPagination import DefaultPagination

from products.filters import ProductGroupFilter, ProductGroupsFilter

from .models                 import Menu, ProductGroup
from .serializers            import MenuSerializer, ProductGroupSerializer, ProductGroupsSerializer


class MenuListViewSet(ListModelMixin, GenericViewSet):
    queryset = Menu.objects.prefetch_related('category_set', 'category_set__subcategory_set').all()       
    serializer_class = MenuSerializer


class ProductGroupsViewSet(ListModelMixin, GenericViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupsSerializer
    pagination_class = DefaultPagination
    filter_class = ProductGroupsFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = super().get_queryset()
        
        sub_category_id = self.request.query_params.get('sub_category_id', '')

        if sub_category_id:
            queryset.filter(sub_category_id = sub_category_id).annotate(
                best_ranking      = Avg('review__star_rate'),
                review_count      = Count('review'),
                review_star_point = Avg('review__star_rate'),
                discounted_price  = F('displayed_price') - F('displayed_price') * (F('discount_rate')/100),
                latest_update     = F('created_at')
                )
        
        return queryset


class ProductGroupViewSet(ListModelMixin,GenericViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
    pagination_class = DefaultPagination
    filter_class = ProductGroupFilter
    filter_backends = [DjangoFilterBackend]


# class ProductGroupsView(View):
#     def get(self, request):
#         sub_category_id = request.GET.get("SubCategoryId")
#         ordering        = request.GET.get("ordering")
#         OFFSET          = int(request.GET.get("offset", 0))
#         LIMIT           = int(request.GET.get("limit", 16))

#         product_groups = ProductGroup.objects.filter(sub_category_id = sub_category_id).annotate(
#             best_ranking      = Avg('review__star_rate'),
#             review_count      = Count('review'),
#             review_star_point = Avg('review__star_rate'),
#             discounted_price  = F('displayed_price') - F('displayed_price') * (F('discount_rate')/100),
#             latest_update     = F('created_at')
#         ).order_by(ordering)[OFFSET:OFFSET+LIMIT]
        
#         results = [
#             {
#             'id'               : product_group.id,
#             'company'          : product_group.company,
#             'product_name'     : product_group.name,
#             'price'            : float(product_group.displayed_price),
#             'image_url'        : product_group.productimage_set.all()[0].image_url,
#             'discount_rate'    : float(product_group.discount_rate),
#             'discounted_price' : float(round(product_group.discounted_price,0)),
#             'star_point'       : float(product_group.review_star_point),
#             'review'           : product_group.review_count
#             }for product_group in product_groups]

#         return JsonResponse({'product_groups':results}, status = 200)


# class ProductGroupView(View):
#     def get(self, request, id):
#         try:

#             product_groups   = ProductGroup.objects.prefetch_related('product_set').select_related('delivery').annotate(
#                 star_ranking     = Avg('review__star_rate'),
#                 discounted_price = F('displayed_price') - F('displayed_price')  * (F('discount_rate')/100)
#             ).get(id=id)

#             product_group = {
#                 'id'                : product_groups.id,
#                 'name'              : product_groups.name,
#                 'displayed_price'   : float(product_groups.displayed_price),
#                 'discount_rate'     : float(product_groups.discount_rate),
#                 'discounted_price'  : float(round(product_groups.discounted_price,0)),
#                 'star_point'        : float(round((product_groups.star_ranking),1)),
#                 'image'             : [product.image_url for product in product_groups.productimage_set.all()],
#                 'company'           : product_groups.company,
#                 'delivery_type'     : product_groups.delivery.delivery_type,
#                 'payment_type'      : product_groups.delivery.payment_type,
#                 'delivery_fee'      : float(product_groups.delivery.delivery_fee),
#                 'product'           : [
#                     {
#                         'id' : product.id,
#                         'name' : product.name,
#                         'price' : product.price,
#                     } for product in product_groups.product_set.all()
#                 ],
#                 'color' : list(product_groups.product_set.all()[0].colors.values("name","id"))
#             }

#             return JsonResponse({'product_group' : product_group}, status=200)
        
#         except ProductGroup.DoesNotExist:
#             return JsonResponse({'message' : 'INVALID_PRODUCT'}, status=404)
