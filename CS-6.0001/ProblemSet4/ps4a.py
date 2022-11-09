# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return [sequence]

    permutations = []
    for small_perm in get_permutations(sequence[1:]):
        for i in range(len(small_perm) + 1):
            permutations.append(small_perm[:i] + sequence[0] + small_perm[i:])
    return permutations


if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
    print('Actual Output:', sorted(get_permutations(example_input)), end="\n\n")

    example_input = 'bdh'
    print('Input:', example_input)
    print('Expected Output:', sorted(['bdh', 'bhd', 'dbh', 'dhb', 'hdb', 'hbd']))
    print('Actual Output:', sorted(get_permutations(example_input)), end="\n\n")

    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', sorted(['xyz', 'xzy', 'yzx', 'yxz', 'zyx', 'zxy']))
    print('Actual Output:', sorted(get_permutations(example_input)), end="\n\n")
    


