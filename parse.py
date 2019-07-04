from Bio import SeqIO
import sys
#fastq=sys.argv[1]
fastq="ShortRead_1.fastq"
c=1
with open(fastq) as t:
    with open(fastq[:-6] +"_parsed.fastq", "w") as s:
        for record in SeqIO.parse(t, "fastq"):
            record.id=str(c)+"/1"
            SeqIO.write(record, s, "fastq")
            c=c+1
c=1
with open(fastq[:-7]+ "2.fastq") as t:
    with open(fastq[:-7] +"2_parsed.fastq", "w") as s:
        for record in SeqIO.parse(t, "fastq"):
            record.id=str(c)+"/2"
            SeqIO.write(record, s, "fastq")
            c=c+1
