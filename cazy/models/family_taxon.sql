{{ config(alias=var("family") + "_taxon") }}

WITH
gene AS (
    SELECT name, cazy, accession
    FROM
    {{ source('cazy', 'gene') }}
),
genome AS (
    SELECT name, superkingdom, phylum, class, genus
    FROM {{ source('cazy', 'genome') }}
)
SELECT
    gene.accession,
    genome.superkingdom,
    genome.phylum,
    genome.class,
    genome.genus
    
FROM genome, gene
WHERE genome.name = gene.name AND gene.cazy = '{{ var("family") }}' AND genome.superkingdom IS NOT NULL AND genome.phylum IS NOT NULL AND genome.class IS NOT NULL AND genome.genus IS NOT NULL