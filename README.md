# Schemas version 2.0
YAML schema, examples, and validators for OpenControl format.

## Example Project Organizations
```bash
data
├── certifications
│   ├── FedRAMP-low.yaml
│   ├── FedRAMP-med.yaml
│   └── LATO.yaml
├── components
│   └── 18F
|       ├── system.yaml
│       └── AC_Policy
│           └── component.yaml
└── standards
    └── NIST-800-53.yaml
```

## System YAML
```yaml
name: System Name
```

## Component YAML
```yaml
name: Name of the component
documentation_complete: Manual check if the documentation is complete (for gap analysis)
references:
  - name: Name of the reference ie. EC2 website
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
  - name: Name of the reference ie. EC2 website
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
verifications:
  ID_of_verification:  
    name: Name of verification
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
  EC2_Verification_2:
    name: Name of verification
    path: Relative path of local file or URL ie. diagrams/diagram-1.png
    type: Type of reference ie. Image, URL
satisfies:
  NIST-800-53:
    CM-2:
      narrative: Justification text
      implementation_status: Manual status of implementation (for gap analysis)
      references:
        - verification: The specific verification ID that the reference links, no component or system is needed for internal references
        - system: System name of the verification (can link to other systems / components)
          component: System name of the verification (can link to other systems / components)
          verification: The specific verification ID that the reference links to
```

## Standards Documentation
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

## Certifications
```yaml
# Fisma.yaml
standards:
  NIST-800-53:
    C-2:
    C-3:
  PCI:
    6:
```
