from wagtail.core import blocks
from wagtail.images import blocks as image_blocks


class PosterBlock(blocks.StructBlock):
    poster = image_blocks.ImageChooserBlock(label="Poster", required=True)

    class Meta:
        icon = "fa/object-group-solid"
        label = "Poster"
