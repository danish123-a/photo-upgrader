import requests
import os

def download_image(url, save_path="output/raw_alibaba.jpg"):
    print("📥 Step 1: Downloading raw photo...")
    try:
        # Some websites block Python, so we use a standard browser header
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
                
        print(f"   ✅ Raw image saved to {save_path}")
        return save_path
    except Exception as e:
        print(f"❌ Error downloading image: {e}")
        return None