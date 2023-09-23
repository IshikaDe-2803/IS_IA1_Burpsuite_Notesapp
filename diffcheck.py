

api_params = {
    'token': api_key,
    # 'url': 'https://github.com/IshikaDe-2803/MiniProject_SemIV',  # Leave this empty for raw text analysis
    'html': document_content,  # Use this for raw text analysis
}

# Send a POST request to the Diffbot API
response = requests.post(diffbot_api_url, data=api_params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)
    
    # Extract the plagiarism score (Diffbot provides a similarity score)
    plagiarism_score = data.get('plagiarismScore', None)
    
    if plagiarism_score is not None:
        print(f"Plagiarism Score: {plagiarism_score}")
    else:
        print("Plagiarism score not available.")
else:
    print(f"Error: {response.status_code}")
