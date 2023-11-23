class Sort:

    def __init__(self, coll):
        if self._get_type_correct(coll):
            self._coll = coll
        else:
            self._coll = None

    @property
    def coll(self):
        return self._coll

    @coll.setter
    def coll(self, value):
        if self._get_type_correct(value):
            self._coll = value
        else:
            self._coll = None

    def _get_type_correct(self, value):
        return isinstance(value, list) | isinstance(value, dict)

    # Пузырьковая сортировка
    def _sort1(self):
        if self._coll == None:
            return
        for i in range(len(self._coll)):
            for j in range(len(self._coll) - i - 1):
                a = self._coll[j]
                b = self._coll[j + 1]
                if a > b:
                    self._coll[j] = b
                    self._coll[j + 1] = a


c = Sort([1, 4, 8, 2, 3, 6, 3, 5])
print(c.coll)
c._sort1()
print(c.coll)

