from article import Article

class Author:

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        from magazine import Magazine
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({m.category for m in mags})
