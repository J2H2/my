from typing import Tuple

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):
    pass


class BaseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class BasePaginatorReqSerializer(BaseSerializer):
    default_offset = 0
    default_limit = 20

    offset = serializers.IntegerField(required=False)
    limit = serializers.IntegerField(required=False)

    def get_paginator_params(self) -> Tuple[int, int]:
        offset = self.validated_data.get('offset', self.default_offset)
        limit = self.validated_data.get('limit', self.default_limit)

        return offset, limit
