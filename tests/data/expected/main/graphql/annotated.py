# generated by datamodel-codegen:
#   filename:  annotated.graphql
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional, TypeAlias

from pydantic import BaseModel, Field
from typing_extensions import Annotated, Literal

Boolean: TypeAlias = bool
"""
The `Boolean` scalar type represents `true` or `false`.
"""


String: TypeAlias = str
"""
The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.
"""


class A(BaseModel):
    field: String
    listField: List[String]
    listListField: List[List[String]]
    typename__: Annotated[Optional[Literal['A']], Field(alias='__typename')] = 'A'
