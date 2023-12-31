from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import ArticleContentTab
from elasticsearch_dsl import analysis

ngram_tokenizer = analysis.token_filter("edge_ngram_filter", type="edge_ngram", min_gram=2, max_gram=3)
ngram_analyzer = analysis.analyzer("edge_ngram_analyzer", tokenizer="standard", filter=["lowercase", ngram_tokenizer])

@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'article_content_idx'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = ArticleContentTab # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            "id",
            'title',
            'content',
            "created_at"
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Configure how the index should be refreshed after an update.
        # See Elasticsearch documentation for supported options:
        # https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-refresh.html
        # This per-Document setting overrides settings.ELASTICSEARCH_DSL_AUTO_REFRESH.
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000
    
    author = fields.TextField(analyzer=ngram_analyzer)