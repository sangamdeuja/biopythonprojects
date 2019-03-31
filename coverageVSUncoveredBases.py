##When testing your function for the Random Coverage exercise,
##you have noticed that the number of uncovered bases differs a lot
##because of randomness. Stabilize the results by providing a function 
##avg_gap_position_count(seq_len, read_len, coverage, N_trials)
##which is like the previous function, but performs N runs and
##averages the results. When submitting the exercise code, paste into
##the comments the output for varying coverage between
##1 and 9, seq_len=2000, read_len=20, N_trials=1000.
##Print the percent of bases which are, on average, left uncovered. Like so:
##
##coverage= 1 leaves 36.728 % uncovered bases
##coverage= 2 leaves 13.68085 % uncovered bases
##coverage= 3 leaves 5.2204 % uncovered bases
##coverage= 4 leaves 2.1699 % uncovered bases
##coverage= 5 leaves 0.94695 % uncovered bases
##coverage= 6 leaves 0.49805 % uncovered bases
##coverage= 7 leaves 0.3123 % uncovered bases
##coverage= 8 leaves 0.224 % uncovered bases
##coverage= 9 leaves 0.18875 % uncovered bases


from random import randint

        
def avg_gap_position_count(seq_len,read_len,coverage,N_trials):
    count=0
    #stabilizing the variation in uncovered bases count
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
               
        count=count+len(empty_pos)
    average_gap=float(count)/N_trials
    percentage_gap=average_gap/seq_len*100
    return percentage_gap

for coverage in range(1,10):
    print 'coverage=',coverage,'leaves',avg_gap_position_count(2000,20,coverage,1000),' % uncovered bases'

##coverage= 1 leaves 36.75455  % uncovered bases
##coverage= 2 leaves 13.65305  % uncovered bases
##coverage= 3 leaves 5.2499  % uncovered bases
##coverage= 4 leaves 2.09165  % uncovered bases
##coverage= 5 leaves 0.9155  % uncovered bases
##coverage= 6 leaves 0.4666  % uncovered bases
##coverage= 7 leaves 0.2698  % uncovered bases
##coverage= 8 leaves 0.1951  % uncovered bases
##coverage= 9 leaves 0.14895  % uncovered bases
