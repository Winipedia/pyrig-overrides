"""Test module."""

from pyrig_pypi.rig.configs.pyproject import PyprojectConfigFile


class TestPyprojectConfigFile:
    """Test class."""

    def test_make_keywords(self) -> None:
        """Test method."""
        assert "code-quality" in PyprojectConfigFile.I.make_keywords()

    def test_make_classifiers(self) -> None:
        """Test method."""
        assert (
            "Development Status :: 5 - Production/Stable"
            in PyprojectConfigFile.I.make_classifiers()
        )
