# lib-version

**Overview**
A version-aware utility library used by the `app` to log or display component versions. The personal contribution can be seen from `ACTIVITY.md`.  

#### **Features**

- Provides the current version of the library or service.
- Automated version updates via Git tags.

#### **Installation**

```python
pip install git+https://github.com/remla2025-team16/lib-version@v0.0.8
```

#### **Usage**

```python
from lib_version.version_util import VersionUtil
print(VersionUtil.get_version())
```
