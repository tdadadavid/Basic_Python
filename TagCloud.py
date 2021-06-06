class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getItem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setItem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


tag = TagCloud()
tag.add("JavaScript")
tag.add("JavaScript")
tag.add("JavaScript")
tag.add("Python")
tag.add("Java")
len(tag)
print(tag.tags)
