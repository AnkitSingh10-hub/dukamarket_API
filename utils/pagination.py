from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("currentPage", self.page.number),
                    (
                        "nextPage",
                        self.page.next_page_number() if self.page.has_next() else None,
                    ),
                    ("pageSize", self.get_page_size(self.request)),
                    ("totalPages", self.page.paginator.num_pages),
                    ("totalObjects", self.page.paginator.count),
                    ("results", data),
                ]
            )
        )
