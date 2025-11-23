from rest_framework.routers import SimpleRouter
from spa_tables.views import TableDataViewSet
from spa_tables.apps import SpaTablesConfig

app_name = SpaTablesConfig.name

router = SimpleRouter()
router.register("", TableDataViewSet)

urlpatterns = []
urlpatterns += router.urls