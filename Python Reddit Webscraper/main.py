import crawler 
import reddit_word_cloud
import form

def main():
    crawler_form = form.Form("Crawler Form")
    crawler_form.generate_crawler_info_form()
    crawler_info = crawler_form.get_form_fields()
    crawled_text = crawler.return_crawled_text(
        crawler_info['subreddit'],
        crawler_info['category'],
        crawler_info['title_or_content'],
        int(crawler_info['post_limit'])
    )
    wd_cloud = reddit_word_cloud.generate_cloud(crawled_text)
    reddit_word_cloud.plot_cloud(wd_cloud)

if __name__ == "__main__":
    main()
