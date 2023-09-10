"""Articles management callbacks."""

from aiogram.filters.callback_data import CallbackData


class ArticlesOpenMenuCallback(CallbackData, prefix='articles/open'):
    """Callback for opening articles management menu."""


class ArticlesOpenListCallback(CallbackData, prefix='articles/list/open'):
    """Callback for opening articles list."""


class ArticlesCreateCallback(CallbackData, prefix='articles/create'):
    """Callback for creating new article."""


class ArticlesOpenArticleCallback(
    CallbackData,
    prefix='articles/list/article',
):
    """Open article menu."""

    article_id: str


class ArticlesDeleteArticleCallback(
    CallbackData,
    prefix='articles/list/article/delete',
):
    """Delete article."""

    article_id: str
