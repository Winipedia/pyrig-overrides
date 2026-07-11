"""Pyrig-specific `mkdocs.yml` configuration overrides."""

from typing import Any

from pyrig.rig.configs.docs.builder import (
    DocsBuilderConfigFile as BaseDocsBuilderConfigFile,
)


class DocsBuilderConfigFile(BaseDocsBuilderConfigFile):
    """Pyrig-specific `mkdocs.yml` configuration.

    Disables mkdocstrings' default member filter, which hides single-underscore
    names. pyrig's core abstractions use single-underscore methods (e.g.
    `ConfigFile._configs()`) as the primary subclassing/override surface, so
    the API reference needs to document them.
    """

    def _configs(self) -> dict[str, Any]:
        """Return the base structure with mkdocstrings' member filter disabled.

        Returns:
            The base `mkdocs.yml` structure with an empty mkdocstrings
            `filters` list.
        """
        configs = super()._configs()
        mkdocstrings_plugin = next(
            plugin
            for plugin in configs["plugins"]
            if isinstance(plugin, dict) and "mkdocstrings" in plugin
        )
        options = mkdocstrings_plugin["mkdocstrings"]["handlers"]["python"]["options"]
        options["filters"] = []
        return configs
