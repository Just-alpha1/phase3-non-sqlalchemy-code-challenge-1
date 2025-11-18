from article import Article

class Magazine:

    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")

        self._name = name
        self._category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise Exception("Name must be 2–16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        if len(value) == 0:
            raise Exception("Category must be longer than 0")
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        if not self.articles():
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        authors = self.contributors()
        result = []
        for author in authors:
            count = len([a for a in self.articles() if a.author is author])
            if count > 2:
                result.append(author)
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda m: len(m.articles()))
