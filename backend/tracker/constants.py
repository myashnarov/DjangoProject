from django.db.models import IntegerChoices

class ProductStatus(IntegerChoices):
    DOING = 0, "doing"
    STOP = 1, "stop"
    DONE = 2, "done"
    ERROR = 3, "error"
    
class Markets(IntegerChoices):
    UZUM_MARKET = 0, "uzum_market"
    WILDBERRIES = 1, "wildberries"