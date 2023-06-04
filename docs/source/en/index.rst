GitHub Actions | SiteNetSoft
============================

GitHub Actions for SiteNetSoft projects.

Implemented Actions
-------------------

Create: ``.github/workflows/<name>.yml``.

.. code-block:: yaml

     on: [push]
        jobs:
          <name>:
            uses: SiteNetSoft/GitHub-Actions/.github/workflows/<name>.yml@master

.. note::

   Replace ``<name>`` with the name of the action.

Documentation
^^^^^^^^^^^^^

Create ``.github/workflows/documentation.yml`` action:

.. code-block::

    on: [push]
    jobs:
      documentation:
        uses: SiteNetSoft/GitHub-Actions/.github/workflows/documentation.yml@master

Resources
---------

- `Hari Sekhon <https://github.com/HariSekhon/GitHub-Actions>`__ - GitHub Actions for DevOps Workflows
- `Reusing Workflows <https://docs.github.com/en/actions/using-workflows/reusing-workflows#calling-a-reusable-workflow>`__ - GitHub Docs
