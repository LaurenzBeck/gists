"""# 🐍📦 Python Gists Importing."""

from __future__ import annotations

import importlib.abc
import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING

from gist_import import GistImporter as Gist
from loguru import logger

if TYPE_CHECKING:
    from importlib.machinery import ModuleSpec

INIT_MODULE_DOCSTRING: str = "# 🐍📦 GitHub gists imported with the [`gists`](https://github.com/LaurenzBeck/gists) package."  # noqa: E501."
"""`gists/__init__.py` module docstring."""


class GistFinder(importlib.abc.MetaPathFinder):
    """🔎 a `MetaPathFinder`, that searches GitHub gists by their id.

    If added to `sys.meta_path`, you can import Python GitHub gists by using:
    ```python
    from gists import <gist_id>
    ```
    """

    def find_spec(  # noqa: D102
        self: str,
        _path: list[bytes | str],
        _target: ModuleType | None = None,
    ) -> ModuleSpec | None:
        if not self.startswith("gists."):
            return None

        modules = self.split(".")
        if len(modules) > 2:  # noqa: PLR2004
            logger.warning(f"🫸 cannot import sub module {self} from a gist.")
            return None

        gist_id = modules[1]

        # 🔎📂 if gist is already saved as file, return None to use the file loader
        if Path("gists/{gist_id}.py").is_file():
            return None

        return importlib.util.spec_from_loader(gist_id, GistLoader(gist_id))


class GistLoader(importlib.abc.Loader):
    """🐍📄 a `Loader` that retrieves GitHub gists by their id using its API."""

    def __init__(self, gist_id: str) -> None:  # noqa: ANN101
        """🏗️ constructs a `GistLoader`.

        Args:
            gist_id (str): GitHub gist id.
                You can retrieve this id from the GitHub url.
        """
        self.gist_id = gist_id

    def create_module(self, spec: ModuleSpec) -> ModuleType:  # noqa: D102, ANN101
        return ModuleType(spec.name)

    def exec_module(self, module: ModuleType) -> None:  # noqa: D102, ANN101
        gist_id = module.__name__
        gist = Gist(gist_id)

        code = gist.gist_codeblock
        description = gist.gist_description

        path = Path("gists")
        if not path.is_dir():
            path.mkdir(parents=True, exist_ok=True)
            with (path / "__init__.py").open("wt", encoding="utf8") as file:
                file.write(INIT_MODULE_DOCSTRING)

        # 💾 save gist to disk
        gist_path = path / f"{gist_id}.py"
        with gist_path.open("wt", encoding="utf8") as file:
            logger.info(f"💾 saving gist to {gist_path}")
            file.write(code)

        # 📝 save description to disk
        gist_path = path / f"{gist_id}.md"
        with gist_path.open("wt", encoding="utf8") as file:
            file.write(description)

        exec(code, module.__dict__)  # noqa: S102


# 📦 adapt `import` logic
sys.meta_path.insert(0, GistFinder)
