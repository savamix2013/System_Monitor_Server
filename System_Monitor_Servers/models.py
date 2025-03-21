from django.db import models

# Create your models here.

class Server(models.Model):
    """Атрибути: ID, назва, IP-адреса, тип, операційна система. Методи: отримати статус, оновити конфігурацію."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField()
    type = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_status(self):
        """Отримати статус сервера."""
        pass

    def update_configuration(self):
        """Оновити конфігурацію сервера."""
        pass

    def __str__(self):
        return self.name
    
class Metric(models.Model):
    """Клас Metric (абстрактний). Атрибути: тип метрики, значення, часова мітка. Методи: отримати значення, встановити значення."""
    id = models.AutoField(primary_key=True)
    metric_type = models.CharField(max_length=50)
    value = models.FloatField()
    time_stamp = models.DateTimeField()

    def get_value(self):
        """Отримати значення метрики."""
        pass

    def set_value(self):
        """Встановити значення метрики."""
        pass

    class Meta:
        abstract = True
    
class CPUMetric(Metric):
    """Клас CPUMetric (наслідується від Metric). Атрибути: тип метрики (CPU), значення, часова мітка. Методи: отримати значення, встановити значення."""
    pass

class MemoryMetric(Metric):
    """Клас MemoryMetric (наслідується від Metric). Атрибути: тип метрики (Memory), значення, часова мітка. Методи: отримати значення, встановити значення."""
    pass

class DiskMetric(Metric):
    """Клас DiskMetric (наслідується від Metric). Атрибути: тип метрики (Disk), значення, часова мітка. Методи: отримати значення, встановити значення."""
    pass

class NetworkMetric(Metric):
    """Клас NetworkMetric (наслідується від Metric). Атрибути: тип метрики (Network), значення, часова мітка. Методи: отримати значення, встановити значення."""
    pass

class Alert(models.Model):
    """Атрибути: тип сповіщення, рівень критичності, повідомлення, часова мітка. Методи: створити сповіщення, відправити сповіщення"""
    id = models.AutoField(primary_key=True)
    alert_type = models.CharField(max_length=50)
    critical_level = models.IntegerField()
    message = models.TextField()
    time_stamp = models.DateTimeField()

    def create_alert(self):
        """Створити сповіщення."""
        pass

    def send_alert(self):
        """Відправити сповіщення."""
        pass

    def __str__(self):
        return self.message
    
class Dashboard(models.Model):
    """Атрибути: назва, список віджетів. Методи: додати віджет, видалити віджет, оновити дані"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    widgets = models.ManyToManyField('Widget')

    def add_widget(self):
        """Додати віджет."""
        pass

    def remove_widget(self):
        """Видалити віджет."""
        pass

    def update_data(self):
        """Оновити дані."""
        pass

    def __str__(self):
        return self.name
    
class Widget(models.Model):
    """Атрибути: тип віджету, джерело даних, налаштування відображення. Методи: оновити дані, відобразити віджет"""
    id = models.AutoField(primary_key=True)
    widget_type = models.CharField(max_length=50)
    data_source = models.CharField(max_length=50)
    display_settings = models.TextField()

    def update_data(self):
        """Оновити дані."""
        pass

    def display_widget(self):
        """Відобразити віджет."""
        pass

    def __str__(self):
        return self.widget_type
    
class DataCollector(models.Model):
    """Атрибути: список серверів для збору даних, інтервал збору. Методи: почати збір даних, зупинити збір, обробити зібрані дані"""
    id = models.AutoField(primary_key=True)
    servers = models.ManyToManyField('Server')
    collection_interval = models.IntegerField()

    def start_collection(self):
        """Почати збір даних."""
        pass

    def stop_collection(self):
        """Зупинити збір."""
        pass

    def process_data(self):
        """Обробити зібрані дані."""
        pass

    def __str__(self):
        return f'DataCollector {self.id}'
    
class DataStorage(models.Model):
    """Атрибути: тип сховища (бази даних), налаштування підключення. Методи: зберегти дані, отримати дані, очистити старі дані"""
    id = models.AutoField(primary_key=True)
    storage_type = models.CharField(max_length=50)
    connection_settings = models.TextField()

    def save_data(self):
        """Зберегти дані."""
        pass

    def get_data(self):
        """Отримати дані."""
        pass

    def clear_old_data(self):
        """Очистити старі дані."""
        pass

    def __str__(self):
        return self.storage_type
    
class AlertManager(models.Model):
    """Атрибути: правила сповіщень, список активних сповіщень. Методи: перевірити умови сповіщень, створити сповіщення, відправити сповіщення"""
    id = models.AutoField(primary_key=True)
    alert_rules = models.ManyToManyField('AlertRule')
    active_alerts = models.ManyToManyField('Alert')

    def check_alert_conditions(self):
        """Перевірити умови сповіщень."""
        pass

    def create_alert(self):
        """Створити сповіщення."""
        pass

    def send_alert(self):
        """Відправити сповіщення."""
        pass

    def __str__(self):
        return f'AlertManager {self.id}'
    
class MonitoringSystem(models.Model):
    """Атрибути: список серверів, колектор даних, сховище даних, менеджер сповіщень. Методи: додати сервер, налаштувати моніторинг, генерувати звіти."""
    id = models.AutoField(primary_key=True)
    servers = models.ManyToManyField('Server')
    data_collector = models.ForeignKey('DataCollector', on_delete=models.CASCADE)
    data_storage = models.ForeignKey('DataStorage', on_delete=models.CASCADE)
    alert_manager = models.ForeignKey('AlertManager', on_delete=models.CASCADE)

    def add_server(self):
        """Додати сервер."""
        pass

    def configure_monitoring(self):
        """Налаштувати моніторинг."""
        pass

    def generate_reports(self):
        """Генерувати звіти."""
        pass

    def __str__(self):
        return f'MonitoringSystem {self.id}'
    
class AlertRule(models.Model):
    """Атрибути: тип сповіщення, умови сповіщення. Методи: перевірити умови сповіщення."""
    id = models.AutoField(primary_key=True)
    alert_type = models.CharField(max_length=50)
    conditions = models.TextField()

    def check_conditions(self):
        """Перевірити умови сповіщення."""
        pass

    def __str__(self):
        return self.alert_type

class AutoScaler(models.Model):
    """Реалізуйте методи для визначення оптимальної конфігурації серверів на основі поточного навантаження"""
    pass

class SecurityMonitor(models.Model):
    """Реалізуйте методи для аналізу логів, виявлення аномалій у мережевому трафіку та сповіщення про потенційні загрози"""
    pass

class CloudIntegration(models.Model):
    """Реалізуйте методи для інтеграції з хмарними сервісами для збереження даних та моніторингу"""
    pass


class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name