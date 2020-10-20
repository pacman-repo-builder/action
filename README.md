# GitHub Action: Pacman Repo Builder

## Description

This action let you run [`build-pacman-repo`](https://github.com/pacman-repo-builder/pacman-repo-builder) within an Arch Linux docker container.

## Usage

### Inputs

#### `command`

_Required_.

Command to run.

### Example

```yaml
on:
  push:
    branch: master

jobs:
  build-pacman-repo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: pacman-repo-builder/action@<TAG>
        with:
          command: build-pacman-repo build --syncdeps --deref-db
```

_Note:_ Replace `<TAG>` in the above code snippet with a tag of this repository.

## Issues and Pull Requests

### Issues

Go to [pacman-repo-builder/pacman-repo-builder](https://github.com/pacman-repo-builder/pacman-repo-builder/issues).

### Pull Requests

Go to [pacman-repo-builder/pacman-repo-builder](https://github.com/pacman-repo-builder/pacman-repo-builder/pulls).

## License

[MIT](https://git.io/JTBo6) © [Hoàng Văn Khải](https://ksxgithub.github.io).
