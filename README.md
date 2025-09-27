# Ollama Web Search

## Setup Configs

### .env
``` TAVILY_API_KEY='...' ```
``` OLLAMA_API_KEY='...' ```

## Notebooks with examples

``` notebooks/main.ipynb ```

## Create ENV

``` conda env create -n ollama-websearch-env -f ./env.yml ```

## Update ENV

``` conda env update -n ollama-websearch-env -f ./env.yml ```

## Remove ENV

``` conda env remove --n ollama-websearch-env ```

## Activate ENV

``` conda activate ollama-websearch-env ```

## RUN

``` python src/main.py ```
``` python src/main.py --model qwen3:0.6b --web-searcher ollama --content "what is ollama's new engine" ```
``` python src/main.py --model qwen3:0.6b --web-searcher tavily --content "what is ollama's new engine" ```

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

[tavily](https://www.tavily.com/)