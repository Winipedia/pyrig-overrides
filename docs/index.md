# Home

<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-overrides/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-overrides/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-overrides/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-overrides/actions/workflows/deploy.yml)
<!-- testing -->
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-overrides/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-overrides)
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
<!-- code-quality -->
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-overrides?style=social)](https://github.com/Winipedia/pyrig-overrides)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://Winipedia.github.io/pyrig-overrides)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-overrides?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-overrides)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-overrides)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-overrides)](https://github.com/Winipedia/pyrig-overrides/blob/main/LICENSE)

---

> A simple package that contains overrides for pyrig.

---

## Overview

pyrig-overrides carries the project overrides applied to
[pyrig](https://github.com/Winipedia/pyrig)'s own repository. It is a maintenance
package for pyrig itself — not a general-purpose plugin — added as a development
dependency to the pyrig project.

## Installation

```bash
uv add pyrig-overrides --dev
uv run pyrig sync
```

## How it works

The package overrides three pyrig classes:

- **Project metadata** — extends the generated `pyproject.toml` with
  pyrig-specific PyPI trove classifiers and discovery keywords.
- **Dependency audit** — an extension point for adjusting the arguments passed
  to `pip-audit`.
- **Docs config** — disables mkdocstrings' default member filter in the
  generated `mkdocs.yml`, so pyrig's single-underscore override methods are
  documented in the API reference.

## API Reference

For class- and method-level details, see the [API Reference](api.md), generated
automatically from the source.
