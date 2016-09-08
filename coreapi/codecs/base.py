import itypes


class BaseCodec(itypes.Object):
    media_type = None
    plain_data = False

    # We don't implement stubs, to ensure that we can check which of these
    # two operations a codec supports. For example:
    # `if hasattr(codec, 'decode'): ...`

    # def decode(self, bytestring, **options):
    #    pass

    # def encode(self, document, **options):
    #    pass

    # The following will be removed at some point, most likely in a 2.1 release:
    def dump(self, *args, **kwargs):
        # Fallback for v1.x interface
        return self.encode(*args, **kwargs)

    def load(self, *args, **kwargs):
        # Fallback for v1.x interface
        return self.decode(*args, **kwargs)

    @property
    def supports(self):
        # Fallback for v1.x interface.
        if self.plain_data:
            return ['data']

        ret = []
        if hasattr(self, 'encode'):
            ret.append('encoding')
        if hasattr(self, 'decode'):
            ret.append('decoding')
        return ret
