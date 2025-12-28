from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtcTimeResponse")


@_attrs_define
class UtcTimeResponse:
    """Class UtcTimeResponse.

    Attributes:
        request_reception_time (datetime.datetime | Unset): Gets the UTC time when request has been received.
        response_transmission_time (datetime.datetime | Unset): Gets the UTC time when response has been sent.
    """

    request_reception_time: datetime.datetime | Unset = UNSET
    response_transmission_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        request_reception_time: str | Unset = UNSET
        if not isinstance(self.request_reception_time, Unset):
            request_reception_time = self.request_reception_time.isoformat()

        response_transmission_time: str | Unset = UNSET
        if not isinstance(self.response_transmission_time, Unset):
            response_transmission_time = self.response_transmission_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if request_reception_time is not UNSET:
            field_dict["RequestReceptionTime"] = request_reception_time
        if response_transmission_time is not UNSET:
            field_dict["ResponseTransmissionTime"] = response_transmission_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _request_reception_time = d.pop("RequestReceptionTime", UNSET)
        request_reception_time: datetime.datetime | Unset
        if isinstance(_request_reception_time, Unset):
            request_reception_time = UNSET
        else:
            request_reception_time = isoparse(_request_reception_time)

        _response_transmission_time = d.pop("ResponseTransmissionTime", UNSET)
        response_transmission_time: datetime.datetime | Unset
        if isinstance(_response_transmission_time, Unset):
            response_transmission_time = UNSET
        else:
            response_transmission_time = isoparse(_response_transmission_time)

        utc_time_response = cls(
            request_reception_time=request_reception_time,
            response_transmission_time=response_transmission_time,
        )

        return utc_time_response
