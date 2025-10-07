from typing import Optional


def find_min_max(arr: list[int], left: Optional[int] = None, right: Optional[int] = None) -> tuple[int, int]:
    """
    Find the minimum and maximum values in an array using a divide-and-conquer approach.

    Args:
        arr (list[int]): List of integers
        left (int, optional): Left index of the subarray (inclusive)
        right (int, optional): Right index of the subarray (inclusive)

    Returns:
        tuple[int, int]: A tuple containing the minimum and maximum values
    """
    if not arr:
        raise ValueError("Array must not be empty")
    
    left = 0 if left is None else left
    right = len(arr) - 1 if right is None else right

    if left < 0 or right >= len(arr) or left > right:
        raise ValueError("Invalid left or right indices")
    
    if left == right:
        return arr[left], arr[left]
    if right - left == 1:
        return min(arr[left], arr[right]), max(arr[left], arr[right])

    mid = (left + right) // 2
    min1, max1 = find_min_max(arr, left, mid)
    min2, max2 = find_min_max(arr, mid + 1, right)

    return min(min1, min2), max(max1, max2)


def tests():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    r_min, r_max = find_min_max(arr)
    print(f"Min: {r_min}, Max: {r_max} of {arr}")
    assert (r_min, r_max) == (1, 9)

    arr = [-1, -2, -3, -4, -5]
    r_min, r_max = find_min_max(arr)
    print(f"Min: {r_min}, Max: {r_max} of {arr}")
    assert (r_min, r_max) == (-5, -1)

    arr = [42]
    r_min, r_max = find_min_max(arr)
    print(f"Min: {r_min}, Max: {r_max} of {arr}")
    assert (r_min, r_max) == (42, 42)

    arr = [3, 3]
    r_min, r_max = find_min_max(arr)
    print(f"Min: {r_min}, Max: {r_max} of {arr}")
    assert (r_min, r_max) == (3, 3)
    arr = [3, 1]
    r_min, r_max = find_min_max(arr)
    print(f"Min: {r_min}, Max: {r_max} of {arr}")
    assert (r_min, r_max) == (1, 3)

    print("All tests passed.")


if __name__ == "__main__":
    tests()
