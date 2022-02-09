import readFasta
import saveCode
from utils import CKSAAP
fastas = readFasta.readFasta('./ifeatpro_data/seq.fa')
kw = {'order': 'ACDEFGHIKLMNPQRSTVWY'}
output="encode.tsv"
saveCode.savetsv(CKSAAP(fastas, 5, **kw), output)
# print(CKSAAP(fastas, 5, **kw))
