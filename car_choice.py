from bs4 import BeautifulSoup
import requests
import time
import csv
def find_cars():
    page_number = 1
    header_written = False
    while True:
        url = 'https://www.cars.com/shopping/results/?page_size=20&amp;page=' + str(page_number) + '&amp;KNC=acqgeosem31&amp;aff=acqgeosem31&amp;ag_id=1192970658168163&amp;loc_interest_ms=51139&amp;loc_physical_ms=76450&amp;maximum_distance=30&amp;msclkid=165a94290fe015e28216f1856448fae4&amp;network=o&amp;utm_campaign=Search+-+LA%2Fen+-+NB+-+Generic%2BCity%3ACar%2BRuston_LA&amp;utm_campaign_id=376294964&amp;utm_content=Car+for+Sale+Ruston+%7C+Intent%3AForSale%2BMT%3AExact&amp;utm_medium=cpc&amp;utm_source=bing&amp;utm_term=cars+for+sale+ruston&amp;utm_trusted=TRUE&amp;zip=71270'
        response = requests.get(url)
        if response.status_code == 200  and page_number <=10:

            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')

            vehicles = soup.find_all('div', class_='vehicle-details')

            for vehicle in vehicles:
                status = vehicle.find('p', class_='stock-type')
                car = vehicle.a.h2.text
                access = vehicle.a['href']
                c_access = 'https://www.cars.com/' + access
                mileage = vehicle.find('div', class_='mileage')
                price_con = vehicle.find('div', class_='price-section price-section-vehicle-card')

                # Check if parameters is not None before accessing its properties
                if mileage:
                    mileage = vehicle.find('div', class_='mileage').text
                else:
                    mileage = 'mileage not available'
                if status:
                    status = vehicle.find('p', class_='stock-type').text
                else:
                    status = 'status not available'
                if price_con:
                    price = price_con.find('span', class_='primary-price').text
                else:       #check whether or not price is available
                    pass

                with open('cars.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    
                    if not header_written:
                        csv_writer.writerow(['Car Name', 'Car Status', 'Price', 'Check it out here'])
                        header_written = True
                    
                    csv_writer.writerow([car, status, price, c_access])
            page_number += 1
        else:
            break

if __name__ == '__main__':
    while True:
        find_cars()
        time_wait = 10
        print('waiting', time_wait, 'minutes')
        time.sleep(time_wait * 60)

