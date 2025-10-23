# Number of Recent Calls
# Topic: Queue
# Type: Home Challenge

from collections import deque
from typing import List, Tuple

class RecentCounter:
    def __init__(self):
        """Initialize RecentCounter with an empty queue"""
        self.requests = deque()  # Queue to store timestamps
        self.window = 3000      # Sliding window size in milliseconds

    def ping(self, t: int) -> int:
        """
        Add new request at time t and return count of requests in last 3000ms
        Time Complexity: O(k) where k is number of outdated requests to remove
        Space Complexity: O(n) where n is number of requests in window
        """
        # Add current request
        self.requests.append(t)
        
        # Remove requests older than t - 3000
        while self.requests and self.requests[0] < t - self.window:
            self.requests.popleft()
            
        # Return count of requests in current window
        return len(self.requests)

def run_test_case(operations: List[str], timestamps: List[List[int]]) -> List[int]:
    """Helper function to run test cases"""
    counter = None
    results = []
    
    for op, t in zip(operations, timestamps):
        if op == "RecentCounter":
            counter = RecentCounter()
            results.append(None)
        elif op == "ping":
            results.append(counter.ping(t[0]))
            
    return [r for r in results if r is not None]

def visualize_window(timestamps: List[int], current_time: int, window_size: int = 3000) -> str:
    """Helper function to visualize the sliding window"""
    if not timestamps:
        return "Empty timeline"
        
    # Calculate timeline bounds
    start = min(timestamps)
    end = max(timestamps)
    
    # Create timeline visualization
    timeline = ["Timeline:"]
    timeline.append("-" * 50)
    
    # Calculate scale factor
    total_span = end - start
    scale = 40 / total_span if total_span > 0 else 1
    
    # Add timestamps to timeline
    for t in timestamps:
        pos = int((t - start) * scale)
        line = " " * pos + "•"
        timeline.append(f"{line:<41} {t}ms")
    
    # Add window visualization
    window_start = current_time - window_size
    window_start_pos = int((max(window_start, start) - start) * scale)
    window_end_pos = int((current_time - start) * scale)
    
    window_line = " " * window_start_pos + "["
    window_line += "-" * max(0, window_end_pos - window_start_pos)
    window_line += "]"
    
    timeline.append("-" * 50)
    timeline.append(f"{window_line:<41} Window: [{window_start}-{current_time}]")
    
    return "\n".join(timeline)

# Demo
if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Test case 1: Basic example from problem
        (["RecentCounter", "ping", "ping", "ping", "ping"],
         [[], [1], [100], [3001], [3002]]),
        
        # Test case 2: Requests far apart
        (["RecentCounter", "ping", "ping", "ping"],
         [[], [5000], [8000], [11000]]),
        
        # Test case 3: Requests at window boundary
        (["RecentCounter", "ping", "ping", "ping", "ping"],
         [[], [3000], [3002], [6000], [6001]]),
        
        # Test case 4: Regular intervals
        (["RecentCounter", "ping", "ping", "ping", "ping"],
         [[], [10], [3010], [6010], [9000]]),
        
        # Test case 5: Rapid requests
        (["RecentCounter", "ping", "ping", "ping", "ping", "ping"],
         [[], [1], [2], [3], [4], [3002]])
    ]
    
    for i, (operations, timestamps) in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print("Operations:", operations)
        print("Timestamps:", timestamps)
        
        results = run_test_case(operations, timestamps)
        print("\nResults:", results)
        
        # Visualize final state
        if timestamps and timestamps[-1]:
            final_timestamps = [t[0] for t in timestamps[1:]]  # Skip empty list for RecentCounter
            print("\nFinal state visualization:")
            print(visualize_window(final_timestamps, final_timestamps[-1]))
        print("\n" + "="*50)
