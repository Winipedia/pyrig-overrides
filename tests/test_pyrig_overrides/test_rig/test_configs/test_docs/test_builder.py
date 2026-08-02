"""Test module."""

from pyrig_overrides.rig.configs.docs.builder import DocsBuilderConfigFile


class TestDocsBuilderConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        configs = DocsBuilderConfigFile.I.configs()
        options = configs["project"]["plugins"]["mkdocstrings"]["handlers"]["python"][
            "options"
        ]
        assert options["filters"] == []
