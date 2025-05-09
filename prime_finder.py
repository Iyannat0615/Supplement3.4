"""
prime_finder.py

Author: [Iyanna Thweatt]
Date: [5/8/2025]

Description:
------------
This script finds all prime numbers in a given numeric range using Python's
multiprocessing module. The number range and the number of processes to use are
specified via command-line arguments.

It splits the range evenly into N subranges and checks each number in parallel
to see if it is prime.

Performance on this machine:
-----------------------------
# Execution time on my computer:
# 1 process: 0.60 seconds
# 4 processes: 0.56 seconds


Usage:
------
    python prime_finder.py <start> <end> <num_processes>

Example:
--------
    python prime_finder.py 1 100000 4
"""

import sys
import time
from multiprocessing import Pool


def is_prime(n):
    """
    Determine whether a given number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, else False.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    """
    Generate a list of prime numbers within a given range.

    Args:
        start (int): Start of the range (inclusive).
        end (int): End of the range (exclusive).

    Returns:
        List[int]: A list of prime numbers found in the range.
    """
    return [n for n in range(start, end) if is_prime(n)]


def split_range(start, end, num_chunks):
    """
    Split a numeric range evenly into a given number of subranges.

    Args:
        start (int): Start of the full range.
        end (int): End of the full range.
        num_chunks (int): Number of chunks to divide the range into.

    Returns:
        List[Tuple[int, int]]: A list of (start, end) tuples for each subrange.
    """
    chunk_size = (end - start) // num_chunks
    ranges = []
    for i in range(num_chunks):
        chunk_start = start + i * chunk_size
        # Make sure the last chunk includes any remainder
        chunk_end = start + (i + 1) * chunk_size if i != num_chunks - 1 else end
        ranges.append((chunk_start, chunk_end))
    return ranges


def main():
    """
    Entry point of the script.
    Parses command-line arguments, runs multiprocessing, and prints results.
    """
    if len(sys.argv) != 4:
        print("Usage: python prime_finder.py <start> <end> <num_processes>")
        sys.exit(1)

    # Parse command-line arguments
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    num_processes = int(sys.argv[3])

    # Split the range for each process
    ranges = split_range(start, end, num_processes)

    # Start timer for performance measurement
    start_time = time.time()

    # Use multiprocessing to find primes in parallel
    with Pool(processes=num_processes) as pool:
        results = pool.starmap(find_primes_in_range, ranges)

    # Flatten the list of lists into one list
    all_primes = [prime for sublist in results for prime in sublist]

    end_time = time.time()

    # Display results
    print(f"Found {len(all_primes)} prime numbers.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
