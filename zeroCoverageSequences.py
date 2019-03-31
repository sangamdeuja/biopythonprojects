# Write a function gap_position_count(seq_len, read_len, coverage) 
# seq_len --- the length of the underlying sequence from which we draw reads
# read_len --- the length of individual reads
# coverage --- the desired (average) coverage of the sequence
# The function simulates extracting reads of read_len bases at random
# positions from an underlying sequence of seq_len bases until the
# average coverage is reached.
# For example if seq_len=1000, read_len=100 and coverage=5, you
# would need a total of 5000 bases worth of reads to get an average
# coverage of 5, i.e. you'd need 50 reads.
# The function should return the number of bases which receive
# zero coverage, ie are not covered by any of the reads.



from random import randint

#changing read_len large to small value showed that lower the read length less is the gap formation while sequencing.

        
def gap_position_count(seq_len,read_len,coverage):
    bases=[]
    empty_pos=[]
    #number of reads=seq_len*coverage/read_len
    for loop in range(0,seq_len*coverage/read_len):
        random_pos=randint(0,seq_len-read_len+1)
        read_positions=range(random_pos,random_pos+read_len)
        bases.extend(read_positions)
    for i in range(0,seq_len):
        if i not in bases:
            empty_pos.append(i)
    #adding 1 to each position to start counting 1 for first element of sequence
    empty_base_pos=[item+1 for item in empty_pos]
    return empty_base_pos

