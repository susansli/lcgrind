# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
# the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# nums = [1,2,3,4] --> [24,12,8,6] where 24 = 2 * 3 * 4, 12 = 1 * 3 * 4, and so on.
# nums = [-1,1,0,-3,3] --> [0,0,9,0,0]

# Constraints: 2 <= nums.length <= 105, -30 <= nums[i] <= 30

# The way I would solve this is to use floor division instead of division, since that fits the constraints
# of avoiding division (/). I would create an array that contains the product of every number in the array,
# then loop through to floor divide it by itself. Since each original value of nums would be a factor of the
# combined product, floor division will work the same as division.

# If nums contains 0s, if it contains more than a single 0, then the entire array must be 0
# If it only contains a single 0, then we must note what index it occurred and the product without the 0
# changing the index manually.

def product_except_self(nums):
    zero_index = None
    combined_product = None

    for i in range(len(nums)):
        if nums[i] == 0:
            if zero_index is None:
                zero_index = i
                if combined_product is None:  # this means that 0 is the first number
                    combined_product = 1
            else:
                combined_product = 0  # we have multiple 0s so the entire array would be 0
        else:
            if combined_product is None:
                combined_product = nums[i]
            else:
                combined_product *= nums[i]

    output = [combined_product for _ in range(len(nums))]

    for i in range(len(output)):
        if zero_index is not None:
            if i != zero_index:
                output[i] = 0
        else:
            output[i] = output[i] // nums[i]

    return output


# Admittedly this feels kind of cheap since I'm still doing division.
# The optimal solution is with pre and postfix (neetcode solution):

def product_except_self_prepost(nums):
    # 1. Create an array of 1s the length of nums
    output = [1 for _ in range(len(nums))]

    # 2. initiate a value as product to be modified
    product = 1

    # 3. Loop through the nums array, multiplying product by each subsequent one
    for i in range(len(nums)):
        output[i] = product
        product *= nums[i]

    # 4. Reset product
    product = 1

    # Loop through the nums array in reverse, doing essentially the reverse of step 3 but
    # multiplying each preceding value by the product
    for i in range(len(nums) - 1, -1, -1):  # reverses range iterator
        output[i] *= product
        product *= nums[i]
    return output


print(product_except_self_prepost([1, 2, 3, 4]))
