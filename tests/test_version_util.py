import importlib
from lib_version.version_util import VersionUtil

def test_version_util_reads_correctly():
    assert VersionUtil.get_version() == "0.0.2"