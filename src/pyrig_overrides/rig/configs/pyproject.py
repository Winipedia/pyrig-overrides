"""Pyrig-specific pyproject.toml configuration overrides.

Extends the base pyproject.toml configuration with PyPI classifiers and keywords
relevant to pyrig's purpose as a project scaffolding and automation toolkit.
Only active when pyrig itself is the project being configured.

The conditional class definition gates subclass registration so that
``__subclasses__()`` only discovers this class when running inside pyrig's own
repository, leaving dependent projects unaffected.
"""

from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyrig-specific pyproject.toml configuration.

    Extends the base ``PyprojectConfigFile`` with PyPI metadata specific to
    pyrig: development status, intended audience, topic classifiers, and
    project-related keywords for package discovery.

    Only defined when pyrig is the current project (via the module-level
    conditional). Projects that use pyrig as a dependency get the base class
    defaults instead.
    """

    def make_keywords(self) -> list[str]:
        """Override pyrig's method to add pyrig-specific keywords."""
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

    def make_classifiers(self) -> list[str]:
        """Override pyrig's method to add pyrig-specific classifiers."""
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
