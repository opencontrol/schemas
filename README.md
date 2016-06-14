# Schemas version 2.0.0
YAML schema, examples, and validators for OpenControl format.

## Component YAML example
```yaml
name: Name of the component
key: Key of the component (optional)
references:
  - name: Name of the reference ie. EC2 website 
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
verifications:
  - key: Key of verification
    name: Name of verification
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
satisfies:
  - standard_key: Standard Key (NIST-800-53)
    control_key: Control Key (CM-2)
    narrative: Justification text
    covered_by:
      - verification_key: The specific verification key that the reference links to
        component_key: System name of the verification (required only when linking to a verification not listed in the same component) 
```

## Standards Documentation examples
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

## Certifications example
```yaml
# Fisma.yaml
standards:
  NIST-800-53:
    C-2:
    C-3:
  PCI:
    6:
```
