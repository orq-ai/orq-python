#!/usr/bin/env python
"""Re-apply hand-maintained patches to generated SDK code.

Speakeasy owns every file under ``src/orq_ai_sdk``, so a manual fix there is
reverted by the next ``speakeasy run``. This script is wired into
``compileCommands`` in .speakeasy/gen.yaml, ahead of the type checkers, so the
patches land on the freshly generated tree and are validated before anything
ships.

Each patch is idempotent -- an already-patched file is left alone, so this is
safe to run repeatedly and safe when some other mechanism already preserved the
edit. A patch whose anchor has disappeared is a hard error: generation fails
loudly rather than producing an SDK that silently lost the fix.
"""

import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Patch:
    """One hand-maintained change to a generated file."""

    path: str
    reason: str
    # Present in the patched file, absent in the generated one. Used to detect
    # an already-applied patch without re-running the replacements.
    marker: str
    replacements: list[tuple[str, str]] = field(default_factory=list)


PATCHES: list[Patch] = [
    Patch(
        path="src/orq_ai_sdk/utils/annotations.py",
        reason=(
            "get_discriminator must return None -- not raise -- for absent or "
            "UNSET values, so pydantic reports union_tag_not_found and a "
            "nullable discriminated union falls through to its Unset / None "
            "member. Without this, router.completions.create() raises while "
            "building the request, before any HTTP call. Covered by "
            "tests/test_nullable_discriminated_union.py."
        ),
        marker="UNSET_SENTINEL",
        replacements=[
            (
                "from enum import Enum\n"
                "from typing import Any, Optional\n"
                "\n"
                "\n"
                "def get_discriminator(model: Any, fieldname: str, key: str) -> str:\n",
                "from enum import Enum\n"
                "from typing import Any, Optional\n"
                "\n"
                "from orq_ai_sdk.types.basemodel import UNSET_SENTINEL, Unset\n"
                "\n"
                "\n"
                "def get_discriminator(model: Any, fieldname: str, key: str) -> Optional[str]:\n",
            ),
            (
                "    Returns:\n"
                "        str: The name of the discriminator attribute.\n",
                "    Returns:\n"
                "        Optional[str]: The name of the discriminator attribute, or None when the\n"
                "        value is absent or null and therefore carries no discriminator.\n",
            ),
            (
                '        ValueError: If the discriminator attribute is not found.\n'
                '    """\n'
                "    upper_fieldname = fieldname.upper()\n",
                '        ValueError: If the discriminator attribute is not found.\n'
                '    """\n'
                "    # An absent or null value carries no discriminator. Returning None makes\n"
                "    # pydantic report union_tag_not_found, which lets an optional or nullable\n"
                "    # union fall through to its Unset / None member instead of raising.\n"
                "    if model is None or isinstance(model, Unset) or model == UNSET_SENTINEL:\n"
                "        return None\n"
                "\n"
                "    upper_fieldname = fieldname.upper()\n",
            ),
        ],
    ),
]


def apply(patch: Patch) -> str:
    """Apply one patch. Returns a short status for logging."""
    target = ROOT / patch.path
    if not target.is_file():
        raise SystemExit(f"apply_patches: {patch.path} does not exist")

    source = target.read_text()
    if patch.marker in source:
        return "already applied"

    patched = source
    for old, new in patch.replacements:
        if old not in patched:
            raise SystemExit(
                f"apply_patches: {patch.path} no longer contains an anchor this "
                f"patch depends on. The generator has changed the file and the "
                f"patch must be rewritten by hand.\n\n"
                f"Why the patch exists:\n  {patch.reason}\n\n"
                f"Missing anchor:\n{old}"
            )
        patched = patched.replace(old, new, 1)

    target.write_text(patched)
    return "applied"


def main() -> int:
    for patch in PATCHES:
        print(f"apply_patches: {patch.path}: {apply(patch)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
