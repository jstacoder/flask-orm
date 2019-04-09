from sqlalchemy.orm import Query


class BaseQuery(Query):
    @classmethod
    def all(cls):
        # type: () -> None
        pass

    @classmethod
    def first(cls):
        # type: () -> None
        pass
