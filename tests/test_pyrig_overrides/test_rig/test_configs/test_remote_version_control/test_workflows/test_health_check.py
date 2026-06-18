"""Test module."""

from pyrig.rig.configs.remote_version_control.workflows.health_check import (
    HealthCheckWorkflowConfigFile,
)


class TestHealthCheckWorkflowConfigFile:
    """Test class."""

    def test_step_run_tests(self) -> None:
        """Test method."""
        assert "env" in HealthCheckWorkflowConfigFile.I.step_run_tests()
        assert "env" in HealthCheckWorkflowConfigFile.I.step_run_tests(step={})
