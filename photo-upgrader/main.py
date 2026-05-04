import os
from dotenv import load_dotenv

from downloader import download_image
from studio import create_studio_shot
from upscale import upscale_image

load_dotenv()

def run_pipeline():
    print("🚀 Starting AI Photo Upgrader Engine...\n")
    
    if not os.path.exists('output'):
        os.makedirs('output')
        
    # Get user inputs
    image_url = input("🔗 Paste the URL of the crappy product photo: ")
    print("\nExample prompt: 'minimalist white marble pedestal, soft cinematic studio lighting, blurred background'")
    studio_prompt = input("🎨 Describe the background you want: ")
    print("\n" + "="*40 + "\n")
    
    # Run the pipeline
    raw_img = download_image(image_url)
    if not raw_img: return
    
    studio_img = create_studio_shot(raw_img, studio_prompt)
    if not studio_img: return
    
    final_img = upscale_image(studio_img)
    
    print("\n" + "="*40 + "\n")
    print("Done! Open your 'output' folder to see the transformation.")

if __name__ == "__main__":
    run_pipeline()