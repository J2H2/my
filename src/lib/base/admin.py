from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    list_per_page = 20

    def get_actions(self, request):
        # Disable delete
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None) -> bool:
        # Disable delete
        return False


class BasePrefetchModelAdmin(BaseModelAdmin):
    # Separate req for inner join elimination
    list_select_related = ()
    list_prefetch_related = ()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related(self.list_prefetch_related)
