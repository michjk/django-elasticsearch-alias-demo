from typing import Any
from django.core.management.base import BaseCommand, CommandParser

from article.factory import ArticleContentTabFactory

class Command(BaseCommand):
    help = "Populate test article content"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--size", type=int, default=1000000)
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        size = options["size"]
        for i in range(size):
            ArticleContentTabFactory.create()

