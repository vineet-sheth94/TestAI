#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

# generated by datamodel-codegen:
#   filename:  AllowedHosts.yaml

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field


class AllowedHosts(BaseModel):
    class Config:
        extra = Extra.allow

    hosts: Optional[List[str]] = Field(
        None,
        description="An array of hosts that this connector can connect to.  AllowedHosts not being present for the source or destination means that access to all hosts is allowed.  An empty list here means that no network access is granted.",
    )
