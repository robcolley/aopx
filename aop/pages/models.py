from datetime import date

from django.db import models
from django.utils import timezone
from wagtail import images
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images import edit_handlers as image_edit_handlers
from wagtail.search import index

from aop.pages import blocks as pages_blocks


class HomePage(Page):
    heading = models.TextField(verbose_name="Heading", blank=True, default="Heading")
    hero_image = models.ForeignKey(
        to=images.get_image_model_string(),
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero image",
        blank=True,
        null=True,
    )
    gallery = StreamField(
        block_types=[("card", pages_blocks.CardBlock())],
        verbose_name="Gallery",
        blank=True,
    )

    hero_panels = [
        FieldPanel("heading"),
        image_edit_handlers.ImageChooserPanel("hero_image"),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel(heading="Hero", children=hero_panels),
        StreamFieldPanel("gallery"),
    ]

    subpage_types = [
        "pages.HomePage",
        "pages.NewsPage",
    ]
    parent_page_types = [
        "wagtailcore.Page",
        "pages.HomePage",
        "pages.NewsPage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Homepage"


class NewsPage(Page):

    parent_page_types = [
        "pages.HomePage",
        "pages.NewsPage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "News"


class NewsItemPage(Page):
    body = StreamField(
        block_types=[
            ("paragraph", pages_blocks.ParagraphBlock()),
            ("image", pages_blocks.ImageBlock()),
            ("quote", pages_blocks.QuoteBlock()),
        ],
        verbose_name="Body",
    )
    publish_date = models.DateField(verbose_name="Publish date", default=timezone.now)

    content_panels = Page.content_panels + [
        FieldPanel("publish_date"),
        StreamFieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.FilterField("body"),
        index.FilterField("publish_date"),
    ]

    subpage_types = []
    parent_page_types = [
        "pages.NewsPage",
    ]

    preview_modes = []

    class Meta:
        verbose_name = "News item"
