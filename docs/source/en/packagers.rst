Packagers
==============

A set of the GitHub Actions are for packaging the application for distribution.

The usage of packages makes it easier to install the application on the target system.

Supported Packagers and Distributions
-------------------------------------

Each packager has its own YAML file in the ``.github/workflows`` directory and is named ``packager-<packager>.yml``.

Cross-platform
^^^^^^^^^^^^^

* `pip <https://pypi.org/project/pip/>`__: Python package (can also use Poetry, Pipenv, etc.)

Containers
^^^^^^^^^^

* `**Docker Hub** <https://hub.docker.com/>`__
* `**Quay.io** <https://quay.io/>`__

Linux
^^^^^

* ``deb``: `Debian <https://www.debian.org/>`__ package (also supported by Debian derived distributions like `Ubuntu <https://ubuntu.com/>`__, `Kali <https://www.kali.org/>`__, etc.)
* ``rpm``: `RedHat <https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux>`__ package (also supported by `RedHat <https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux>`__ derived distributions like `Fedora <https://fedoraproject.org/>`__, `CentOS <https://www.centos.org/>`__, `Rocky OS <https://rockylinux.org/>`__, etc.)
* ``apk``: `Alpine <https://www.alpinelinux.org/>`__ package (also supported by `Alpine <https://www.alpinelinux.org/>`__ derived distributions like `postmarketOS <https://postmarketos.org/>`__, etc.)
* ``pacman``: `Arch <https://archlinux.org/>`__ package (also supported by `Arch <https://archlinux.org/>`__ derived distributions like `Manjaro <https://manjaro.org/>`__, etc.)
* ``snap``: `Snap package <https://snapcraft.io/>`__ (also supported by `Snap <https://snapcraft.io/>`__ supported distributions like `Ubuntu <https://ubuntu.com/>`__, etc.)
* ``flatpak``: `Flatpak package <https://flatpak.org/>`__ (also supported by `Flatpak <https://flatpak.org/>`__ supported distributions like `Fedora <https://fedoraproject.org/>`__, etc.)
* ``ebuild``: `Gentoo <https://www.gentoo.org/>`__ package (also supported by `Gentoo <https://www.gentoo.org/>`__ derived distributions like `Funtoo <https://www.funtoo.org/Welcome>`__, etc.)
* ``txz, tgz``: `Slackware <http://www.slackware.com/>`__ package (also supported by `Slackware <http://www.slackware.com/>`__ derived distributions like `Salix <https://www.salixos.org/>`__, etc.)
* ``.tar.gz, .tar.bz2, .tar.xz``: Tarball (also supported by all distributions)

Mac OS X
^^^^^^^^

* `**Homebrew** <https://brew.sh/>`__: macOS package
* `**MacPorts** <https://www.macports.org/>`__: macOS package
* `**pkgbuild** <https://developer.apple.com/documentation/devtools/pkgbuild>`__: macOS package

Windows
^^^^^^^

* `**Chocolatey** <https://chocolatey.org/>`__: Windows package
* `**Scoop** <https://scoop.sh/>`__: Windows package
* `**NSIS** <https://nsis.sourceforge.io/Main_Page>`__: Windows package

Packagers List
--------------

* `**packager-apk.yml** <.github/workflows/packager-apk.yml>`__: Alpine package
* `**packager-chocolatey.yml** <.github/workflows/packager-chocolatey.yml>`__: Chocolatey package
* `**packager-deb.yml** <.github/workflows/packager-deb.yml>`__: Debian package
* `**packager-ebuild.yml** <.github/workflows/packager-ebuild.yml>`__: Ebuild image
* `**packager-flatpak.yml** <.github/workflows/packager-flatpak.yml>`__: Flatpak package
* `**packager-homebrew.yml** <.github/workflows/packager-homebrew.yml>`__: Homebrew package
* `**packager-macports.yml** <.github/workflows/packager-macports.yml>`__: MacPorts package
* `**packager-nsis.yml** <.github/workflows/packager-nsis.yml>`__: NSIS package
* `**packager-pacman.yml** <.github/workflows/packager-pacman.yml>`__: Pacman package
* `**packager-pip.yml** <.github/workflows/packager-pip.yml>`__: Pip package
* `**packager-pkgbuild.yml** <.github/workflows/packager-pkgbuild.yml>`__: Pkgbuild package
* `**packager-rpm.yml** <.github/workflows/packager-rpm.yml>`__: RPM package
* `**packager-scoop.yml** <.github/workflows/packager-scoop.yml>`__: Scoop package
* `**packager-slackware.yml** <.github/workflows/packager-slackware.yml>`__: Slackware package
* `**packager-snap.yml** <.github/workflows/packager-snap.yml>`__: Snap package
* `**packager-tarball.yml** <.github/workflows/packager-tarball.yml>`__: Tarball packages
