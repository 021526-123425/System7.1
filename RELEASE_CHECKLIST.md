# Release checklist

1. Update CHANGELOG.md and version in pyproject.toml (or setup.cfg)
2. Run full CI matrix (Linux/macOS/Windows; Python versions)
3. Build wheels and sdist; verify hashes
4. Generate SBOM (CycloneDX) and attach to release
5. Tag and sign: `git tag -s vX.Y.Z && git push --tags`
6. Publish to PyPI/conda (and GHCR for containers)
7. Create Zenodo DOI; upload artifacts (sdist, wheels, docs zip)
8. Submit snapshot to Software Heritage; upload to Internet Archive
9. Update README “Resilience and mirrors” with links
10. Announce with release notes and citation