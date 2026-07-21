"""Optional persisted device preference (last MAC / model)."""

from medical_ble_toolkit.brands.omron.config.store import load_device_config, save_device_config

__all__ = ["load_device_config", "save_device_config"]
