from abc import ABC

from monzo.authentication import Authentication
from monzo.exceptions import MonzoAuthenticationError


class Monzo(ABC):
    """
    Abstract base class all endpoints will inherit from.

    Class to provide basic functionality to all endpoints
    """
    __slots__ = ['_monzo_auth', ]

    def __init__(self, auth: Authentication):
        """
        Standard init.

        Args:
            auth: Monzo authentication object

        Raises:
            MonzoAuthenticationError: On failure to provide object with an access token
        """
        if not auth.access_token:
            raise MonzoAuthenticationError('Endpoint cannot be instantiated without a valid access token')
        self._monzo_auth = auth
