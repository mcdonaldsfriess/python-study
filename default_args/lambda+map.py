def square(x):
    return x * x

square = lambda x: x * x


nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums)) #[1 4, 9, 16]


nums = [1, 2, 3, 4, 5, 6,]
evens = list(filter(lambda x: x % 2 == 0, nums)) #[2, 4, 6]

squares = [x * x for x in nums] #[1, 4, 9, 16 instead of map
evens = [x for x in nums if x % 2 == 0] #[2, 4, 6 instead of filter
comvined = [x * x for x in nums if x % 2 == 0] #[4, 16 map + filter together
