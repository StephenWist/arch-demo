#!/bin/bash
# install nextflow to run single cell NGS processing
apt install -y openjdk-19-jre-headless
apt install -y python3 pip3
apt install -y curl wget
curl -s https://get.nextflow.io | bash
chmod +x nextflow
nextflow self-update

# get human genome references
wget -L ftp://ftp.ensembl.org/pub/release-108/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz
wget -L ftp://ftp.ensembl.org/pub/release-108/gtf/homo_sapiens/Homo_sapiens.GRCh38.108.gtf.gz