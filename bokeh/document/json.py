#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
'''

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Literal,
    TypedDict,
    Union,
)

# External imports
from typing_extensions import TypeAlias

## Bokeh imports
if TYPE_CHECKING:
    from ..core.has_props import ModelDef
    from ..core.serialization import ModelRep, Ref
    from ..models.sources import DataDict

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = ()

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

Patch: TypeAlias = Any # TODO

Patches: TypeAlias = Dict[str, List[Patch]]

class ModelChanged(TypedDict):
    kind: Literal["ModelChanged"]
    model: Ref
    attr: str
    new: Any

class MessageSent(TypedDict):
    kind: Literal["MessageSent"]
    msg_type: str
    msg_data: Any | None

class TitleChanged(TypedDict):
    kind: Literal["TitleChanged"]
    title: str

class RootAdded(TypedDict):
    kind: Literal["RootAdded"]
    model: Ref

class RootRemoved(TypedDict):
    kind: Literal["RootRemoved"]
    model: Ref

class ColumnDataChanged(TypedDict):
    kind: Literal["ColumnDataChanged"]
    model: Ref
    attr: str
    data: DataDict
    cols: list[str] | None

class ColumnsStreamed(TypedDict):
    kind: Literal["ColumnsStreamed"]
    model: Ref
    attr: str
    data: DataDict
    rollover: int | None

class ColumnsPatched(TypedDict):
    kind: Literal["ColumnsPatched"]
    model: Ref
    attr: str
    patches: Patches

DocumentPatched: TypeAlias = Union[
    MessageSent,
    ModelChanged,
    ColumnDataChanged,
    ColumnsStreamed,
    ColumnsPatched,
    TitleChanged,
    RootAdded,
    RootRemoved,
]

DocumentChanged = DocumentPatched

class DocJson(TypedDict):
    version: str | None
    title: str | None
    defs: list[ModelDef] | None
    roots: list[ModelRep]

class PatchJson(TypedDict):
    events: list[DocumentChanged]

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
