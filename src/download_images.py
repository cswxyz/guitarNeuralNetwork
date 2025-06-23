import requests
from bs4 import BeautifulSoup
import os
import time
import logging

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

"""Below is queries for the seven new guitars from fender"""
# Search Queries for Fender Jazzmaster 
jazzmaster_angle_queries = {
    "side_view": "Fender Jazzmaster guitar side view",
    "top_down": "Fender Jazzmaster guitar top-down view",
    "bottom_up": "Fender Jazzmaster guitar bottom-up view",
    "45_degree_angle": "Fender Jazzmaster guitar 45 degree angle",
    "angled_profile": "Fender Jazzmaster guitar angled profile"
}
jazzmaster_context_queries = {
    "studio_background": "Fender Jazzmaster guitar studio background",
    "on_stage": "Fender Jazzmaster guitar on stage",
    "in_concert": "Fender Jazzmaster guitar in concert",
    "outdoors": "Fender Jazzmaster guitar outdoors",
    "recording_studio": "Fender Jazzmaster guitar in recording studio"
}
jazzmaster_orientation_queries = {
    "flat_on_table": "Fender Jazzmaster guitar flat on table",
    "tilted": "Fender Jazzmaster guitar tilted",
    "horizontal_view": "Fender Jazzmaster guitar horizontal view",
    "rotated": "Fender Jazzmaster guitar rotated"
}
jazzmaster_inuse_queries = {
    "player_holding": "Fender Jazzmaster guitar player holding",
    "being_played": "Fender Jazzmaster guitar being played",
    "live_performance": "Fender Jazzmaster guitar live performance",
    "musician_playing": "Fender Jazzmaster guitar musician playing"
}

# Search Queries for Fender Mustang
mustang_angle_queries = {
    "side_view": "Fender Mustang guitar side view",
    "top_down": "Fender Mustang guitar top-down view",
    "bottom_up": "Fender Mustang guitar bottom-up view",
    "45_degree_angle": "Fender Mustang guitar 45 degree angle",
    "angled_profile": "Fender Mustang guitar angled profile"
}
mustang_context_queries = {
    "studio_background": "Fender Mustang guitar studio background",
    "on_stage": "Fender Mustang guitar on stage",
    "in_concert": "Fender Mustang guitar in concert",
    "outdoors": "Fender Mustang guitar outdoors",
    "recording_studio": "Fender Mustang guitar in recording studio"
}
mustang_orientation_queries = {
    "flat_on_table": "Fender Mustang guitar flat on table",
    "tilted": "Fender Mustang guitar tilted",
    "horizontal_view": "Fender Mustang guitar horizontal view",
    "rotated": "Fender Mustang guitar rotated"
}
mustang_inuse_queries = {
    "player_holding": "Fender Mustang guitar player holding",
    "being_played": "Fender Mustang guitar being played",
    "live_performance": "Fender Mustang guitar live performance",
    "musician_playing": "Fender Mustang guitar musician playing"
}

# Search Queries for Fender Duo-Sonic
duosonic_angle_queries = {
    "side_view": "Fender Duo-Sonic guitar side view",
    "top_down": "Fender Duo-Sonic guitar top-down view",
    "bottom_up": "Fender Duo-Sonic guitar bottom-up view",
    "45_degree_angle": "Fender Duo-Sonic guitar 45 degree angle",
    "angled_profile": "Fender Duo-Sonic guitar angled profile"
}
duosonic_context_queries = {
    "studio_background": "Fender Duo-Sonic guitar studio background",
    "on_stage": "Fender Duo-Sonic guitar on stage",
    "in_concert": "Fender Duo-Sonic guitar in concert",
    "outdoors": "Fender Duo-Sonic guitar outdoors",
    "recording_studio": "Fender Duo-Sonic guitar in recording studio"
}
duosonic_orientation_queries = {
    "flat_on_table": "Fender Duo-Sonic guitar flat on table",
    "tilted": "Fender Duo-Sonic guitar tilted",
    "horizontal_view": "Fender Duo-Sonic guitar horizontal view",
    "rotated": "Fender Duo-Sonic guitar rotated"
}
duosonic_inuse_queries = {
    "player_holding": "Fender Duo-Sonic guitar player holding",
    "being_played": "Fender Duo-Sonic guitar being played",
    "live_performance": "Fender Duo-Sonic guitar live performance",
    "musician_playing": "Fender Duo-Sonic guitar musician playing"
}

# Search Queries for Fender Lead II
leadii_angle_queries = {
    "side_view": "Fender Lead II guitar side view",
    "top_down": "Fender Lead II guitar top-down view",
    "bottom_up": "Fender Lead II guitar bottom-up view",
    "45_degree_angle": "Fender Lead II guitar 45 degree angle",
    "angled_profile": "Fender Lead II guitar angled profile"
}
leadii_context_queries = {
    "studio_background": "Fender Lead II guitar studio background",
    "on_stage": "Fender Lead II guitar on stage",
    "in_concert": "Fender Lead II guitar in concert",
    "outdoors": "Fender Lead II guitar outdoors",
    "recording_studio": "Fender Lead II guitar in recording studio"
}
leadii_orientation_queries = {
    "flat_on_table": "Fender Lead II guitar flat on table",
    "tilted": "Fender Lead II guitar tilted",
    "horizontal_view": "Fender Lead II guitar horizontal view",
    "rotated": "Fender Lead II guitar rotated"
}
leadii_inuse_queries = {
    "player_holding": "Fender Lead II guitar player holding",
    "being_played": "Fender Lead II guitar being played",
    "live_performance": "Fender Lead II guitar live performance",
    "musician_playing": "Fender Lead II guitar musician playing"
}

# Search Queries for Fender Toronado
toronado_angle_queries = {
    "side_view": "Fender Toronado guitar side view",
    "top_down": "Fender Toronado guitar top-down view",
    "bottom_up": "Fender Toronado guitar bottom-up view",
    "45_degree_angle": "Fender Toronado guitar 45 degree angle",
    "angled_profile": "Fender Toronado guitar angled profile"
}
toronado_context_queries = {
    "studio_background": "Fender Toronado guitar studio background",
    "on_stage": "Fender Toronado guitar on stage",
    "in_concert": "Fender Toronado guitar in concert",
    "outdoors": "Fender Toronado guitar outdoors",
    "recording_studio": "Fender Toronado guitar in recording studio"
}
toronado_orientation_queries = {
    "flat_on_table": "Fender Toronado guitar flat on table",
    "tilted": "Fender Toronado guitar tilted",
    "horizontal_view": "Fender Toronado guitar horizontal view",
    "rotated": "Fender Toronado guitar rotated"
}
toronado_inuse_queries = {
    "player_holding": "Fender Toronado guitar player holding",
    "being_played": "Fender Toronado guitar being played",
    "live_performance": "Fender Toronado guitar live performance",
    "musician_playing": "Fender Toronado guitar musician playing"
}

# Search Queries for Fender Performer
performer_angle_queries = {
    "side_view": "Fender Performer guitar side view",
    "top_down": "Fender Performer guitar top-down view",
    "bottom_up": "Fender Performer guitar bottom-up view",
    "45_degree_angle": "Fender Performer guitar 45 degree angle",
    "angled_profile": "Fender Performer guitar angled profile"
}
performer_context_queries = {
    "studio_background": "Fender Performer guitar studio background",
    "on_stage": "Fender Performer guitar on stage",
    "in_concert": "Fender Performer guitar in concert",
    "outdoors": "Fender Performer guitar outdoors",
    "recording_studio": "Fender Performer guitar in recording studio"
}
performer_orientation_queries = {
    "flat_on_table": "Fender Performer guitar flat on table",
    "tilted": "Fender Performer guitar tilted",
    "horizontal_view": "Fender Performer guitar horizontal view",
    "rotated": "Fender Performer guitar rotated"
}
performer_inuse_queries = {
    "player_holding": "Fender Performer guitar player holding",
    "being_played": "Fender Performer guitar being played",
    "live_performance": "Fender Performer guitar live performance",
    "musician_playing": "Fender Performer guitar musician playing"
}

# Search Queries for Fender Starcaster
starcaster_angle_queries = {
    "side_view": "Fender Starcaster guitar side view",
    "top_down": "Fender Starcaster guitar top-down view",
    "bottom_up": "Fender Starcaster guitar bottom-up view",
    "45_degree_angle": "Fender Starcaster guitar 45 degree angle",
    "angled_profile": "Fender Starcaster guitar angled profile"
}
starcaster_context_queries = {
    "studio_background": "Fender Starcaster guitar studio background",
    "on_stage": "Fender Starcaster guitar on stage",
    "in_concert": "Fender Starcaster guitar in concert",
    "outdoors": "Fender Starcaster guitar outdoors",
    "recording_studio": "Fender Starcaster guitar in recording studio"
}
starcaster_orientation_queries = {
    "flat_on_table": "Fender Starcaster guitar flat on table",
    "tilted": "Fender Starcaster guitar tilted",
    "horizontal_view": "Fender Starcaster guitar horizontal view",
    "rotated": "Fender Starcaster guitar rotated"
}
starcaster_inuse_queries = {
    "player_holding": "Fender Starcaster guitar player holding",
    "being_played": "Fender Starcaster guitar being played",
    "live_performance": "Fender Starcaster guitar live performance",
    "musician_playing": "Fender Starcaster guitar musician playing"
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

"""Below is for scraping the seven new guitars from fender"""
# Scraping images for Fender Jazzmaster 
for specific_name, query in jazzmaster_angle_queries.items():
    jazzmaster_images = get_image_urls(query, num_angle_images // len(jazzmaster_angle_queries))
    save_images(jazzmaster_images, "fender_jazzmaster", "fender_jazzmaster", "angle", specific_name)

for specific_name, query in jazzmaster_context_queries.items():
    jazzmaster_images = get_image_urls(query, num_context_images // len(jazzmaster_context_queries))
    save_images(jazzmaster_images, "fender_jazzmaster", "fender_jazzmaster", "context", specific_name)

for specific_name, query in jazzmaster_orientation_queries.items():
    jazzmaster_images = get_image_urls(query, num_orientation_images // len(jazzmaster_orientation_queries))
    save_images(jazzmaster_images, "fender_jazzmaster", "fender_jazzmaster", "orientation", specific_name)

for specific_name, query in jazzmaster_inuse_queries.items():
    jazzmaster_images = get_image_urls(query, num_inuse_images // len(jazzmaster_inuse_queries))
    save_images(jazzmaster_images, "fender_jazzmaster", "fender_jazzmaster", "inuse", specific_name)

# Scraping images for Fender Mustang
for specific_name, query in mustang_angle_queries.items():
    mustang_images = get_image_urls(query, num_angle_images // len(mustang_angle_queries))
    save_images(mustang_images, "fender_mustang", "fender_mustang", "angle", specific_name)

for specific_name, query in mustang_context_queries.items():
    mustang_images = get_image_urls(query, num_context_images // len(mustang_context_queries))
    save_images(mustang_images, "fender_mustang", "fender_mustang", "context", specific_name)

for specific_name, query in mustang_orientation_queries.items():
    mustang_images = get_image_urls(query, num_orientation_images // len(mustang_orientation_queries))
    save_images(mustang_images, "fender_mustang", "fender_mustang", "orientation", specific_name)

for specific_name, query in mustang_inuse_queries.items():
    mustang_images = get_image_urls(query, num_inuse_images // len(mustang_inuse_queries))
    save_images(mustang_images, "fender_mustang", "fender_mustang", "inuse", specific_name)

# Scraping images for Fender Duo-Sonic
for specific_name, query in duosonic_angle_queries.items():
    duosonic_images = get_image_urls(query, num_angle_images // len(duosonic_angle_queries))
    save_images(duosonic_images, "fender_duosonic", "fender_duosonic", "angle", specific_name)

for specific_name, query in duosonic_context_queries.items():
    duosonic_images = get_image_urls(query, num_context_images // len(duosonic_context_queries))
    save_images(duosonic_images, "fender_duosonic", "fender_duosonic", "context", specific_name)

for specific_name, query in duosonic_orientation_queries.items():
    duosonic_images = get_image_urls(query, num_orientation_images // len(duosonic_orientation_queries))
    save_images(duosonic_images, "fender_duosonic", "fender_duosonic", "orientation", specific_name)

for specific_name, query in duosonic_inuse_queries.items():
    duosonic_images = get_image_urls(query, num_inuse_images // len(duosonic_inuse_queries))
    save_images(duosonic_images, "fender_duosonic", "fender_duosonic", "inuse", specific_name)

# Scraping images for Fender Lead II
for specific_name, query in leadii_angle_queries.items():
    leadii_images = get_image_urls(query, num_angle_images // len(leadii_angle_queries))
    save_images(leadii_images, "fender_leadii", "fender_leadii", "angle", specific_name)

for specific_name, query in leadii_context_queries.items():
    leadii_images = get_image_urls(query, num_context_images // len(leadii_context_queries))
    save_images(leadii_images, "fender_leadii", "fender_leadii", "context", specific_name)

for specific_name, query in leadii_orientation_queries.items():
    leadii_images = get_image_urls(query, num_orientation_images // len(leadii_orientation_queries))
    save_images(leadii_images, "fender_leadii", "fender_leadii", "orientation", specific_name)

for specific_name, query in leadii_inuse_queries.items():
    leadii_images = get_image_urls(query, num_inuse_images // len(leadii_inuse_queries))
    save_images(leadii_images, "fender_leadii", "fender_leadii", "inuse", specific_name)

# Scraping images for Fender Toronado
for specific_name, query in toronado_angle_queries.items():
    toronado_images = get_image_urls(query, num_angle_images // len(toronado_angle_queries))
    save_images(toronado_images, "fender_toronado", "fender_toronado", "angle", specific_name)

for specific_name, query in toronado_context_queries.items():
    toronado_images = get_image_urls(query, num_context_images // len(toronado_context_queries))
    save_images(toronado_images, "fender_toronado", "fender_toronado", "context", specific_name)

for specific_name, query in toronado_orientation_queries.items():
    toronado_images = get_image_urls(query, num_orientation_images // len(toronado_orientation_queries))
    save_images(toronado_images, "fender_toronado", "fender_toronado", "orientation", specific_name)

for specific_name, query in toronado_inuse_queries.items():
    toronado_images = get_image_urls(query, num_inuse_images // len(toronado_inuse_queries))
    save_images(toronado_images, "fender_toronado", "fender_toronado", "inuse", specific_name)

# Scraping images for Fender Performer
for specific_name, query in performer_angle_queries.items():
    performer_images = get_image_urls(query, num_angle_images // len(performer_angle_queries))
    save_images(performer_images, "fender_performer", "fender_performer", "angle", specific_name)

for specific_name, query in performer_context_queries.items():
    performer_images = get_image_urls(query, num_context_images // len(performer_context_queries))
    save_images(performer_images, "fender_performer", "fender_performer", "context", specific_name)

for specific_name, query in performer_orientation_queries.items():
    performer_images = get_image_urls(query, num_orientation_images // len(performer_orientation_queries))
    save_images(performer_images, "fender_performer", "fender_performer", "orientation", specific_name)

for specific_name, query in performer_inuse_queries.items():
    performer_images = get_image_urls(query, num_inuse_images // len(performer_inuse_queries))
    save_images(performer_images, "fender_performer", "fender_performer", "inuse", specific_name)

# Scraping images for Fender Starcaster
for specific_name, query in starcaster_angle_queries.items():
    starcaster_images = get_image_urls(query, num_angle_images // len(starcaster_angle_queries))
    save_images(starcaster_images, "fender_starcaster", "fender_starcaster", "angle", specific_name)

for specific_name, query in starcaster_context_queries.items():
    starcaster_images = get_image_urls(query, num_context_images // len(starcaster_context_queries))
    save_images(starcaster_images, "fender_starcaster", "fender_starcaster", "context", specific_name)

for specific_name, query in starcaster_orientation_queries.items():
    starcaster_images = get_image_urls(query, num_orientation_images // len(starcaster_orientation_queries))
    save_images(starcaster_images, "fender_starcaster", "fender_starcaster", "orientation", specific_name)

for specific_name, query in starcaster_inuse_queries.items():
    starcaster_images = get_image_urls(query, num_inuse_images // len(starcaster_inuse_queries))
    save_images(starcaster_images, "fender_starcaster", "fender_starcaster", "inuse", specific_name)

print("Image scraping complete!")
