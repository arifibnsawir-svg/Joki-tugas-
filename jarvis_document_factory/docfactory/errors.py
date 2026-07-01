"""Structured error types for the Document Factory.

All errors are raised before or at the boundary they protect, so a bad SPEC
never reaches a binary writer. Each error carries the fields named in the
design Error Handling table.
"""
from __future__ import annotations

from .constants import SUPPORTED_FORMATS


class DocumentFactoryError(Exception):
    """Base class for all factory errors."""


class UnsupportedFormatError(DocumentFactoryError):
    """Raised when a requested format is not one of pdf, docx, pptx.

    The message always names all three supported formats (Requirements 1.5, 12.3).
    """

    def __init__(self, token: str):
        self.token = token
        self.supported = tuple(SUPPORTED_FORMATS)
        supported = ", ".join(SUPPORTED_FORMATS)
        super().__init__(
            "unsupported format %r. Supported formats are: %s." % (token, supported)
        )


class SpecValidationError(DocumentFactoryError):
    """Raised when a required field is missing for a requested format.

    Carries the missing field name and the format that needs it (Requirement 2.4).
    """

    def __init__(self, field: str, fmt: str, detail: str = ""):
        self.field = field
        self.fmt = fmt
        self.detail = detail
        msg = "missing required field %r for format %r" % (field, fmt)
        if detail:
            msg += ": " + detail
        super().__init__(msg)


class MissingImageError(DocumentFactoryError):
    """Raised when a referenced figure path does not exist.

    Carries the unresolved figure reference and the path checked (Requirement 8.2).
    """

    def __init__(self, ref: str, path: str):
        self.ref = ref
        self.path = path
        super().__init__(
            "figure %r references a path that does not exist: %r" % (ref, path)
        )
