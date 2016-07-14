# Kwalify schema files

The files in the subdirectories of this folder are organized by the type of file, and then named by the version of that file's schema. These YAML files are in the [Kwalify](http://www.kuwata-lab.com/kwalify/) format—see that site for documentation.

## Validation

To validate your OpenControl files, use [the Kwalify command-line tool](http://www.kuwata-lab.com/kwalify/ruby/users-guide.05.html#ref-usage).

1. Install Kwalify (requires Ruby).

    ```bash
    gem install kwalify
    ```

1. Run the validation.

    ```
    $ kwalify -f kwalify/component/v3.0.0.yaml path/to/my/component.yaml
    path/to/my/component.yaml#0: valid.
    ```

Note there is also [a Python port](https://github.com/Grokzen/pykwalify).

For a more advanced setup, see [18F's cloud.gov compliance repository](https://github.com/18F/cg-compliance) as an example of using pykwalify as part of continuous integration.
