#! /bin/bash

# Q: Why not just use Dockerfile itself?
# A: Dockerfile does not support variables, control flows, and programming in general

set -o errexit -o pipefail -o nounset

pacman -Syu --noconfirm
pacman -Fy --noconfirm

packages=(
  base
  base-devel # makepkg depends on this
  bash       # obviously already installed, but still here for completeness sake
  git        # some sources are git urls
)
pacman -S --noconfirm --needed --overwrite '*' "${packages[@]}"
