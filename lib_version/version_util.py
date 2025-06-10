# lib-version/version_util.py
import importlib

class VersionUtil:
    @staticmethod
    def get_version() -> str:
        m = importlib.import_module("lib_version.version")
        return getattr(m, "__version__", "0.0.0")

# Example usage:
if __name__ == "__main__":
    print(f"Current version: {VersionUtil.get_version()}")