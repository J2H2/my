from typing import List


class BaseRepository:
    model_class = None

    @classmethod
    def create(cls, entities: List[model_class]):
        cls.model_class.objects.bulk_create(entities)

    @staticmethod
    def update(entity: model_class):
        entity.save()

    @classmethod
    def find_all(cls) -> List:
        return cls.model_class.objects.all()
