-- Set up the defaults
USE WAREHOUSE COMPUTE_WH;
USE DATABASE cazy;
USE SCHEMA RAW;

CREATE OR REPLACE TABLE raw_cazy_data
        (cazy string,
        superkingdom string,
        name string,
        accession string);
COPY INTO raw_cazy_data (cazy,
        superkingdom,
        name,
        accession)
from 's3://datathon-medium-file/cazy_data_formatted.csv.gz'
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' skip_header = 1);


CREATE OR REPLACE TABLE raw_cazy_genome
        (name string,
        taxid string,
        superkingdom string,
        phylum string,
        class string,
        "ORDER" string,
        family string,
        genus string,
        species string);
COPY INTO raw_cazy_genome (name,
        taxid,
                          superkingdom, phylum, class, "ORDER", family, genus, species)
from 's3://datathon-medium-file/cazy_genome.csv.gz'
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' skip_header = 1);