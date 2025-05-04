# lib-version

**Overview**
A version-aware utility library used by the `app` to log or display component versions.

#### **Features**

- Provides the current version of the library or service.
- Automated version updates via Git tags.

#### **Installation**

```python
pip install git+https://github.com/remla25-team16/lib-version@v1.0.0
```

#### **Usage**

```python
from lib_version.version_util import VersionUtil
print(VersionUtil.get_version())  # Output: "1.0.0"
```