__author__ = 'koshlan'
# 0    # Nucleotide Sequences With Mates
# 1    # Nucleotide Sequences With Quality
# 2    # Nucleotides
# 3    # Sequences
# 4    % Identical Sites
# 5    % Pairwise Identity
# 6    Accession
# 7    Bit-Score
# 8    Created Date
# 9    Database
# 10    Description
# 11    E Value
# 12    Free end gaps
# 13    Grade
# 14    Hit end
# 15    Hit start
# 16    Max Sequence Length
# 17    Mean Coverage
# 18    Min Sequence Length
# 19    Modified
# 20    Molecule Type
# 21    Name
# 22    Original Query Frame
# 23    Query
# 24    Query coverage
# 25    Query end
# 26    Query start
# 27    Ref Seq Index
# 28    Ref Seq Length
# 29    Ref Seq Name
# 30    Sequence
# 31    Sequence Length
# 32    Topology
class geneious_blast_line_holder():
    def __init__(self, MyList):
        self.Pos = {'Query':25,'Name':22, 'PairwiseIdentity':5, 'QueryCoverage':26}
        self.MyList = MyList
        self.Query  = str()
        self.Name = str()
        self.QueryCoverage = str()
    def populate(self):
        self.Query = self.MyList[self.Pos['Query']]
        self.Name = self.MyList[self.Pos['Name']]
        self.QueryCoverage = self.MyList[self.Pos['QueryCoverage']]
        self.PairwiseIdentity = self.MyList[self.Pos['PairwiseIdentity']]
    def repair_percentage(self,x):
        return float(x.replace("%",""))
    def check_if_value_exceeds(self, some_value, some_threshold):
        if some_value > some_threshold:
            return True
        else:
            return False

def network_recover_geneious_table(fn):
    fh = open(fn, 'r')
    fh.readline() # remove Header
    for line in fh:
        line = line.strip().split("\t")
        x = geneious_blast_line_holder(line)
        x.populate()
        x.QueryCoverage = x.repair_percentage(x.QueryCoverage)
        x.PairwiseIdentity = x.repair_percentage(x.PairwiseIdentity)

        QueryCoveragePass = x.check_if_value_exceeds(x.QueryCoverage, 90)
        PerIDPass = x.check_if_value_exceeds(x.PairwiseIdentity, 50)
        if PerIDPass and QueryCoveragePass:
            print x.Query, x.Name, x.PairwiseIdentity

if __name__ == "__main__":
    network_recover_geneious_table("/Users/koshlan/PycharmProjects/GeneNet/data/EV5L_VS5L_recovered_rdhA_blast_all_v_all_geneious.tsv")


