# vLLM-HUST Scheduler Policy Lab

Owner-led research carrier for runtime transitions, scheduler baseline ports, and structured-output effectiveness telemetry. It is a comparison workspace, not one deployable plugin.

**Status: source-preservation and contract-design scaffold. There is no installable runtime implementation or support claim yet.**

Technical ownership belongs to @Tkhkrnx. Source extraction must preserve exact authorship, license, tests, constraints, and evidence before activation is considered.

See [MAINTAINERS.md](MAINTAINERS.md) and [PROVENANCE.md](PROVENANCE.md).

## Extension framework

Extension ID: `org.vllm-hust.scheduler-policy-lab`

This repository follows the vLLM-HUST Extension Template. The current package
is deliberately `import_only`: it can be built, installed, discovered, and
inspected, but Extension Manager must refuse enablement until the maintainers
land a real host contract, implementation, compatibility evidence, and tests.

```bash
python -m pip install "vllm-hust-ext @ git+https://github.com/vLLM-HUST/extension-manager.git@main"
python -m pip install -e ".[test]"
vllm-hust-ext extension inspect org.vllm-hust.scheduler-policy-lab
vllm-hust-ext extension check org.vllm-hust.scheduler-policy-lab
pytest -q
```

The static Manifest 0.2 descriptor lives inside the Python distribution under
`src/`. Installation alone changes no vLLM behavior.
