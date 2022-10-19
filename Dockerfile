FROM archlinux:base-devel

COPY pacman.conf /etc/pacman.conf
COPY init-image.bash /init-image.bash
RUN /init-image.bash

ADD https://github.com/pacman-repo-builder/pacman-repo-builder/releases/download/0.0.0-rc.62/build-pacman-repo-x86_64-unknown-linux-gnu /usr/local/bin/build-pacman-repo
RUN chmod +x /usr/local/bin/build-pacman-repo

# force makepkg to allow running as root
RUN build-pacman-repo patch-makepkg --replace

COPY run.bash /run.bash

ENTRYPOINT ["/run.bash"]
