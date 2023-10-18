import factory
import faker
from article.models import ArticleContentTab


class ArticleContentTabFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ArticleContentTab
    
    author = factory.Faker("name")
    email = factory.Faker("email")
    organization = factory.Faker("company")
    title = factory.Faker('sentence', nb_words=5)
    content = factory.Faker("paragraph", nb_sentences = 10)