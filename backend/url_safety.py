"""Network safety helpers for user- or document-provided URLs."""

from __future__ import annotations

import ipaddress
import socket
from urllib.parse import urlparse


class UnsafeUrlError(ValueError):
    """Raised when a URL targets a disallowed scheme or network location."""


def validate_public_http_url(url: str) -> str:
    """Return *url* if it is HTTP(S) and does not resolve to private/internal IPs."""
    parsed = urlparse(str(url or "").strip())
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise UnsafeUrlError(f"URL must be http(s): {url!r}")

    hostname = parsed.hostname
    try:
        ip = ipaddress.ip_address(hostname)
        _reject_private_ip(ip, url)
        return url
    except ValueError:
        pass

    try:
        infos = socket.getaddrinfo(
            hostname, parsed.port or _default_port(parsed.scheme), type=socket.SOCK_STREAM
        )
    except socket.gaierror as exc:
        raise UnsafeUrlError(f"Could not resolve URL host {hostname!r}") from exc

    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        _reject_private_ip(ip, url)
    return url


def _default_port(scheme: str) -> int:
    return 443 if scheme == "https" else 80


def _reject_private_ip(ip: ipaddress._BaseAddress, url: str) -> None:
    if (
        ip.is_private
        or ip.is_loopback
        or ip.is_link_local
        or ip.is_multicast
        or ip.is_reserved
        or ip.is_unspecified
    ):
        raise UnsafeUrlError(f"URL resolves to a non-public IP ({ip}): {url!r}")
