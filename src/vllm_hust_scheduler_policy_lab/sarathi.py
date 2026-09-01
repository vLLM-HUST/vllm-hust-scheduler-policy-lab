# SPDX-License-Identifier: Apache-2.0
"""Host-independent Sarathi configuration contract from legacy PR #268."""

from __future__ import annotations

from dataclasses import dataclass

SARATHI_FIXED_CHUNK_SIZE = 512


@dataclass(frozen=True)
class SarathiPolicy:
    chunk_size: int = SARATHI_FIXED_CHUNK_SIZE

    def validate_host_configuration(
        self, *, enable_chunked_prefill: bool, max_num_scheduled_tokens: int
    ) -> None:
        if not enable_chunked_prefill:
            raise ValueError("Sarathi policy requires chunked prefill")
        if max_num_scheduled_tokens != self.chunk_size:
            raise ValueError(
                f"Sarathi policy requires max scheduled tokens={self.chunk_size}"
            )

    def receipt(self) -> dict[str, object]:
        return {
            "schema": "vllm-hust.scheduler-policy.sarathi.v1",
            "scheduler_type": "sarathi",
            "chunk_size": self.chunk_size,
            "dynamic_chunking_schedule": False,
            "decode_first": True,
        }


__all__ = ["SARATHI_FIXED_CHUNK_SIZE", "SarathiPolicy"]
