import requests
from bs4 import BeautifulSoup
import os
import time
import logging

# Set up logging
logging.basicConfig(filename='image_scraper.log', level=logging.ERROR)

def get_image_urls(query, num_images):
    """Scrapes image URLs from Google Image Search with pagination."""
    search_url = "https://www.google.com/search?q={query}&source=lnms&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    image_urls = []
    start = 0

    while len(image_urls) < num_images:
        url = search_url.format(query=query) + f"&start={start}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all("img")
        for img_tag in img_tags:
            img_url = img_tag.get("src")
            if img_url and img_url.startswith("http"):
                if img_url not in image_urls:
                    image_urls.append(img_url)
                if len(image_urls) >= num_images:
                    break

        start += 20
        time.sleep(2)

    return image_urls

def save_images(image_urls, guitar_model, prefix, query_type, specific_name):
    """Downloads and saves images from URLs to a specified folder, naming them uniquely."""
    guitar_folder = os.path.join('data/raw_data', guitar_model)
    if not os.path.exists(guitar_folder):
        os.makedirs(guitar_folder)

    for idx, img_url in enumerate(image_urls):
        try:
            img_data = requests.get(img_url).content
            file_name = os.path.join(guitar_folder, f"{prefix}_{query_type}_{specific_name}_{idx + 1}.jpg")
            with open(file_name, 'wb') as img_file:
                img_file.write(img_data)
            print(f"Saved: {file_name}")
        except Exception as e:
            logging.error(f"Failed to save image {idx + 1}: {e}")

# Number of images to scrape for each category
num_angle_images = 200
num_context_images = 150
num_orientation_images = 100
num_inuse_images = 50

# Search Queries for Fender Jaguar
jaguar_angle_queries = {
    "side_view": "Fender Jaguar guitar side view",
    "top_down": "Fender Jaguar guitar top-down view",
    "bottom_up": "Fender Jaguar guitar bottom-up view",
    "45_degree_angle": "Fender Jaguar guitar 45 degree angle",
    "angled_profile": "Fender Jaguar guitar angled profile"
}
jaguar_context_queries = {
    "studio_background": "Fender Jaguar guitar studio background",
    "on_stage": "Fender Jaguar guitar on stage",
    "in_concert": "Fender Jaguar guitar in concert",
    "outdoors": "Fender Jaguar guitar outdoors",
    "recording_studio": "Fender Jaguar guitar in recording studio"
}
jaguar_orientation_queries = {
    "flat_on_table": "Fender Jaguar guitar flat on table",
    "tilted": "Fender Jaguar guitar tilted",
    "horizontal_view": "Fender Jaguar guitar horizontal view",
    "rotated": "Fender Jaguar guitar rotated"
}
jaguar_inuse_queries = {
    "player_holding": "Fender Jaguar guitar player holding",
    "being_played": "Fender Jaguar guitar being played",
    "live_performance": "Fender Jaguar guitar live performance",
    "musician_playing": "Fender Jaguar guitar musician playing"
}

# Search Queries for Fender Telecaster
telecaster_angle_queries = {
    "side_view": "Fender Telecaster guitar side view",
    "top_down": "Fender Telecaster guitar top-down view",
    "bottom_up": "Fender Telecaster guitar bottom-up view",
    "45_degree_angle": "Fender Telecaster guitar 45 degree angle",
    "angled_profile": "Fender Telecaster guitar angled profile"
}
telecaster_context_queries = {
    "studio_background": "Fender Telecaster guitar studio background",
    "on_stage": "Fender Telecaster guitar on stage",
    "in_concert": "Fender Telecaster guitar in concert",
    "outdoors": "Fender Telecaster guitar outdoors",
    "recording_studio": "Fender Telecaster guitar in recording studio"
}
telecaster_orientation_queries = {
    "flat_on_table": "Fender Telecaster guitar flat on table",
    "tilted": "Fender Telecaster guitar tilted",
    "horizontal_view": "Fender Telecaster guitar horizontal view",
    "rotated": "Fender Telecaster guitar rotated"
}
telecaster_inuse_queries = {
    "player_holding": "Fender Telecaster guitar player holding",
    "being_played": "Fender Telecaster guitar being played",
    "live_performance": "Fender Telecaster guitar live performance",
    "musician_playing": "Fender Telecaster guitar musician playing"
}

# Search Queries for Fender Stratocaster
stratocaster_angle_queries = {
    "side_view": "Fender Stratocaster guitar side view",
    "top_down": "Fender Stratocaster guitar top-down view",
    "bottom_up": "Fender Stratocaster guitar bottom-up view",
    "45_degree_angle": "Fender Stratocaster guitar 45 degree angle",
    "angled_profile": "Fender Stratocaster guitar angled profile"
}
stratocaster_context_queries = {
    "studio_background": "Fender Stratocaster guitar studio background",
    "on_stage": "Fender Stratocaster guitar on stage",
    "in_concert": "Fender Stratocaster guitar in concert",
    "outdoors": "Fender Stratocaster guitar outdoors",
    "recording_studio": "Fender Stratocaster guitar in recording studio"
}
stratocaster_orientation_queries = {
    "flat_on_table": "Fender Stratocaster guitar flat on table",
    "tilted": "Fender Stratocaster guitar tilted",
    "horizontal_view": "Fender Stratocaster guitar horizontal view",
    "rotated": "Fender Stratocaster guitar rotated"
}
stratocaster_inuse_queries = {
    "player_holding": "Fender Stratocaster guitar player holding",
    "being_played": "Fender Stratocaster guitar being played",
    "live_performance": "Fender Stratocaster guitar live performance",
    "musician_playing": "Fender Stratocaster guitar musician playing"
}

# Scraping images for Fender Jaguar
for specific_name, query in jaguar_angle_queries.items():
    jaguar_images = get_image_urls(query, num_angle_images // len(jaguar_angle_queries))
    save_images(jaguar_images, "fender_jaguar", "fender_jaguar", "angle", specific_name)

for specific_name, query in jaguar_context_queries.items():
    jaguar_images = get_image_urls(query, num_context_images // len(jaguar_context_queries))
    save_images(jaguar_images, "fender_jaguar", "fender_jaguar", "context", specific_name)

for specific_name, query in jaguar_orientation_queries.items():
    jaguar_images = get_image_urls(query, num_orientation_images // len(jaguar_orientation_queries))
    save_images(jaguar_images, "fender_jaguar", "fender_jaguar", "orientation", specific_name)

for specific_name, query in jaguar_inuse_queries.items():
    jaguar_images = get_image_urls(query, num_inuse_images // len(jaguar_inuse_queries))
    save_images(jaguar_images, "fender_jaguar", "fender_jaguar", "inuse", specific_name)

# Scraping images for Fender Telecaster
for specific_name, query in telecaster_angle_queries.items():
    telecaster_images = get_image_urls(query, num_angle_images // len(telecaster_angle_queries))
    save_images(telecaster_images, "fender_telecaster", "fender_telecaster", "angle", specific_name)

for specific_name, query in telecaster_context_queries.items():
    telecaster_images = get_image_urls(query, num_context_images // len(telecaster_context_queries))
    save_images(telecaster_images, "fender_telecaster", "fender_telecaster", "context", specific_name)

for specific_name, query in telecaster_orientation_queries.items():
    telecaster_images = get_image_urls(query, num_orientation_images // len(telecaster_orientation_queries))
    save_images(telecaster_images, "fender_telecaster", "fender_telecaster", "orientation", specific_name)

for specific_name, query in telecaster_inuse_queries.items():
    telecaster_images = get_image_urls(query, num_inuse_images // len(telecaster_inuse_queries))
    save_images(telecaster_images, "fender_telecaster", "fender_telecaster", "inuse", specific_name)

# Scraping images for Fender Stratocaster
for specific_name, query in stratocaster_angle_queries.items():
    stratocaster_images = get_image_urls(query, num_angle_images // len(stratocaster_angle_queries))
    save_images(stratocaster_images, "fender_stratocaster", "fender_stratocaster", "angle", specific_name)

for specific_name, query in stratocaster_context_queries.items():
    stratocaster_images = get_image_urls(query, num_context_images // len(stratocaster_context_queries))
    save_images(stratocaster_images, "fender_stratocaster", "fender_stratocaster", "context", specific_name)

for specific_name, query in stratocaster_orientation_queries.items():
    stratocaster_images = get_image_urls(query, num_orientation_images // len(stratocaster_orientation_queries))
    save_images(stratocaster_images, "fender_stratocaster", "fender_stratocaster", "orientation", specific_name)

for specific_name, query in stratocaster_inuse_queries.items():
    stratocaster_images = get_image_urls(query, num_inuse_images // len(stratocaster_inuse_queries))
    save_images(stratocaster_images, "fender_stratocaster", "fender_stratocaster", "inuse", specific_name)

print("Image scraping complete!")
