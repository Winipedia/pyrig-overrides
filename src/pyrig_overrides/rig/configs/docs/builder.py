"""Pyrig-specific documentation configuration overrides."""

from typing import Any

from pyrig.rig.configs.docs.builder import (
    DocsBuilderConfigFile as BaseDocsBuilderConfigFile,
)


class DocsBuilderConfigFile(BaseDocsBuilderConfigFile):
    """Pyrig-specific documentation configuration.

    Disables mkdocstrings' default member filter, which hides single-underscore
    names. pyrig's core abstractions use single-underscore methods (e.g.
    `ConfigFile._configs()`) as the primary subclassing/override surface, so
    the API reference needs to document them.
    """

    def _configs(self) -> dict[str, Any]:
        """Return the base structure with mkdocstrings' member filter disabled.

        Returns:
            The configs structure with an empty mkdocstrings `filters` list.
        """
        configs = super()._configs()
        options = configs["project"]["plugins"]["mkdocstrings"]["handlers"]["python"][
            "options"
        ]
        options["filters"] = []
        return configs
