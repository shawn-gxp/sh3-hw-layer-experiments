"""
Active brand plugin registrations. Import a brand module here to activate it
— this is the ONE file touched when adding a new brand.
"""
from .omron import plugin as _omron_plugin  # noqa: F401

# Future:
# from .nipro import plugin as _nipro_plugin
# from .beurer import plugin as _beurer_plugin
# from .fora import plugin as _fora_plugin
