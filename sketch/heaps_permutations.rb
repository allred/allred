#!/usr/bin/ruby
# Heap's permutations algorithm

def perms(array, n = array.size-1)
    # return a permutation or recurse
    if  n == 0
        p array
        return array
    else
        for i in 0..n do
            perms(array, n-1)
            if (n-1) % 2 == 1
                array[1], array[n] = array[n], array[1]
            else
                array[i], array[n] = array[n], array[i]
            end
        end
    end
end

perms [1, 2, 3]
