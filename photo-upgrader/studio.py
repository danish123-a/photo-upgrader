import os
import requests

def create_studio_shot(image_path, prompt, output_path="output/studio_shot.jpg"):
    print("🎨 Step 2: Removing messy background & generating studio scene...")
    
    api_key = os.getenv("STABILITY_API_KEY")
    url = "https://api.stability.ai/v2beta/stable-image/edit/replace-background"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "image/*"
    }
    
    # We send the image file and our prompt for the new background
    files = {"image": open(image_path, "rb")}
    data = {
        "prompt": prompt,
        "output_format": "jpeg"
    }
    
    response = requests.post(url, headers=headers, files=files, data=data)
    
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"   ✅ Studio shot created at {output_path}")
        return output_path
    else:
        print(f"❌ Error in Studio step: {response.json()}")
        return None