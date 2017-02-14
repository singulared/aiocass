class Cluster:
    """
    The main class to use when interacting with a Cassandra cluster.
    Typically, one instance of this class will be created for each
    separate Cassandra cluster that your application interacts with.

    Example usage::

        >>> from aiocass.cluster import Cluster
        >>>
        >>> cluster = Cluster(['192.168.1.1', '192.168.1.2'])
        >>> session = await cluster.connect()
        >>> await session.execute("CREATE KEYSPACE ...")
        >>> ...
        >>> await cluster.shutdown()

    ``Cluster`` and ``Session`` also provide async context management functions
    which implicitly handle shutdown when leaving scope.
    """

    contact_points = ['127.0.0.1']
    """
    The list of contact points to try connecting for cluster discovery.
    Defaults to loopback interface.
    """

    port = 9042
    """
    The server-side port to open connections to. Defaults to 9042.
    """

    def __init__(self, contact_points=None, port=9042):
        if contact_points is not None:
            if isinstance(contact_points, str):
                raise TypeError(
                    'contact_points should not be a string, it should be a '
                    'sequence (e.g. list) of strings')
            if None in contact_points:
                raise ValueError(
                    'contact_points should not contain None '
                    '(it can resolve to localhost)')
            self.contact_points = contact_points

        self.port = port

    async def connect(self, keyspace=None, wait_for_all_pools=False):
        """
        Coroutine that creates and return a new :class:`~.Session` object.
        If `keyspace` is specified, that keyspace will be the default
        keyspace for operations on the ``Session``.
        """
        pass
