# lib-version/version_util.py
import pkg_resources

class VersionUtil:
    @staticmethod
    def get_version(package_name: str = "lib-version") -> str:
        return pkg_resources.get_distribution(package_name).version

# Example usage:
if __name__ == "__main__":
    print(f"Current version: {VersionUtil.get_version()}")