# Problem 1. CyclicRotation:
def solution(A, K):
    # if A = [] empty list:
    if len(A) == 0:
        return A

    result = A[:]  # shallow copy of list
    # shift everything right by 1 and move last number to start of list:
    for i in range(K):
        last = result.pop()  # remove last number
        result.insert(0, last)  # insert last number at start
    return result


# Problem 2. OddOccuranceInArray:
# there will only ever be one unpaired entry and there will always be one unpaired so those edge cases are not needed, there will also never be an empty list
def solution(A):
    counts = {}  # empty dictionary
    # find current count of that number and add 1 to that
    for num in A:
        counts[num] = counts.get(num, 0) + 1
    # find the odd count
    for num, count in counts.items():
        if count % 2 == 1:  # check if count is odd
            return num  # if odd, then return that number as unpaired number


# Problem 3. FrogJmp:
def solution(X, Y, D):
    distance_across_road = Y - X  # frog starts at X
    jumps = distance_across_road // D  # number of full jumps needed
    # if left over distance but less then a full jump left, then do another jump to cross the road farther than needed
    if distance_across_road % D > 0:  # left over distnace if greater than Ø
        jumps += 1
    return jumps


# Problem 4. PermMissingElem:
def solution(A):
    N = len(A)
    expected_sum = (N + 1) * (N + 2) // 2  # total if nothing was missing from the order
    actual_sum = sum(A)  # sum of all numbers
    missing_number = expected_sum - actual_sum  # difference is the missing number
    return missing_number


# Problem 5. TapeEquilibrium:
def solution(A):
    total = sum(A)  # total sum
    left = 0  # partial sum
    min_diff = None  # minimal difference

    for P in range(
        1, len(A)
    ):  # cut tape at P starting after 1st value when left side is not empty, ending before the last value so right side is not empty
        left += A[P - 1]  # move number left on the tape
        right = total - left  # everything else is on the right
        difference = abs(left - right)  # for this split, absolute difference
        if min_diff is None or difference < min_diff:
            min_diff = difference  # new smallest difference

    return min_diff  # example return 1
