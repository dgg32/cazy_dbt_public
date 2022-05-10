{{ config(alias=var("family") + "_taxid") }}

WITH
gene AS (
    SELECT accession, cazy, name
    FROM
    {{ source('cazy', 'gene') }}
),
genome AS (
    SELECT taxid, name
    FROM {{ source('cazy', 'genome') }}
)
SELECT
    genome.taxid,
    gene.accession
FROM genome, gene
WHERE genome.name = gene.name AND gene.cazy = '{{ var("family") }}' AND genome.taxid IS NOT NULL