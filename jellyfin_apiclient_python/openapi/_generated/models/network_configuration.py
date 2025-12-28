from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkConfiguration")


@_attrs_define
class NetworkConfiguration:
    """Defines the MediaBrowser.Common.Net.NetworkConfiguration.

    Attributes:
        base_url (str | Unset): Gets or sets a value used to specify the URL prefix that your Jellyfin instance can be
            accessed at.
        enable_https (bool | Unset): Gets or sets a value indicating whether to use HTTPS.
        require_https (bool | Unset): Gets or sets a value indicating whether the server should force connections over
            HTTPS.
        certificate_path (str | Unset): Gets or sets the filesystem path of an X.509 certificate to use for SSL.
        certificate_password (str | Unset): Gets or sets the password required to access the X.509 certificate data in
            the file specified by MediaBrowser.Common.Net.NetworkConfiguration.CertificatePath.
        internal_http_port (int | Unset): Gets or sets the internal HTTP server port.
        internal_https_port (int | Unset): Gets or sets the internal HTTPS server port.
        public_http_port (int | Unset): Gets or sets the public HTTP port.
        public_https_port (int | Unset): Gets or sets the public HTTPS port.
        auto_discovery (bool | Unset): Gets or sets a value indicating whether Autodiscovery is enabled.
        enable_u_pn_p (bool | Unset): Gets or sets a value indicating whether to enable automatic port forwarding.
        enable_i_pv_4 (bool | Unset): Gets or sets a value indicating whether IPv6 is enabled.
        enable_i_pv_6 (bool | Unset): Gets or sets a value indicating whether IPv6 is enabled.
        enable_remote_access (bool | Unset): Gets or sets a value indicating whether access from outside of the LAN is
            permitted.
        local_network_subnets (list[str] | Unset): Gets or sets the subnets that are deemed to make up the LAN.
        local_network_addresses (list[str] | Unset): Gets or sets the interface addresses which Jellyfin will bind to.
            If empty, all interfaces will be used.
        known_proxies (list[str] | Unset): Gets or sets the known proxies.
        ignore_virtual_interfaces (bool | Unset): Gets or sets a value indicating whether address names that match
            MediaBrowser.Common.Net.NetworkConfiguration.VirtualInterfaceNames should be ignored for the purposes of
            binding.
        virtual_interface_names (list[str] | Unset): Gets or sets a value indicating the interface name prefixes that
            should be ignored. The list can be comma separated and values are case-insensitive. <seealso
            cref="P:MediaBrowser.Common.Net.NetworkConfiguration.IgnoreVirtualInterfaces" />.
        enable_published_server_uri_by_request (bool | Unset): Gets or sets a value indicating whether the published
            server uri is based on information in HTTP requests.
        published_server_uri_by_subnet (list[str] | Unset): Gets or sets the PublishedServerUriBySubnet
            Gets or sets PublishedServerUri to advertise for specific subnets.
        remote_ip_filter (list[str] | Unset): Gets or sets the filter for remote IP connectivity. Used in conjunction
            with <seealso cref="P:MediaBrowser.Common.Net.NetworkConfiguration.IsRemoteIPFilterBlacklist" />.
        is_remote_ip_filter_blacklist (bool | Unset): Gets or sets a value indicating whether <seealso
            cref="P:MediaBrowser.Common.Net.NetworkConfiguration.RemoteIPFilter" /> contains a blacklist or a whitelist.
            Default is a whitelist.
    """

    base_url: str | Unset = UNSET
    enable_https: bool | Unset = UNSET
    require_https: bool | Unset = UNSET
    certificate_path: str | Unset = UNSET
    certificate_password: str | Unset = UNSET
    internal_http_port: int | Unset = UNSET
    internal_https_port: int | Unset = UNSET
    public_http_port: int | Unset = UNSET
    public_https_port: int | Unset = UNSET
    auto_discovery: bool | Unset = UNSET
    enable_u_pn_p: bool | Unset = UNSET
    enable_i_pv_4: bool | Unset = UNSET
    enable_i_pv_6: bool | Unset = UNSET
    enable_remote_access: bool | Unset = UNSET
    local_network_subnets: list[str] | Unset = UNSET
    local_network_addresses: list[str] | Unset = UNSET
    known_proxies: list[str] | Unset = UNSET
    ignore_virtual_interfaces: bool | Unset = UNSET
    virtual_interface_names: list[str] | Unset = UNSET
    enable_published_server_uri_by_request: bool | Unset = UNSET
    published_server_uri_by_subnet: list[str] | Unset = UNSET
    remote_ip_filter: list[str] | Unset = UNSET
    is_remote_ip_filter_blacklist: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        enable_https = self.enable_https

        require_https = self.require_https

        certificate_path = self.certificate_path

        certificate_password = self.certificate_password

        internal_http_port = self.internal_http_port

        internal_https_port = self.internal_https_port

        public_http_port = self.public_http_port

        public_https_port = self.public_https_port

        auto_discovery = self.auto_discovery

        enable_u_pn_p = self.enable_u_pn_p

        enable_i_pv_4 = self.enable_i_pv_4

        enable_i_pv_6 = self.enable_i_pv_6

        enable_remote_access = self.enable_remote_access

        local_network_subnets: list[str] | Unset = UNSET
        if not isinstance(self.local_network_subnets, Unset):
            local_network_subnets = self.local_network_subnets

        local_network_addresses: list[str] | Unset = UNSET
        if not isinstance(self.local_network_addresses, Unset):
            local_network_addresses = self.local_network_addresses

        known_proxies: list[str] | Unset = UNSET
        if not isinstance(self.known_proxies, Unset):
            known_proxies = self.known_proxies

        ignore_virtual_interfaces = self.ignore_virtual_interfaces

        virtual_interface_names: list[str] | Unset = UNSET
        if not isinstance(self.virtual_interface_names, Unset):
            virtual_interface_names = self.virtual_interface_names

        enable_published_server_uri_by_request = (
            self.enable_published_server_uri_by_request
        )

        published_server_uri_by_subnet: list[str] | Unset = UNSET
        if not isinstance(self.published_server_uri_by_subnet, Unset):
            published_server_uri_by_subnet = self.published_server_uri_by_subnet

        remote_ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.remote_ip_filter, Unset):
            remote_ip_filter = self.remote_ip_filter

        is_remote_ip_filter_blacklist = self.is_remote_ip_filter_blacklist

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if base_url is not UNSET:
            field_dict["BaseUrl"] = base_url
        if enable_https is not UNSET:
            field_dict["EnableHttps"] = enable_https
        if require_https is not UNSET:
            field_dict["RequireHttps"] = require_https
        if certificate_path is not UNSET:
            field_dict["CertificatePath"] = certificate_path
        if certificate_password is not UNSET:
            field_dict["CertificatePassword"] = certificate_password
        if internal_http_port is not UNSET:
            field_dict["InternalHttpPort"] = internal_http_port
        if internal_https_port is not UNSET:
            field_dict["InternalHttpsPort"] = internal_https_port
        if public_http_port is not UNSET:
            field_dict["PublicHttpPort"] = public_http_port
        if public_https_port is not UNSET:
            field_dict["PublicHttpsPort"] = public_https_port
        if auto_discovery is not UNSET:
            field_dict["AutoDiscovery"] = auto_discovery
        if enable_u_pn_p is not UNSET:
            field_dict["EnableUPnP"] = enable_u_pn_p
        if enable_i_pv_4 is not UNSET:
            field_dict["EnableIPv4"] = enable_i_pv_4
        if enable_i_pv_6 is not UNSET:
            field_dict["EnableIPv6"] = enable_i_pv_6
        if enable_remote_access is not UNSET:
            field_dict["EnableRemoteAccess"] = enable_remote_access
        if local_network_subnets is not UNSET:
            field_dict["LocalNetworkSubnets"] = local_network_subnets
        if local_network_addresses is not UNSET:
            field_dict["LocalNetworkAddresses"] = local_network_addresses
        if known_proxies is not UNSET:
            field_dict["KnownProxies"] = known_proxies
        if ignore_virtual_interfaces is not UNSET:
            field_dict["IgnoreVirtualInterfaces"] = ignore_virtual_interfaces
        if virtual_interface_names is not UNSET:
            field_dict["VirtualInterfaceNames"] = virtual_interface_names
        if enable_published_server_uri_by_request is not UNSET:
            field_dict["EnablePublishedServerUriByRequest"] = (
                enable_published_server_uri_by_request
            )
        if published_server_uri_by_subnet is not UNSET:
            field_dict["PublishedServerUriBySubnet"] = published_server_uri_by_subnet
        if remote_ip_filter is not UNSET:
            field_dict["RemoteIPFilter"] = remote_ip_filter
        if is_remote_ip_filter_blacklist is not UNSET:
            field_dict["IsRemoteIPFilterBlacklist"] = is_remote_ip_filter_blacklist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("BaseUrl", UNSET)

        enable_https = d.pop("EnableHttps", UNSET)

        require_https = d.pop("RequireHttps", UNSET)

        certificate_path = d.pop("CertificatePath", UNSET)

        certificate_password = d.pop("CertificatePassword", UNSET)

        internal_http_port = d.pop("InternalHttpPort", UNSET)

        internal_https_port = d.pop("InternalHttpsPort", UNSET)

        public_http_port = d.pop("PublicHttpPort", UNSET)

        public_https_port = d.pop("PublicHttpsPort", UNSET)

        auto_discovery = d.pop("AutoDiscovery", UNSET)

        enable_u_pn_p = d.pop("EnableUPnP", UNSET)

        enable_i_pv_4 = d.pop("EnableIPv4", UNSET)

        enable_i_pv_6 = d.pop("EnableIPv6", UNSET)

        enable_remote_access = d.pop("EnableRemoteAccess", UNSET)

        local_network_subnets = cast(list[str], d.pop("LocalNetworkSubnets", UNSET))

        local_network_addresses = cast(list[str], d.pop("LocalNetworkAddresses", UNSET))

        known_proxies = cast(list[str], d.pop("KnownProxies", UNSET))

        ignore_virtual_interfaces = d.pop("IgnoreVirtualInterfaces", UNSET)

        virtual_interface_names = cast(list[str], d.pop("VirtualInterfaceNames", UNSET))

        enable_published_server_uri_by_request = d.pop(
            "EnablePublishedServerUriByRequest", UNSET
        )

        published_server_uri_by_subnet = cast(
            list[str], d.pop("PublishedServerUriBySubnet", UNSET)
        )

        remote_ip_filter = cast(list[str], d.pop("RemoteIPFilter", UNSET))

        is_remote_ip_filter_blacklist = d.pop("IsRemoteIPFilterBlacklist", UNSET)

        network_configuration = cls(
            base_url=base_url,
            enable_https=enable_https,
            require_https=require_https,
            certificate_path=certificate_path,
            certificate_password=certificate_password,
            internal_http_port=internal_http_port,
            internal_https_port=internal_https_port,
            public_http_port=public_http_port,
            public_https_port=public_https_port,
            auto_discovery=auto_discovery,
            enable_u_pn_p=enable_u_pn_p,
            enable_i_pv_4=enable_i_pv_4,
            enable_i_pv_6=enable_i_pv_6,
            enable_remote_access=enable_remote_access,
            local_network_subnets=local_network_subnets,
            local_network_addresses=local_network_addresses,
            known_proxies=known_proxies,
            ignore_virtual_interfaces=ignore_virtual_interfaces,
            virtual_interface_names=virtual_interface_names,
            enable_published_server_uri_by_request=enable_published_server_uri_by_request,
            published_server_uri_by_subnet=published_server_uri_by_subnet,
            remote_ip_filter=remote_ip_filter,
            is_remote_ip_filter_blacklist=is_remote_ip_filter_blacklist,
        )

        return network_configuration
