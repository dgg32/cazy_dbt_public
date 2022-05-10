

# Introduction

  

  

This repository contains code and data for my article "Analyze CAZy with dbt, Snowflake and Preset](https://towardsdatascience.com/neo4j-for-diseases-959dffb5b479)".

1. The python scripts are for data processing.

  

2. The cazy folder contains the dbt project.

  
3. The GH17.tsv is for the Krona plot. 

# Prerequisite

dbt, accounts in Snowflake and Preset
  

# Run

  
  
1. Connect dbt to Snowflake
```console
dbt init cazy
```
 
2. Run the models
```console
dbt run --vars '{"family": "GH17"}'
```


## Authors

  

*  **Sixing Huang** - *Concept and Coding*

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
