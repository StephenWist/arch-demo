#!/bin/bash
curl 'ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/GDSnnn/GDS999/soft/GDS999.soft.gz' -o 'GDS999.soft.gz'
gunzip 'GDS999.soft.gz'