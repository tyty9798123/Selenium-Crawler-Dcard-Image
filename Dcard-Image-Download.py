# -*- coding: utf-8 -*-

from selenium import webdriver;
from urllib.request import Request, urlopen


class ArticlesURL:
    def __init__(self, scrollTimes):        
        self.articlesURL = [];
        self.driver = webdriver.Chrome("/Users/user/desktop/chromedriver");
        self.getUrl();
        self.scrollDown(scrollTimes);
        self.findArticlesURL();
        
    def getUrl(self):
        self.driver.get("https://www.dcard.tw/f/");#url
        
    def scrollDown(self, scrollTimes):
        for i in range(0, scrollTimes):
            self.driver.execute_script('window.scrollTo(0,1000000)');
    
    def findArticlesURL(self):
        aTag = self.driver.find_elements_by_class_name("PostEntry_root_V6g0rd");
        for i in aTag:
            self.articlesURL.append(i.get_attribute("href").split("-", 2)[0]);
    
    def getArticlesURL(self):
        return self.articlesURL;
    
    def getDriver(self):
        return self.driver;
    
class Images:
    def __init__(self, urls, driver):
        self.num = 1;
        self.urls = urls;
        self.driver = driver;   
        self.getUrls(self.urls);
    
    def getUrls(self, urls):
        for i in urls:
            self.driver.get(i);
            self.scrollDown();
    
    def scrollDown(self):
        self.driver.execute_script('window.scrollTo(0,1000000)')
        while True:    
            try:
                self.driver.execute_script("document.getElementsByClassName('CommentList_content_1KaR30')[0].click();")
                break;
            except:
                self.driver.execute_script('window.scrollTo(0,1000000)')
        self.getImages();         
    
    def getImages(self):
        #紀錄所有image GalleryImage_image_3lGzO5
        try:
            imgTags = self.driver.find_elements_by_class_name("GalleryImage_image_3lGzO5");
            for i in imgTags:
                print(i.get_attribute("src").split("/",4)[3]);
                self.downloadImages(i.get_attribute("src"), i.get_attribute("src").split("/",4)[3]);
                #downloadzxx
        except:
            None;

    def downloadImages(self, imageUrl, imageName):
        url = imageUrl;
        response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        image = urlopen(response).read()
        with open(imageName, 'wb') as file:
            file.write(image)
        
        self.num+=1
        
if __name__ == '__main__':
    ArticlesURLObj = ArticlesURL(1);
    urls = ArticlesURLObj.getArticlesURL();
    driver = ArticlesURLObj.getDriver();
    Images(urls, driver)
