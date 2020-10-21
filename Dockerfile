from archlinux/base

run pacman -Syu --noconfirm
run pacman -S --noconfirm --needed --overwrite '*' base base-devel bash

add https://github.com/pacman-repo-builder/pacman-repo-builder/releases/download/0.0.0-rc.26/build-pacman-repo-x86_64-unknown-linux-gnu /usr/local/bin/build-pacman-repo
run chmod +x /usr/local/bin/build-pacman-repo

# force makepkg to allow running as root
run build-pacman-repo patch-makepkg --replace

copy run.bash /run.bash

entrypoint ["/run.bash"]
