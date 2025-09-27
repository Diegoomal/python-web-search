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
``` ollama pull gemma3:1b ```

### Run Model in CLI
``` ollama run gemma3:1b ```

### Official example
``` https://ollama.com/blog/web-search ```



## Other References

### tavily web search
``` https://www.tavily.com/ ```



## Links

[github_author](https://github.com/Diegoomal)

[project_ref](https://github.com/Diegoomal/diffusers/)

[olhar_digital](https://olhardigital.com.br/2025/04/28/pro/microsoft-cria-ia-que-roda-dentro-de-pcs-normais/)

[bitnet_model_page_huggingfaces](https://huggingface.co/microsoft/bitnet-b1.58-2B-4T)