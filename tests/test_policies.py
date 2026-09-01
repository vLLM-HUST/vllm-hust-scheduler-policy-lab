import pytest

from vllm_hust_scheduler_policy_lab import (
    NativeRecaptureScopeObserver,
    PastFuturePolicy,
    PastFutureRequestState,
    SarathiPolicy,
)


def test_past_future_is_seeded_and_host_independent() -> None:
    running = [PastFutureRequestState("running", 32, 8, 128)]
    candidate = PastFutureRequestState("candidate", 16, 0, 128)
    left = PastFuturePolicy(seed=7).decide(
        running=running, candidate=candidate, max_kv_tokens=4096
    )
    right = PastFuturePolicy(seed=7).decide(
        running=running, candidate=candidate, max_kv_tokens=4096
    )
    assert left == right
    assert left.request_id == "candidate"


def test_sarathi_validates_host_configuration() -> None:
    policy = SarathiPolicy()
    policy.validate_host_configuration(
        enable_chunked_prefill=True, max_num_scheduled_tokens=512
    )
    with pytest.raises(ValueError, match="chunked prefill"):
        policy.validate_host_configuration(
            enable_chunked_prefill=False, max_num_scheduled_tokens=512
        )


def test_observer_is_bounded_and_scope_filtered() -> None:
    observer = NativeRecaptureScopeObserver(
        enabled=True, capacity=128, request_prefix="accepted-"
    )
    observer.record(
        num_scheduled_tokens={"ignored-1": 2},
        total_num_scheduled_tokens=2,
        config_epoch=1,
        max_num_running_reqs=4,
        max_num_scheduled_tokens=512,
    )
    assert observer.state()["latest_sequence"] == 0
    observer.record(
        num_scheduled_tokens={"accepted-1": 2},
        total_num_scheduled_tokens=2,
        config_epoch=1,
        max_num_running_reqs=4,
        max_num_scheduled_tokens=512,
    )
    assert observer.state()["latest_sequence"] == 1
