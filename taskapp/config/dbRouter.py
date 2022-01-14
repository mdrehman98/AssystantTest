from django.conf import settings

class UserRouter:
    route_app_labels = ['taskapp', 'admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles']
    print('entered user routes')

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'task_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'task_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        print('entered user allow_relation')
        # db_list = ['user_db']
        # print(db_list)
        # if obj1._state.db in db_list and obj2._state.db in db_list:
        #     return True
        # return None

        # def allow_relation(self, obj1, obj2, **hints):

        # if obj1._meta.app_label == 'user_db' and obj2._meta.app_label == 'user_db':
        #     return True
        # # Allow if neither is user app
        # elif 'user_db' not in [obj1._meta.app_label, obj2._meta.app_label]:
        #     return True
        # return False

        if (
                obj1._meta.app_label in self.route_app_labels and
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return obj1._state.db == obj2._state.db

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'task_db':
            return app_label in self.route_app_labels

        elif app_label in self.route_app_labels:
            return False
        return None