
To create a website that will check if the person is wearing a mask or not.

Target Audience:
This web application is aimed at helping organizations take precautions against covid 19 by tracking whether employees are wearing masks.

Tech Stack:
FrontEnd: Figma, HTML, CSS, Bootstrap BackEnd: Flask Libraries: OpenCV, Keras, tensorflow

References:

Rapid Object Detection using a Boosted Cascade of Simple Features - Viola and Jones
https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
"""

# Define the Diffbot API endpoint for article analysis
diffbot_api_url = 'https://api.diffbot.com/v3/article'

# Set up the API request parameters
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
