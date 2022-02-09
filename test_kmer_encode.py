import numpy as np
from kmer import kmer_featurization  # import the module kmer_featurization from the kmer.py file

# If you just pass one sequence in string:
seq = 'ANTETTKVNGSLETKYRWTEYGLTFTEKWNTDNTLGTEITV'
k = 2
obj = kmer_featurization(k) 
kmer_feature = obj.obtain_kmer_feature_for_one_sequence(seq, write_number_of_occurrences=False)
print(np.count_nonzero(kmer_feature))
np.savetxt("kmer.txt", kmer_feature, delimiter=',')
