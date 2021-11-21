from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from . import config

settings = config.get_settings()


# List View -> Detail View
class Product(Model): # -> table
    __keyspace__ = settings.db_keyspace
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    brand = columns.Text()
    price_str = columns.Text(default="-100")
    country_of_origin = columns.Text()
