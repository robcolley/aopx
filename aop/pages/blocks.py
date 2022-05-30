from wagtail.core import blocks
from wagtail.images import blocks as image_blocks


class ParagraphBlock(blocks.StructBlock):
    paragraph = blocks.RichTextBlock(
        label="Paragraph",
        required=True,
        features=[
            "bold",
            "italic",
            "h2",
            "h3",
            "h4",
            "h5",
            "ol",
            "ul",
            "link",
            "document",
            "embed",
        ],
        default="",
    )

    class Meta:
        icon = "fa/object-group-solid"
        label = "Paragraph"


class ImageBlock(blocks.StructBlock):
    image = image_blocks.ImageChooserBlock(label="Image", required=True)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Image"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(label="Quote", required=True, default="")
    attribution = blocks.TextBlock(label="Attribution", required=False, default="")

    class Meta:
        icon = "fa/object-group-solid"
        label = "Quote"


class CardBlock(blocks.StructBlock):
    title = blocks.TextBlock(label="Title", required=False, default="")
    page = blocks.PageChooserBlock(label="Page", required=False, page_type=[])
    image = image_blocks.ImageChooserBlock(label="Image", required=False)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Card"
