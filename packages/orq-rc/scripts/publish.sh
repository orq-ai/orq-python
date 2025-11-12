#!/usr/bin/env bash
export POETRY_PYPI_TOKEN_PYPI=${PYPI_TOKEN}

# Replace all symlinks pointing to .subpackages with actual files
find src -type l | while read -r symlink; do
    target=$(readlink "$symlink")
    # Check if symlink points to .subpackages
    if [[ "$target" == *".subpackages"* ]]; then
        echo "Replacing symlink: $symlink -> $target"
        rm -f "$symlink"
        cp -r "$(dirname "$symlink")/$target" "$symlink"
    fi
done

poetry run python scripts/prepare_readme.py

poetry publish --build --skip-existing
