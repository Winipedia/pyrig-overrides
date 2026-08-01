"""Pyrig-specific overrides for the pyrig CLI tool wrapper."""

from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger


class Pyrigger(BasePyrigger):
    """Pyrig-specific pyrig CLI tool wrapper.

    Excludes pyrig itself from the dev dependencies it declares, since pyrig
    is the tool managing this project rather than one of its dependencies.
    """

    def dev_dependencies(self) -> tuple[str, ...]:
        """Return the base dev dependencies with pyrig's own package name removed.

        Returns:
            The base dev dependencies, excluding `self.name()`.
        """
        dependencies = list(super().dev_dependencies())
        dependencies.remove(self.name())
        return tuple(dependencies)
