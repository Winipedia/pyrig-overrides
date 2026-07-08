"""Pyrig-specific pyproject.toml configuration overrides.

Extends the base pyproject.toml configuration with PyPI classifiers and keywords
relevant to pyrig's purpose as a project scaffolding and automation toolkit.
"""

from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyrig-specific pyproject.toml configuration.

    Adds PyPI metadata specific to pyrig: development status, intended
    audience, topic classifiers, and project-related keywords for package
    discovery.
    """

    def make_classifiers(self) -> list[str]:
        """Return the base trove classifiers plus pyrig-specific classifiers."""
        return [
            *super().make_classifiers(),
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

    def make_keywords(self) -> list[str]:
        """Return the base keywords plus pyrig-specific discovery keywords."""
        return [
            *super().make_keywords(),
            "project-setup",
            "scaffolding",
            "boilerplate",
            "project-template",
            "automation",
            "configuration",
            "developer-tools",
            "code-quality",
            "ci-cd",
            "devops",
        ]
