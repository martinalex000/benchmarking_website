"""Unit tests for URL safety helpers."""

import socket

import pytest

from backend.url_safety import UnsafeUrlError, validate_public_http_url


def test_validate_public_http_url_rejects_private_ip():
    with pytest.raises(UnsafeUrlError):
        validate_public_http_url("http://127.0.0.1/private.pdf")


def test_validate_public_http_url_rejects_non_http_scheme():
    with pytest.raises(UnsafeUrlError):
        validate_public_http_url("file:///etc/passwd")


def test_validate_public_http_url_rejects_hostname_resolving_to_private_ip(monkeypatch):
    def fake_getaddrinfo(*args, **kwargs):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("10.0.0.1", 80))]

    monkeypatch.setattr(socket, "getaddrinfo", fake_getaddrinfo)

    with pytest.raises(UnsafeUrlError):
        validate_public_http_url("https://example.com/file.pdf")
