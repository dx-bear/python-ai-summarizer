# 1. Import necessary libraries
import asyncio
import argparse
import os
from dotenv import load_dotenv
from wreq import Client, Proxy, Emulation, Multipart, Part
from wreq.header import HeaderMap

# 2. Load environment variables from the .env file
load_dotenv()

# 3. Define the main asynchronous function
async def generate_response(prompt: str):
    
    # 4. Set up custom headers to mimic a real browser request
    custom_headers = HeaderMap(
        {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-gpc": "1",
            "x-s": "fdAlickdia.",
            "Referer": "https://www.hyperwriteai.com/",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
        }
    )

    # 5. Retrieve proxy URL from the .env file (defaults to empty string if not found)
    proxy_url = os.getenv("PROXY_URL", "")
    
    # 6. Set up the proxy configuration 
    proxy = Proxy.all(url=proxy_url)

    # 7. Create the HTTP client with proxy and browser emulation (Chrome 131)
    client = Client(proxies=[proxy], emulation=Emulation.Chrome131)

    # 8. Create the multipart payload containing the user's prompt
    multipart_data = Multipart(  
        Part(name="text_input", value=prompt),  
        Part(name="tool_name", value="summarize")  
    )

    # 9. Send the asynchronous POST request to the API
    response = await client.post(  
        "https://api.hyperwriteai.com/write_free",  
        headers=custom_headers,  
        multipart=multipart_data  
    )

    # 10. Check if the response is successful and extract the written text
    if response.status.is_success():
        result = await response.json()
        response_text = result.get("written_text", None)
        return response_text
    else:
        # Return an error message if the request failed
        return f"Error: Request failed with status code {response.status}"

# 11. Set up the command-line interface (CLI)
def main():
    
    # 12. Initialize the argument parser
    parser = argparse.ArgumentParser(description="Send a prompt to the AI Summarizer tool and print the response.")
    
    # 13. Add an argument for the prompt
    parser.add_argument(
        "prompt", 
        type=str, 
        help="The long text you want to summarize. Ensure it is wrapped in quotes."
    )
    
    # 14. Parse the arguments passed in the command line
    args = parser.parse_args()

    # 15. Run the async function using asyncio and print the final result
    result = asyncio.run(generate_response(args.prompt))
    print(result)

# 16. Standard Python boilerplate to execute the script
if __name__ == "__main__":
    main()