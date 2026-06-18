"""Pyrig-specific override of the HealthCheckWorkflowConfigFile."""

from typing import Any

from pyrig.rig.tools.version_control.remote import RemoteVersionController
from pyrig_codecov.rig.configs.remote_version_control.workflows.health_check import (
    HealthCheckWorkflowConfigFile as BaseHealthCheckWorkflowConfigFile,
)


class HealthCheckWorkflowConfigFile(BaseHealthCheckWorkflowConfigFile):
    """Pyrig-specific override of the health check workflow config file."""

    def step_run_tests(self, *, step: dict[str, Any] | None = None) -> dict[str, Any]:
        """Pyrig-specific override of the test step.

        Adds the repository access token to the environment variables of
        the test step, to allow pyrig's test suite to test API calls that
        require authentication.
        """
        if step is None:
            step = {}
        step["env"] = {
            RemoteVersionController.I.access_token_key(): self.insert_repo_token()
        }
        return super().step_run_tests(step=step)
