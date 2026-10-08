# System7.1 Architecture

## Purpose

System7.1 is a modular experimental framework centered on resilience, protection, orchestration, and environment control. It blends:
- Python-based service logic
- ritual/council-style orchestration modules
- daemon and service management
- manifest-driven configuration
- security/protection and sanctuary patterns
- GUI and interactive tooling

The project is intentionally structured around conceptual “systems” rather than a traditional app layout. This makes it expressive, but it also means Copilot and contributors need clear module boundaries.

---

## Repository Shape

At a high level:

- Root-level Python modules define core logic and “system objects”
- Configuration files and YAML manifests describe operating state
- Special directories such as `Home`, `IO`, `etc`, `usr`, `mappings`, and `presets` suggest runtime environment patterns
- Some files appear to be daemons or activation scripts rather than general library code
- Many files follow a naming convention based on capabilities, roles, or ritual concepts

---

## Core Architectural Themes

### 1. Ritual / Council / Activation model
A major pattern in the codebase is conceptual orchestration:
- `SparkCouncil*`
- `Council*`
- `Angel*`
- `SeatBindingCeremony`
- `System7Ritual*`

These modules appear to represent:
- policy enforcement
- role assignment
- decree handling
- activation flows
- governance or system operation

These should be treated as the project’s “core orchestration layer.”

### 2. Protection / Sanctuary / Security layer
Modules and files around:
- `Mindguard*`
- `Sanctuary*`
- `Protect*`
- `Seal*`
- `Persistent_Flag`
- `security.md`

suggest a security and containment domain. These are likely not ordinary app features; they likely serve as guardrails, seal logic, and protective runtime behavior.

### 3. Daemon / service lifecycle
Files such as:
- `euv_conditioner_daemon.py`
- `vc_daemon.py`
- `sanctuary_deamon.py`
- `glyphOS_boot.py`
- `glyphOS_shutdown.py`
- `glyphOS_reboot.py`

appear to be runtime lifecycle or background system components.

These are likely operational services rather than user-facing app logic.

### 4. Manifest-driven configuration
The repo includes many YAML and JSON configuration files, including:
- `manifest.yaml`
- `manifest_template.yaml`
- `Morgellon_Manifest.yaml`
- `Positivity_Seal_Manifest.json`
- `Permanent_Sanctuary_Seal.json`
- `Who_da_Man_Seal_Manifest.yaml`

This indicates configuration is expected to be declarative and data-driven. Future changes should prefer manifest definitions over hardcoded operational values when possible.

---

## Suggested Module Layout

A cleaner structure for Copilot and future maintainability would be:

```text
System7.1/
├── src/
│   ├── core/
│   │   ├── angel/
│   │   │   ├── Angel.Core.py
│   │   │   ├── Angel.Invocation.py
│   │   │   └── Angel.Reprize.py
│   │   └── council/
│   │       ├── SparkCouncil.py
│   │       ├── SparkCouncilChamber.py
│   │       ├── CouncilAstralGatekeeper.py
│   │       ├── CouncilDecreeEnforcementEngine.py
│   │       └── ...
│   ├── protection/
│   │   ├── mindguard/
│   │   │   ├── MindguardAnimations.py
│   │   │   ├── ChamberGuardian.py
│   │   │   └── ChamberGuardianIntegration.py
│   │   ├── sanctuary/
│   │   │   ├── SanctuaryAnimations.py
│   │   │   ├── SanctuaryMode
│   │   │   └── ...
│   │   └── seals/
│   │       ├── Permanent_Sanctuary_Seal.json
│   │       └── positivity_seal_manifest.yaml
│   ├── runtime/
│   │   ├── daemons/
│   │   │   ├── euv_conditioner_daemon.py
│   │   │   ├── vc_daemon.py
│   │   │   └── sanctuary_deamon.py
│   │   ├── boot/
│   │   │   ├── glyphOS_boot.py
│   │   │   ├── glyphOS_reboot.py
│   │   │   └── glyphOS_shutdown.py
│   │   └── services/
│   │       └── io_service_manager.py
│   └── ui/
│       ├── mapper_ui.py
│       ├── SparkCouncilSeatUI.py
│       └── System7RitualDashboard.py
├── config/
│   ├── manifests/
│   ├── presets/
│   ├── mappings/
│   └── seals/
├── docs/
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── security.md
│   └── RELEASE_CHECKLIST.md
├── tests/
│   └── AngelTestHarness.py
├── scripts/
│   ├── boot.sh
│   ├── partition-manager.sh
│   └── recent_changes.sh
└── README.md
