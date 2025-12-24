import google.generativeai as genai

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Run a web query using the model
def web_query(q):
    response = model.generate_content(q)
    return response.text
