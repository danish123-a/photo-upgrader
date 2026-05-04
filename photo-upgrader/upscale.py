import os
import requests

def upscale_image(image_path, output_path="output/FINAL_4K_STUDIO.jpg"):
    print("✨ Step 3: Upscaling to crisp 4K resolution...")
    
    api_key = os.getenv("STABILITY_API_KEY")
    url = "https://api.stability.ai/v2beta/stable-image/upscale/fast"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "image/*"
    }
    
    files = {"image": open(image_path, "rb")}
    data = {"output_format": "jpeg"}
    
    response = requests.post(url, headers=headers, files=files, data=data)
    
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"   🎉 SUCCESS! Final 4K Image saved at {output_path}")
        return output_path
    else:
        print(f"❌ Error in Upscale step: {response.json()}")
        return None