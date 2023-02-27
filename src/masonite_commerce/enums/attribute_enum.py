from enum import Enum


class AttributeStatus(Enum):
    DRAFT = "draft" # in edit mode
    PUBLISHED = "published" # visible on site
    ARCHIVED = "archived" # not visible on site
