# Web Search - Ollama | Tavily

## Setup Configs

### .env
``` TAVILY_API_KEY='...' ```
``` OLLAMA_API_KEY='...' ```

## Notebooks with examples

``` notebooks/main.ipynb ```

## Create ENV

``` conda env create -n web-search-env -f ./env.yml ```

## Update ENV

``` conda env update -n web-search-env -f ./env.yml ```

## Remove ENV

``` conda env remove --n web-search-env ```

## Activate ENV

``` conda activate web-search-env ```

## RUN

``` python src/main.py ```
``` python src/main.py --model qwen3:0.6b --web-searcher ollama --content "who is Goku?" ```
``` python src/main.py --model qwen3:0.6b --web-searcher tavily --content "who is Goku?" ```

## Ollama Snippets

### Install
``` https://ollama.com/download/linux ```

### Download Model
``` ollama pull qwen3:0.6b ```

### Run Model in CLI
``` ollama run qwen3:0.6b ```

### Official example
``` https://ollama.com/blog/web-search ```

## Other References

[github_author](https://github.com/Diegoomal)

[ollama](https://ollama.com/blog/web-search)

[tavily](https://www.tavily.com/)