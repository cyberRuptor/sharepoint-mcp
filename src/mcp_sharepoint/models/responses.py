"""Pydantic response models for all MCP tool return values.

Using typed models instead of raw dicts gives:
- Auto-validation of return shapes
- IDE auto-complete in consumers
- Clean JSON serialisation via .model_dump()
"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Shared primitives
# ---------------------------------------------------------------------------

class FolderEntry(BaseModel):
    name: str
    url: str | None = None
    created: str | None = None
    modified: str | None = None


class FileEntry(BaseModel):
    name: str
    url: str | None = None
    size: int | None = None
    created: str | None = None
    modified: str | None = None


class TreeNode(BaseModel):
    name: str
    path: str | None = None
    type: str  # "folder" | "file"
    created: str | None = None
    modified: str | None = None
    size: int | None = None
    children: list[TreeNode] = Field(default_factory=list)
    error: str | None = None


TreeNode.model_rebuild()  # required for self-referential model


# ---------------------------------------------------------------------------
# Operation responses
# ---------------------------------------------------------------------------

class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    file: dict[str, str] | None = None
    folder: dict[str, str] | None = None
    method: str | None = None
    path: str | None = None
    size: int | None = None
    primary_error: str | None = None


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    detail: str | None = None


# ---------------------------------------------------------------------------
# Content responses
# ---------------------------------------------------------------------------

class DocumentContent(BaseModel):
    name: str
    content_type: str                    # "text" | "binary"
    content: str | None = None        # for text files
    content_base64: str | None = None # for binary files
    original_type: str | None = None  # "pdf" | "excel" | "word"
    size: int
    page_count: int | None = None
    sheet_count: int | None = None
    paragraph_count: int | None = None


class MetadataResponse(BaseModel):
    success: bool = True
    message: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    file: dict[str, str] | None = None
