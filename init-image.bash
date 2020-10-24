#! /bin/bash
set -o errexit -o pipefail -o nounset

packages=(
  base
  base-devel # makepkg depends on this
  bash       # obviously already installed, but still here for completeness sake
  git        # some sources are git urls
)
pacman -S --noconfirm --needed --overwrite '*' "${packages[@]}"
