from airflow import configuration
from airflow.configuration import conf
import socket


_sentinel = object()


def get_hostname(default=socket.getfqdn):
    """
    A replacement for `socket.getfqdn` that allows configuration to override it's value.

    :param callable|str default: Default if config does not specify. If a callable is given it will be called.
    """
    hostname = _sentinel
    if configuration.has_option('core', 'hostname'):
        hostname = conf.get('core', 'hostname') or _sentinel

    if hostname is _sentinel:
        hostname = callable(default) and default() or default

    return hostname
