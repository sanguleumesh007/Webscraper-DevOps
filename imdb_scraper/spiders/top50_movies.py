import scrapy

class Top50MoviesSpider(scrapy.Spider):
    name = 'top50_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        movies = response.xpath('//td[@class="titleColumn"]/a')
        for movie in movies[:50]:  # Limit to top 50 movies
            movie_page = movie.xpath('@href').get()
            yield response.follow(movie_page, callback=self.parse_movie_details)

    def parse_movie_details(self, response):
        name = response.xpath('//h1/text()').get().strip()
        year = response.xpath('//span[@id="titleYear"]/a/text()').get()
        director = response.xpath('//div[@class="credit_summary_item"][1]/a/text()').get()
        stars = response.xpath('//div[@class="credit_summary_item"][3]//a/text()').getall()
        stars = [star.strip() for star in stars if 'name' in response.urljoin(star)]

        yield {
            'name': name,
            'year': year,
            'director': director,
            'stars': stars
        }
