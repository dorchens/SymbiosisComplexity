import os
import os.path

import gzip

folder = '../../Data/diversity-2022-08-11' #change this later

verts = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
reps = range(10,18)
header = "rep, VT_rate, alpha_diversity, shannon_diversity\n" #update,

outputFileName = "munged_diversity.csv"

outFile = open(outputFileName, 'w')
outFile.write(header)

#./Output_VT0.0_SEED10.data'
for v in verts:
    for r in reps:
        #_modularity__Modularity_0.0_SEED12
        fname = f"{folder}/_diversity__Diversity_{v}_SEED{r}.data"
        curFile = open(fname, 'r')
        # donatedFile = open(f"{folder}SymDonated_VT_{v}_SEED{r}.data", 'r')
        # donatedFile.readline()
        # mutualismFile = open(f"{folder}SymImpact_VT_{v}_SEED{r}.data", 'r')
        # mutualism = mutualismFile.readline().strip()
        print(f"----VT_{v}_SEED{r}----")
        
        curFile.readline()
        string = curFile.readline()
        
        line = string.split(' ')
        if(len(line)>1):
            outstring = "{}, {}, {}, {}".format(r, v, line[0], line[1])
            outFile.write(outstring)
        # else:
        #     print(len(line))
                
        curFile.close()
outFile.close()