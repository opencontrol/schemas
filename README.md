# Schemas

YAML schema, examples, and validators for OpenControl format. You can find the formal definitions and learn about how to do validation in the [`kwalify/`](kwalify/) folder. The examples from the Glorious (Fake) Nation of Freedonia are the complete standalone example targeted at OpenControl beginners, so we recommend looking at those first.

## Why OpenControl?

OpenControl refers to both the community, and the schemas defined in this repository. You might be wondering: why use the OpenControl format, rather than write control information in a word processor? In short, the OpenControl format is **compliance as code.** That means:

- **Version-controllable.** Since YAML is a textual format (rather than binary), it can be version controlled alongside the code, and updated simultaneously using the same workflow (like pull requests).
- **Structured > unstructured.** Because OpenControl is a structured format, the information is data, so it can be converted to various formats, and/or pulled into a dashboard.
- **Inheritable.** Copying-and-pasting control statements between documents means there isn't a canonical source of information, and to keep that information up-to-date across all your System Security Plans (SSPs). OpenControl supports inheritance, meaning the platforms, policies, and [General Support Systems (GSSs)](https://csrc.nist.gov/Glossary/Term/general-support-system) that are common across multiple information systems can have their inherited/shared control information in one place, and automatically be pulled into the documentation for all the others.

See also: [Compliance Masonry for the Compliance Literate](https://github.com/opencontrol/compliance-masonry/blob/master/docs/masonry-for-the-compliance-literate.md).

## Full project examples

* [Freedonia](https://github.com/opencontrol/freedonia-compliance#readme)
* [cloud.gov](https://github.com/18F/cg-compliance) ([GitBook](https://compliance.cloud.gov/) [rendered with Compliance Masonry](https://github.com/opencontrol/compliance-masonry#creating-gitbook-documentation)) or [alternative source](https://github.com/nsagoo-pivotal/cloud-dot-gov)
* [Environmental Protection Agency (EPA) eManifest/eRegs Notice and Comment](https://github.com/18F/epa-notice)
* [CALC](https://github.com/18F/calc)
* [Docker Enterprise Edition sample](https://github.com/docker/compliance/tree/master/examples/opencontrol/DockerEE-Moderate-ATO)

## Components

Components represent individual parts of an application or organizational policy that deal with specific security requirements. NIST refers to these as [system elements](https://csrc.nist.gov/glossary/term/system-element). For example, in the [AWS compliance documentation](https://github.com/opencontrol/aws-compliance) the [EC2](https://github.com/opencontrol/aws-compliance/blob/master/IAM/component.yaml) component deals with access control and identity management security requirements. In the [Cloud Foundry compliance documentation](https://github.com/opencontrol/cf-compliance), the [UAA](https://github.com/opencontrol/cf-compliance/blob/master/UAA/component.yaml) the [Cloud Controller](https://github.com/opencontrol/cf-compliance/tree/master/CloudController) components deal with those requirements. In a straightforward Django-based application, for example, Django would be the component that deals with access control and identity management. As a developer building an SSP you most likely only deal with the component documentation.

### Examples

* [Amazon Web Services (AWS)](https://github.com/opencontrol/aws-compliance)
    * [The (simplified) Freedonia version](https://github.com/opencontrol/freedonia-aws-compliance)
* [Cloud Foundry](https://github.com/opencontrol/cf-compliance)
* [Docker Enterprise Edition](https://github.com/docker/compliance)
* [Red Hat](https://github.com/ComplianceAsCode/redhat)

### Structure

```yaml
name: Name of the component
key: Key of the component (defaults to the filename if not present)
documentation_complete: Manual check if the documentation is complete (for gap analysis)
schema_version: 3.0.0
references:
  - name: Name of the reference ie. EC2 website
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
  - name: Name of the reference ie. EC2 website
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
verifications:
  - key: Key of verification
    name: Name of verification
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
  - key: Key of verification
    name: Name of verification
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
satisfies:
  - standard_key: Standard Key (NIST-800-53)
    control_key: Control Key (CM-2)
    narrative:
      - key: The optional key that represents a particular section of the control. If the key is not specified, assume the string in the following text represents the entire control
        text: The narrative text for the particular section / entire control if there is no key specified
    implementation_statuses:
      - Used for gap analysis, can only be one of the following:
      - partial
      - planned
      - complete
      - none
    control_origins:
      - shared
      - inherited
      - Other text representing the control origination.
    parameters:
     - key: "The key for a particular parameter of the specific control"
       text: "The parameter text for a particular parameter of a specific control"
    covered_by:
      - verification_key: The specific verification ID that the reference links, no component or system is needed for internal references
      - system_key: System name of the verification (can link to other systems / components)
        component_key: System name of the verification (can link to other systems / components)
        verification_key: The specific verification ID that the reference links to
```

### Validation

```bash
kwalify -f kwalify/component/v3.0.0.yaml examples/component_v3.0.0.yaml
# OR
pykwalify -s kwalify/component/v3.0.0.yaml -d examples/component_v3.0.0.yaml
```

## Standards

A standard is a list composed of individual security requirements called controls.

### Examples

```yaml
# nist-800-53.yaml
standards:
  C-2:
    name: User Access
    description: There is an affordance for managing access by...

# PCI.yaml
standards:
  Regulation-6:
    name: User Access PCI
    description: There is an affordance for managing access by...
```

#### See also

* [Freedonia FRIST](https://github.com/opencontrol/freedonia-frist)
* [National Institute of Standards and Technology (NIST) 800-53](https://github.com/opencontrol/NIST-800-53-Standards)
* [Payment Card Industry Data Security Standard (PCI DSS)](https://github.com/opencontrol/PCI-DSS-Certifications)

## Certifications

Since standards can have thousands of security requirements (aka controls), agencies like the [GSA](http://www.gsa.gov/) or organizations such as [FedRAMP](https://www.fedramp.gov) have curated a list of controls they require in order grant an IT system Authority to Operate (ATO). These are also known as "baselines". The GSA, for example, developed a baseline called [the Lightweight ATO (LATO)](https://gsablogs.gsa.gov/innovation/2014/12/10/it-security-security-in-an-agile-development-cloud-world-by-kurt-garbars/), which uses only 24 controls.

### Example

```yaml
# Fisma.yaml
standards:
  NIST-800-53:
    C-2:
    C-3:
  PCI:
    6:
```

#### See also

* [Freedonia FRIST](https://github.com/opencontrol/freedonia-frist)
* [General Services Administration (GSA) certifications](https://github.com/18F/GSA-Certifications)

## Systems

The `opencontrol.yaml` file defines an application's documentation configuration settings.

### Structure

```yaml
schema_version: "1.0.0" # 1.0.0 is the current opencontrol.yaml schema version
name: Project_Name # Name of the project
metadata:
  description: "A description of the system"
  maintainers:
    - maintainer_email@email.com
components: # A list of paths to components written in the opencontrol format for more information view: https://github.com/opencontrol/schemas
  - ./component-1
certifications: # An optional list of certifications for more information visit: https://github.com/opencontrol/schemas
  - ./cert-1.yaml
standards: # An optional list of standards for more information visit: https://github.com/opencontrol/schemas
  - ./standard-1.yaml
dependencies:
  certifications: # An optional list of certifications stored remotely
    - url: https://github.com/18F/GSA-Certifications
      revision: master
  systems:  # An optional list of repos that contain an opencontrol.yaml stored remotely
    - url: https://github.com/18F/cg-compliance
      revision: master
  standards:   # An optional list of remote repos containing standards info that contain an opencontrol.yaml
    - url: https://github.com/opencontrol/NIST-800-53-Standards
      revision: master
```

For version control systems, a option key `contextdir` can be specified to handle multiple opencontrol content directories in a single repository.
For example:

```
dependencies:
    - url: https://github.com/organization/repository
      contextdir: subdirectory_in_repository
      revision: branch
```

### Validation

```bash
kwalify -f kwalify/opencontrol/v1.0.0.yaml examples/opencontrol_v1.0.0.yaml
# OR
pykwalify -s kwalify/opencontrol/v1.0.0.yaml -d examples/opencontrol_v1.0.0.yaml
```

## Relationship to other formats

### OSCAL

[OSCAL](https://pages.nist.gov/OSCAL/) is a schema being developed by the U.S. [National Institute of Standards & Technology (NIST)](https://www.nist.gov/). It is meant to express control information in a precise way, and can be thought of as a more detailed version of [the OpenControl schemas](https://github.com/opencontrol/schemas). Where OSCAL's focus is precision, the OpenControl schema's focus is on usability.

The mapping:

| OSCAL                                                            | OpenControl                      |
| ---------------------------------------------------------------- | -------------------------------- |
| [Catalog](https://pages.nist.gov/OSCAL/concepts/#oscal-catalogs) | [Standard](#standards)           |
| [Profile](https://pages.nist.gov/OSCAL/concepts/#oscal-profiles) | [Certification](#certifications) |
| [Implementation](https://pages.nist.gov/OSCAL/roadmap/)          | [Component](#components)         |

The two communities have a good relationship, and there is a lot of overlap in terms of participants.
