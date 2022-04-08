from django.core.paginator import Paginator

class CustomPaginator(Paginator):
    """object_list를 QuerySet이 아닌 list로 변환해두어 여러번 요청하지 않고 데이터 처리"""

    def __init__(self, object_list, per_page, orphans=0, allow_empty_first_page=True):
        super().__init__(list(object_list), per_page, orphans, allow_empty_first_page)