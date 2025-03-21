from django.contrib import admin

# Register your models here.

from .models import Server
from .models import CPUMetric
from .models import MemoryMetric
from .models import DiskMetric
from .models import NetworkMetric
from .models import Alert
from .models import DataStorage
from .models import AlertRule
from .models import AutoScaler
from .models import SecurityMonitor
from .models import CloudIntegration
from .models import Topic



admin.site.register(Server)
admin.site.register(CPUMetric)
admin.site.register(MemoryMetric)
admin.site.register(DiskMetric)
admin.site.register(NetworkMetric)
admin.site.register(Alert)
admin.site.register(DataStorage)
admin.site.register(AlertRule)
admin.site.register(AutoScaler)
admin.site.register(SecurityMonitor)
admin.site.register(CloudIntegration)
admin.site.register(Topic)