from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
# project_id = "YOUR_PROJECT_ID"
# model_id = "YOUR_MODEL_ID"
# file_path = "path_to_local_file.txt"

prediction_client = automl.PredictionServiceClient()

# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path("gcp-project-319802", "us-central1", "TST2306007935957860352")

# Read the file content for translation.
#with open(file_path, "rb") as content_file:
with open("Test_Files/TestInput.csv", "rb") as content_file:
    content = content_file.read()
content.decode("utf-8")

text_snippet = automl.TextSnippet(content=content)
payload = automl.ExamplePayload(text_snippet=text_snippet)

response = prediction_client.predict(name=model_full_id, payload=payload)
translated_content = response.payload[0].translation.translated_content

print(u"Translated content: {}".format(translated_content.content))
