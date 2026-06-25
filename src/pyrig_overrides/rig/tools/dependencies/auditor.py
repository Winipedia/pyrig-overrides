"""Pyrig-specific dependency auditor override."""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.dependencies.auditor import (
    DependencyAuditor as BaseDependencyAuditor,
)


class DependencyAuditor(BaseDependencyAuditor):
    """Pyrig-specific dependency auditor.

    Subclasses the base DependencyAuditor to provide an override point for
    pyrig-specific customization.
    """

    def audit_args(self, *args: str) -> Args:
        """Override pip-audit command arguments construction.

        Delegates entirely to the base class implementation.
        """
        return super().audit_args(*args)
