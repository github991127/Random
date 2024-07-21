from random import randint, sample


def generate_sequence(start, end, length, repeat):  # 生成[start,end]中的length个数,repeat=0则不重复
    nums = []
    if repeat:
        for i in range(length):
            nums.append(randint(start, end))
    else:
        if length > end - start + 1:
            raise ValueError("Cannot generate non-repeating sequence with given parameters.")
        nums = sample(range(start, end + 1), length)
    return nums


def main(start=0, end=5, length=5, repeat=0):
    nums = generate_sequence(start, end, length, repeat)
    print(nums)
    return nums


if __name__ == "__main__":
    main()
