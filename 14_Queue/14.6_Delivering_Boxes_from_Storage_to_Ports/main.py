# Delivering Boxes from Storage to Ports
# Topic: Queue
# Type: Home Challenge

from typing import List, Tuple
from collections import deque

def boxDelivering(boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
    """
    Calculate minimum number of trips needed to deliver boxes
    Time Complexity: O(n) where n is number of boxes
    Space Complexity: O(n)
    """
    if not boxes:
        return 0
        
    n = len(boxes)
    # dp[i] represents minimum trips needed to deliver boxes[0:i]
    dp = [0] * (n + 1)
    
    # prefix sums for weights and port changes
    weights = [0]  # prefix sum of weights
    changes = [0]  # prefix sum of port changes
    
    # Calculate prefix sums
    for i in range(n):
        weights.append(weights[-1] + boxes[i][1])
        changes.append(changes[-1] + (i > 0 and boxes[i][0] != boxes[i-1][0]))
    
    # Initialize deque for sliding window
    dq = deque([0])
    
    # Process each ending position
    for i in range(1, n + 1):
        # Remove positions that exceed maxBoxes or maxWeight
        while dq and i - dq[0] > maxBoxes:
            dq.popleft()
        while dq and weights[i] - weights[dq[0]] > maxWeight:
            dq.popleft()
            
        if dq:
            # Calculate minimum trips needed ending at position i
            dp[i] = dp[dq[0]] + changes[i] - changes[dq[0]] + 2
            
        if i < n:
            # Remove positions that can't give better results
            while dq and (dp[dq[-1]] - changes[dq[-1]] >= dp[i] - changes[i]):
                dq.pop()
            dq.append(i)
    
    return dp[n]

def visualize_delivery_plan(boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> str:
    """Helper function to visualize the delivery plan"""
    if not boxes:
        return "No boxes to deliver"
        
    # Calculate optimal solution with tracking
    n = len(boxes)
    dp = [0] * (n + 1)
    prev = [-1] * (n + 1)  # Track previous split points
    
    weights = [0]
    changes = [0]
    for i in range(n):
        weights.append(weights[-1] + boxes[i][1])
        changes.append(changes[-1] + (i > 0 and boxes[i][0] != boxes[i-1][0]))
    
    dq = deque([0])
    
    for i in range(1, n + 1):
        while dq and i - dq[0] > maxBoxes:
            dq.popleft()
        while dq and weights[i] - weights[dq[0]] > maxWeight:
            dq.popleft()
            
        if dq:
            dp[i] = dp[dq[0]] + changes[i] - changes[dq[0]] + 2
            prev[i] = dq[0]
            
        if i < n:
            while dq and (dp[dq[-1]] - changes[dq[-1]] >= dp[i] - changes[i]):
                dq.pop()
            dq.append(i)
    
    # Reconstruct delivery plan
    trips = []
    curr = n
    while curr > 0:
        trips.append((prev[curr], curr))
        curr = prev[curr]
    trips.reverse()
    
    # Create visualization
    result = ["Delivery Plan Visualization:"]
    result.append(f"Total ports: {portsCount}")
    result.append(f"Max boxes per trip: {maxBoxes}")
    result.append(f"Max weight per trip: {maxWeight}")
    result.append("\nBoxes:")
    
    # Show all boxes
    for i, (port, weight) in enumerate(boxes):
        result.append(f"Box {i}: Port {port}, Weight {weight}")
    
    result.append("\nDelivery trips:")
    
    # Show trips
    total_trips = dp[n]
    for trip_num, (start, end) in enumerate(trips):
        trip_boxes = boxes[start:end]
        trip_weight = sum(box[1] for box in trip_boxes)
        ports_visited = sorted(set(box[0] for box in trip_boxes))
        
        result.append(f"\nTrip {trip_num + 1}:")
        result.append(f"Boxes: {trip_boxes}")
        result.append(f"Total weight: {trip_weight}")
        result.append(f"Ports visited: {ports_visited}")
        
    result.append(f"\nTotal minimum trips required: {total_trips}")
    
    return "\n".join(result)

# Demo
if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Test case 1: Basic example
        (
            [[1,2],[1,2],[2,1],[2,1]],
            2, 3, 3
        ),
        # Test case 2: More complex routes
        (
            [[1,2],[2,4],[1,1],[2,1],[3,2]],
            3, 3, 6
        ),
        # Test case 3: Single box
        (
            [[1,1]],
            1, 1, 1
        ),
        # Test case 4: Same port deliveries
        (
            [[1,2],[1,2],[1,2]],
            1, 3, 6
        ),
        # Test case 5: Multiple constraints active
        (
            [[1,3],[2,2],[3,4],[2,2],[1,3]],
            3, 3, 7
        ),
        # Test case 6: Weight constraint dominant
        (
            [[1,1],[2,2],[3,3],[4,1],[5,2]],
            5, 10, 5
        )
    ]
    
    for i, (boxes, portsCount, maxBoxes, maxWeight) in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        
        # Calculate and display result
        min_trips = boxDelivering(boxes, portsCount, maxBoxes, maxWeight)
        print(f"\n{visualize_delivery_plan(boxes, portsCount, maxBoxes, maxWeight)}")
        print("-" * 70)
