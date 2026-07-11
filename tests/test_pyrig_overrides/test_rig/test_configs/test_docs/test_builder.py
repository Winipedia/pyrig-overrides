"""Test module."""

from pyrig_overrides.rig.configs.docs.builder import DocsBuilderConfigFile


class TestDocsBuilderConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        configs = DocsBuilderConfigFile.I.configs()
        mkdocstrings_plugin = next(
            plugin
            for plugin in configs["plugins"]
            if isinstance(plugin, dict) and "mkdocstrings" in plugin
        )
        options = mkdocstrings_plugin["mkdocstrings"]["handlers"]["python"]["options"]
        assert options["filters"] == []
