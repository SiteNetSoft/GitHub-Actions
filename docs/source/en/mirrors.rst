Mirrors
=======

Mirrors are similar to deployers, but they are used to create a mirror of a remote repository.

But compared to deployers it is not triggered by a commit to a branch that starts with `deploy/*`.

It copies the entire repository and makes sure the two repositories are in sync with all its branches.

The mirror is triggered by any push.

List of mirrors
---------------

* `**mirror-gitlab.yml** <.github/workflows/mirror-gitlab.yml>`__ - Mirrors the GitHub repository to `GitLab <https://about.gitlab.com/>`__.