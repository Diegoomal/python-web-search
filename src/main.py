import argparse, os
from dotenv import load_dotenv                                                  # type: ignore
from tavily import TavilyClient                                                 # type: ignore
from ollama import chat, web_fetch, web_search                                  # type: ignore


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process model, web searcher and content parameters')
    parser.add_argument('--model',          type=str, required=True, help='Model parameter',        default='llama2')
    parser.add_argument('--web-searcher',   type=str, required=True, help='Web searcher parameter', default='ollama', choices=['ollama', 'tavily'])
    parser.add_argument('--content',        type=str, required=True, help='Content parameter',      default="what is ollama's new engine")
    return parser.parse_args()


def run_search(model: str, content: str, available_tools):

    print("available_tools:", available_tools.values())

    messages = [{'role': 'user', 'content': content}]

    while True:
        
        response = chat(model=model, messages=messages, tools=list(available_tools.values()), think=True)

        if response.message.thinking: print('Thinking: ', response.message.thinking)

        if response.message.content: print('Content: ', response.message.content)
        
        messages.append(response.message)
        
        if not response.message.tool_calls: break

        print('Tool calls: ', response.message.tool_calls)
        
        for tool_call in response.message.tool_calls: function_to_call = available_tools.get(tool_call.function.name)

        if not function_to_call:
            messages.append({'role': 'tool', 'content': f'Tool {tool_call.function.name} not found', 'tool_name': tool_call.function.name})
            continue

        args = tool_call.function.arguments
        result = function_to_call(**args)
        print('Result: ', str(result)[:200]+'...')
        # Result is truncated for limited context lengths
        messages.append({'role': 'tool', 'content': str(result)[:2000 * 4], 'tool_name': tool_call.function.name})


def main():

    load_dotenv()

    args = parse_arguments()

    if args.web_searcher not in ['ollama', 'tavily']: raise ValueError('Invalid web searcher. Choose either "ollama" or "tavily".')
    
    available_tools = None

    if args.web_searcher == 'ollama':

        if os.getenv('OLLAMA_API_KEY') is None: raise ValueError('OLLAMA_API_KEY environment variable not set.')
        
        available_tools = {'web_search': web_search, 'web_fetch': web_fetch}

        def ollama_web_search(query: str):  return web_search(query=query, max_results=3)
        available_tools = {'web_search': ollama_web_search, 'web_fetch': web_fetch}

    elif args.web_searcher == 'tavily':
        
        if os.getenv('TAVILY_API_KEY') is None: raise ValueError('TAVILY_API_KEY environment variable not set.')
        
        def tavily_web_search(query: str):
            tavily = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))
            return tavily.search(query=query, max_results=3)['results']
        
        available_tools = {'web_search': tavily_web_search}  

    run_search(model=args.model, content=args.content, available_tools=available_tools)


if __name__ == "__main__":
    main()
