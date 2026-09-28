"""Pyrig-specific `pyproject.toml` configuration overrides.

Extends the base `pyproject.toml` configuration with PyPI classifiers and
keywords relevant to pyrig's purpose as a project scaffolding and automation
toolkit.
"""

from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyrig-specific `pyproject.toml` configuration.

    Adds PyPI trove classifiers and keywords specific to pyrig on top of the
    base configuration.
    """

    def classifiers_configs(self) -> list[str]:
        """Return the base trove classifiers plus pyrig-specific classifiers."""
        return [
            *super().classifiers_configs(),
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Software Development :: Code Generators",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Quality Assurance",
            "Topic :: Software Development :: Testing",
            "Topic :: System :: Software Distribution",
            "Topic :: System :: Installation/Setup",
        ]

    def keywords_configs(self) -> list[str]:
        """Return the base keywords plus pyrig-specific discovery keywords."""
        return [
            *super().keywords_configs(),
            "automation",
            "boilerplate",
            "ci-cd",
            "code-generation",
            "code-quality",
            "configuration",
            "convention-over-configuration",
            "developer-tools",
            "devops",
            "github-actions",
            "project-generator",
            "project-maintenance",
            "project-scaffolding",
            "project-setup",
            "pyrig-runtime",
            "python-project",
            "test-generation",
            "test-scaffolding",
        ]
