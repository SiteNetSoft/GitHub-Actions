Deployers
==============

The deployers are a group of GitHub Actions that are there to help you deploy your code to various places.

Here is a list of the deployers:

* `deployer-container-registry.yml` - Deploy to a container registry
* `deployer-ftp.yml` - Deploy to an FTP server

Most of the deployers use the same pattern for when to run the GitHub actions.

For example `deployer-ftp.yml` will run when code is pushed to any branch that starts with `deploy/*` (you still have to add them manually).

.. note::

    It is different than Mirrors where the entire repository is kept in sync. The deployers only deploy what was pushed to the branch that specific to the environment you want to push it to and start with `deploy/*`.

So for production it would be `deploy/production` and for staging it would be `deploy/staging`.

But the first step is to create a release then push the code to the branch with `deploy/staging` for testing then `deploy/production` for production when ready.

Here is good step by step of the best practices for deploying with GitHub Actions:

1. Create a release from the master branch
2. Push the code to the `deploy/staging` branch
3. Test the code on the staging server
4. Push the code to the `deploy/production` branch
5. Test the code on the production server

.. note::

    Based on the GitHub Actions that are configured for the project it will deploy with FTP/SFTP or to a container registry or to any other environment.

Deployers List
--------------

* `**deployer-container-registry.yml** <.github/workflows/deployer-container-registry.yml>` - Deploy to a container registry.
* `**deployer-ftp.yml** <.github/workflows/deployer-ftp.yml>` - Deploy to an FTP/SFTP server.
* `**deployer-pypi.yml** <.github/workflows/deployer-pypi.yml>` - Deploy to `PyPI <https://pypi.org/>`__.
* `**deployer-documentation.yml** <.github/workflows/deployer-documentation.yml>` - Deploy to `Read the Docs <https://readthedocs.org/>`__ on a GitHub repo (often are `GitHub Pages <https://pages.github.com/>`__) with other document file format like ePub, and PDF and `GitHub Wiki <https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis>`__.