
import time
import resource
import os
import importlib.util
import argparse


def get_memory_usage_kb():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return usage.ru_maxrss

def measure_runtime(file_path):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", )
args = parser.parse_args()


# Start Code
initial_memory = get_memory_usage_kb()
start = time.time()

measure_runtime(args.file) # Execute Code file

# Check Time Code
print(f"Runtime: {(time.time() - start)*1000:.2f} ms", )
final_memory = get_memory_usage_kb()
print(f"Memory used: {final_memory - initial_memory} KB")