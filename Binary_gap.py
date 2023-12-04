def solution(N):
    longest_bin_gap = []
    binary_rep = "{0:b}".format(N)
    if binary_rep.count("0")!=0:
        for i in range(len(binary_rep)):
            if binary_rep[i]=="1":
                adjacent = binary_rep.find("1", i+1)
                if adjacent !=-1:
                    longest_bin_gap.extend([adjacent-i-1])
                else:
                    longest_bin_gap.extend([0])
        return max(longest_bin_gap)
    else:
        return 0