#!/usr/bin/env python3
import base64
import json
import zlib
from pathlib import Path

# Read the hello world kernel files
hello_world_dir = Path("examples/hello_world_py")

task_py = (hello_world_dir / "task.py").read_text()
submission_py = (hello_world_dir / "submission.py").read_text()
reference_py = (hello_world_dir / "reference.py").read_text()

# Create eval.py content
eval_py = '''from task import input_t, output_t
from submission import custom_kernel
from reference import reference_kernel

def generate_input(message: str) -> input_t:
    return message

def ref_kernel(data: input_t) -> output_t:
    return reference_kernel(data)

def check_implementation(data, output) -> str:
    expected = ref_kernel(data)
    if output != expected:
        return f'Mismatch found! Expected: {expected}, Got: {output}'
    return ''
'''

# Create utils.py content
utils_py = '''# utility functions for hello world kernel
def print_test_info(test_name: str, input_data: str):
    print(f"Running {test_name} with input: {input_data}")
'''

# Create the payload config matching the proper format
config = {
    "lang": "py",
    "main": "eval.py",
    "sources": {
        "task.py": task_py,
        "submission.py": submission_py,
        "reference.py": reference_py,
        "eval.py": eval_py,
        "utils.py": utils_py
    },
    "mode": "test",
    "tests": [
        {
            "message": "Hello Test 1"
        },
        {
            "message": "Hello Test 2"
        }
    ],
    "benchmarks": [
        {
            "message": "Hello Benchmark 1"
        },
        {
            "message": "Hello Benchmark 2"
        }
    ],
    "test_timeout": 30,
    "benchmark_timeout": 120,
    "ranked_timeout": 300,
    "ranking_by": "last",
    "seed": 42
}

# Convert to JSON string
config_json = json.dumps(config)
print("Raw config:")
print(config_json)

# Compress and encode
compressed = zlib.compress(config_json.encode("utf-8"))
encoded = base64.b64encode(compressed).decode("utf-8")

print(f"\nBase64+zlib encoded payload:")
print(encoded)

# Save to file for easy copying
Path("scripts/hello_world_payload.txt").write_text(encoded)
print(f"\nPayload saved to scripts/hello_world_payload.txt")