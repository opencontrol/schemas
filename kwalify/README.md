# Kwalify schema files

The files in the subdirectories of this folder are organized by the type of file, and then named by the version of that file's schema. These YAML files are in the [Kwalify](http://www.kuwata-lab.com/kwalify/) format—see that site for documentation.

## Validation

To validate your OpenControl files, do the following from your project root directory:

1. Install Python (2 or 3).
1. Ignore the `schemas/` directory from version control (e.g. `.gitignore`).
1. Clone (or update) the [schemas](https://github.com/opencontrol/schemas) repository.

    ```bash
    git clone https://github.com/opencontrol/schemas.git
    # or
    cd schemas && git pull origin master && cd ..
    ```

1. Install the dependencies.

    ```bash
    pip install -r pip install -r schemas/kwalify/requirements.txt
    ```

1. Run the tests.

    ```bash
    pytest
    ```

For a more advanced setup, see [18F's cloud.gov compliance repository](https://github.com/18F/cg-compliance) as an example of using these tests as part of continuous integration.
