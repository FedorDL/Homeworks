# Самостоятельно познакомиться с паттернами Factory (фабрика) и Factory method (фабричный метод) и решить следующую задачу:
# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег
# (например: <tag></tag>). От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
# а через фабричный метод или фабрику, например factory.create_tag(name).»


class TagFactory:

    def create_tag(self, name):
        pass

    def get_html(self):
        return self.create_tag()

class Image(TagFactory):

    def create_tag(self, name):
        if name == 'image':
            return "<img>"


class Input(TagFactory):

    def create_tag(self, name):
        if name == 'input':
            return "<input></input>"


class Text(TagFactory):

    def create_tag(self, name):
        if name == 'p':
            return "<p></p>"

class Link(TagFactory):

    def create_tag(self, name):
        if name == 'a':
            return "<a></a>"

# class HTML:
#
#     def get_html(self, name):
#         if name == 'image':
#             return Image()
#         elif name == 'input':
#             return Input()
#         elif name == 'p':
#             return Text()
#         elif name == 'a':
#             return Link()


factory = TagFactory()
elements = ['image', 'input', 'p', 'a']
for el in elements:
    print(factory.get_html())

