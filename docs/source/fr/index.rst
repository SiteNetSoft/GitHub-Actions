GitHub Actions | SiteNetSoft
============================

GitHub Actions pour les projets de SiteNetSoft.

Utilisation des actions
-----------------------

Ajouter : ``.github/workflows/<nom>.yml``.

.. code-block:: yaml

     on: [push]
        jobs:
          <name>:
            uses: SiteNetSoft/GitHub-Actions/.github/workflows/<nom>.yml@master

.. note::

   Remplacer ``<nom>`` avec le nom de l'action.

Documentation
^^^^^^^^^^^^^

Créer l'action ``.github/workflows/documentation.yml`` :

.. code-block::

    on: [push]
    jobs:
      documentation:
        uses: SiteNetSoft/GitHub-Actions/.github/workflows/documentation.yml@master

Code Count
^^^^^^^^^^^^^

Créer l'action ``.github/workflows/code-count.yml`` :

.. code-block::

    on: [push]
    jobs:
      code-count:
        uses: SiteNetSoft/GitHub-Actions/.github/workflows/code-count.yml@master

Resources
---------

- `Hari Sekhon <https://github.com/HariSekhon/GitHub-Actions>`__ - GitHub Actions for DevOps Workflows
- `Reusing Workflows <https://docs.github.com/en/actions/using-workflows/reusing-workflows#calling-a-reusable-workflow>`__ - GitHub Docs
