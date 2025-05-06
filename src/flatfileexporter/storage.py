import json
import os
from pathlib import Path
import appdirs


class AppConfig:
    def __init__(self, app_name):
        self.app_name = app_name
        self.config_dir = Path(appdirs.user_config_dir(app_name))
        self.config_file = self.config_dir / "config.json"
        self._config = {}

        # Create config directory if it doesn't exist
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # Load existing config
        self.load()

    def load(self):
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, "r") as f:
                    self._config = json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            self._config = {}

    def save(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self._config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")

    def get(self, key, default=None):
        """Get a config value"""
        return self._config.get(key, default)

    def set(self, key, value):
        """Set a config value"""
        self._config[key] = value
        self.save()

    def delete(self, key):
        """Delete a config value"""
        if key in self._config:
            del self._config[key]
            self.save()
