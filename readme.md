#### Ecommerce scraping test in Scrapy 1.5.0

Main Spider
  - Go through a full category of products with the possibility to go to the next page until all items are scraped
  - In this case the background-image URL is needed and found with regex

Pipelines
  - Download the image from 'file_urls' 
  - Convert image name to the ean code

Settings
  - Added to make the image download work:

    ```
    ITEM_PIPELINES = {
      'mmscrapy.pipelines.SaveImagesPipeline': 1
    }
    FILES_STORE = 'product_images'
    ```

Results in a .csv

    ```
    scrapy crawl mmscraper -o result.csv
    ```