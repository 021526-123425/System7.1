> Replace `<org>/<repo>` and `vX.Y` with your project details.

---

### SECURITY.md

```markdown
# Security policy

## Supported versions
We maintain an LTS branch that receives critical security fixes for 18 months. Current branches:
- main: feature development
- vX.Y-lts: security and bugfixes only

## Reporting a vulnerability
Please email security@021526-123425.org with:
- A clear description and minimal repro
- Affected versions and environment
- Impact assessment

We will acknowledge within 3 business days and provide a remediation timeline. Please use responsible disclosure; do not post details publicly until a fix is released.

## Hardening practices
- 2FA required for all maintainers
- Protected default branch; signed commits and releases
- Automated SBOM (CycloneDX) published per release
- Dependabot enabled; CI runs security scanners on dependencies
