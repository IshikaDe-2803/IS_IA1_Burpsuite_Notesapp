

    
    # Extract the plagiarism score (Diffbot provides a similarity score)
    plagiarism_score = data.get('plagiarismScore', None)
    
    if plagiarism_score is not None:
        print(f"Plagiarism Score: {plagiarism_score}")
    else:
        print("Plagiarism score not available.")
else:
    print(f"Error: {response.status_code}")
