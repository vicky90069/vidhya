import requests
from bs4 import BeautifulSoup
import csv
import os 

base_url = "https://courses.analyticsvidhya.com/collections?page={}"


courses = []

for page_number in range(1, 6):  
   
    url = base_url.format(page_number)

  
    response = requests.get(url)

    
    if response.status_code != 200:
        print(f"Failed to fetch the webpage for page {page_number}. Status code:", response.status_code)
        continue  

    
    soup = BeautifulSoup(response.text, "html.parser")

    
    for course_card in soup.find_all("a", class_="course-card"):
        
        link = "https://courses.analyticsvidhya.com" + course_card["href"]

        title = course_card.find("h3").text.strip()

        
        lessons_tag = course_card.find("span", class_="course-card__lesson-count")
        lessons = lessons_tag.text.strip() if lessons_tag else "No lesson count available"

      
        price_tag = course_card.find("span", class_="course-card__price")
        price = price_tag.text.strip() if price_tag else "No price available"

        
        reviews_tag = course_card.find("span", class_="review__stars-count")
        reviews = reviews_tag.text.strip() if reviews_tag else "No reviews available"

        
        image_tag = course_card.find("img", class_="course-card__img")
        image_url = image_tag["src"] if image_tag else "No image available"

       
        courses.append({
            "title": title,
            "link": link,
            "lessons": lessons,
            "price": price,
            "reviews": reviews,
            "image_url": image_url
        })


csv_file = "courses.csv"


file_exists = os.path.isfile(csv_file)


with open(csv_file, "a", newline="", encoding="utf-8") as csvfile:
    
    fieldnames = ["title", "link", "lessons", "price", "reviews", "image_url"]
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    
    if not file_exists:
        writer.writeheader()
    writer.writerows(courses)


print("Data collected and saved to courses.csv!")
