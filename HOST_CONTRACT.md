# Scheduler host contract proposal

The extracted policies do not import vLLM internals. Activation requires a host
provider implementing these versioned seams:

1. `vllm.scheduler.policy.v1`: register a named policy factory without replacing
   the scheduler module.
2. `vllm.scheduler.snapshot.v1`: expose running/waiting request token counters and
   the current KV token budget to an admission policy.
3. `vllm.scheduler.lifecycle.v1`: report successful request completion so a policy
   can update bounded history.
4. `vllm.scheduler.observer.v1`: deliver immutable post-schedule receipts to an
   observer without granting it scheduler mutation rights.

The legacy subclasses in PRs #268 and #269 are compatibility references, not the
desired integration. The extension must not monkey-patch `Scheduler`, mutate a
shared production scheduler in place, or register until the host version range
and all four seams are validated.
