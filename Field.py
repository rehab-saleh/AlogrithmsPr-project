from abc  import ABC

class Field(ABC):
    field_type = None

    def __init__(self,max_length=255, unique=None):
        if unique is True:
            self.unique = 'UNIQUE'
        else:
            self.unique = ''

        if max_length:
            self.max_length = max_length

    def __ropr__(self):
        column = []
        if self.field_type == 'VARCHAR':
            column.append(f'VARCHAR({self.max_length}')
        else:
            column.append(self.field_type)
            column.append(self.unique)
        return ''.join(column).strip()


class charField(Field):
    field_type = 'VARCHAR'

    def __init__(self, max_length=255, unique=None):
        self.max_length = max_length
        self.unique = unique
        super().__init__(max_length=max_length, unique=unique)



class TextField(Field):
    field_type = 'TEXT'

    def __init__(self,unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class IntegerField(Field):
    field_type = 'INTEGER'

    def __add__(self, unique=None):
     self.unique = unique
     super().__init__(unique=unique)


class FloatField(Field):
    field_type = 'REAL'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class BooleamField(Field):
   field_type = 'INTEGER'

   def __init__(self, unique=None):
        self,unique = unique
        super().__init__(unique=unique)


class DataTimeField(Field):
    field_type = 'TIMESTAMP'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique )
