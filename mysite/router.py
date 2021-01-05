from tradeanalyzer.models.dbsetting import DbSetting

class MultiDBRouter(object):
    def db_for_read(self, model, **hints):
        if model == DbSetting:
            print(__name__, 'db_for_read, default', model)
            return 'trade_setting'
        if model._meta.app_label == 'tradeanalyzer':
            return 'trade_data'
        return 'default'

    def db_for_write(self, model, **hints):
        if model == DbSetting:
            print(__name__, 'db_for_read, default', model)
            return 'trade_setting'
        if model._meta.app_label == 'tradeanalyzer':
            return 'trade_data'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'trade_data':
            if app_label == 'tradeanalyzer':
                return True
            else:
                return False
        return True

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'tradeanalyzer' or \
           obj2._meta.app_label == 'tradeanalyzer':
           return True
        return None


