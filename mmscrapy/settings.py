BOT_NAME = 'mmscrapy'

SPIDER_MODULES = ['mmscrapy.spiders']
NEWSPIDER_MODULE = 'mmscrapy.spiders'

USER_AGENT = 'for_testing_only'
ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 0.2
AUTOTHROTTLE_ENABLED = True

ITEM_PIPELINES = {
  'mmscrapy.pipelines.SaveImagesPipeline': 1
}
FILES_STORE = 'product_images'