"""Pyrig-specific dependency auditor override."""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.dependencies.auditor import (
    DependencyAuditor as BaseDependencyAuditor,
)


class DependencyAuditor(BaseDependencyAuditor):
    """Extension point for applying pyrig-specific `pip-audit` customization."""

    def check_args(self, *args: str) -> Args:
        """Overrides the base to adjust the arguments passed to `pip-audit`."""
        return super().check_args(*args)
