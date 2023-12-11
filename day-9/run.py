input = open('file.in', 'r').read().split('\n')

def solve(seq):
    st= []
    while(seq != [0] * len(seq)):
        st.append(seq[0])
        new_seq = []
        for i in range(1, len(seq)):
            new_seq.append(seq[i] - seq[i-1])
        seq = new_seq
    seq.append(0)
    for starting in st[-1::-1]:
        new_seq = [starting]
        for i in range(0, len(seq)):
            new_seq.append(new_seq[i] + seq[i])
        seq = new_seq
        print(seq)
    return seq[-1]

sum = 0

for seq in input:
    seq = [int(x) for x in seq.split(" ")]
    seq = seq[-1::-1]
    print(seq)
    sum += solve(seq)
    print()

print(sum)