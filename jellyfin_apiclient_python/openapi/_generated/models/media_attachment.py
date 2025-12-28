from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaAttachment")


@_attrs_define
class MediaAttachment:
    """Class MediaAttachment.

    Attributes:
        codec (None | str | Unset): Gets or sets the codec.
        codec_tag (None | str | Unset): Gets or sets the codec tag.
        comment (None | str | Unset): Gets or sets the comment.
        index (int | Unset): Gets or sets the index.
        file_name (None | str | Unset): Gets or sets the filename.
        mime_type (None | str | Unset): Gets or sets the MIME type.
        delivery_url (None | str | Unset): Gets or sets the delivery URL.
    """

    codec: None | str | Unset = UNSET
    codec_tag: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    index: int | Unset = UNSET
    file_name: None | str | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    delivery_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        codec: None | str | Unset
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

        codec_tag: None | str | Unset
        if isinstance(self.codec_tag, Unset):
            codec_tag = UNSET
        else:
            codec_tag = self.codec_tag

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        index = self.index

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        delivery_url: None | str | Unset
        if isinstance(self.delivery_url, Unset):
            delivery_url = UNSET
        else:
            delivery_url = self.delivery_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if codec_tag is not UNSET:
            field_dict["CodecTag"] = codec_tag
        if comment is not UNSET:
            field_dict["Comment"] = comment
        if index is not UNSET:
            field_dict["Index"] = index
        if file_name is not UNSET:
            field_dict["FileName"] = file_name
        if mime_type is not UNSET:
            field_dict["MimeType"] = mime_type
        if delivery_url is not UNSET:
            field_dict["DeliveryUrl"] = delivery_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codec = _parse_codec(d.pop("Codec", UNSET))

        def _parse_codec_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codec_tag = _parse_codec_tag(d.pop("CodecTag", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("Comment", UNSET))

        index = d.pop("Index", UNSET)

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("FileName", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("MimeType", UNSET))

        def _parse_delivery_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery_url = _parse_delivery_url(d.pop("DeliveryUrl", UNSET))

        media_attachment = cls(
            codec=codec,
            codec_tag=codec_tag,
            comment=comment,
            index=index,
            file_name=file_name,
            mime_type=mime_type,
            delivery_url=delivery_url,
        )

        return media_attachment
