"""Test module."""

from pyrig.rig.tools.pyrigger import Pyrigger as PyrigPyrigger
from pyrig_runtime.core.dependencies.distribution import (
    distribution_requirement_as_module_name,
)

from pyrig_overrides.rig.configs.pyproject import PyprojectConfigFile
from pyrig_overrides.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_dev_dependencies(self) -> None:
        """Test method."""
        assert Pyrigger().dev_dependencies() == ()
        assert PyrigPyrigger().dev_dependencies() == ("pyrig",)
        assert PyrigPyrigger.I.dev_dependencies() == ()
        assert PyrigPyrigger.L is Pyrigger

        dev_dependencies = PyprojectConfigFile.I.dev_dependencies()
        dev_dependencies = tuple(
            distribution_requirement_as_module_name(dep) for dep in dev_dependencies
        )
        assert "pyrig" not in dev_dependencies
        assert "deptry" in dev_dependencies
        assert "pyrig_pypi" in dev_dependencies
