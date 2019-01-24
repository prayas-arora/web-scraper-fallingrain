# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:40:32 2019

@author: Prayas
Roll number: 101503171
College: Thapar Institue of Engineering & Technology
Company name: Rivigo
Assignment for the role of internship
Github url: https://github.com/Prayas1997/web-scraper-fallingrain
Output: India.csv in current directory.
"""
import os.path
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup 


def web_scraper(): 
    # the target website	 
    url ='http://www.fallingrain.com/world/IN/'
    
    #open with GET method 
    resp = requests.get(url) 
    
    #http_respone 200 means OK status 
    if resp.status_code==200:
        soup = BeautifulSoup(resp.content,'lxml')
        states_list = soup.find_all('li')
        states_urls=[]
        
        for li in states_list:
            href=li.find('a')
            states_urls.append('http://www.fallingrain.com' + href.get('href'))
        
        for state_url in states_urls:
            print(state_url)
            new_url=[]
            new_url.append(state_url)
            final_df=pd.DataFrame(columns=['Name', 'What', 'Region', 'Country', 'Lat', 'Long', 'Elev ft.', 'Pop est'])
            #Implementing DFS for collecting information
            while len(new_url):
                time.sleep(.1) 
                resp = requests.get(new_url[0])
                new_url.pop(0)
                if resp.status_code==200:
                    soup = BeautifulSoup(resp.content,'lxml')
                    tables = soup.find_all('table')
                    if len(tables)==1:
                        new_table = soup.find_all('table', attrs={'border': "2"})
                        if not new_table:
                            sub_links = soup.find_all('a')
                            urls=[]
                            for link in sub_links:
                                urls.append('http://www.fallingrain.com' + link.get('href'))
                            urls = urls[2:]
                            urls.extend(new_url)
                            new_url = urls
                        else:
                            table = soup.find_all('table', attrs={'border': "2"})    
                            data=[]
                            x=0
                            for i in table:
                                x = i
                            table = x    
                            rows = table.find_all('tr')
                            for row in rows:
                                row_td = row.find_all('td')
                                str_cells = str(row_td)
                                cleantext = BeautifulSoup(str_cells, "lxml").get_text()
                                data.append(cleantext)
                                
                            df1 = pd.DataFrame(data)
                            df1 = df1[0].str.split(',', expand=True)
                            df1[0] = df1[0].str.strip('[')
                        
                            col_labels = table.find_all('th')
                            all_header = []
                            col_str = str(col_labels)
                            cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
                            all_header.append(cleantext2)
                            df2 = pd.DataFrame(all_header)
                            df2 = df2[0].str.split(',', expand=True)
                            df2[0] = df2[0].str.strip('[')
                            
                            frames = [df2, df1]
                            df = pd.concat(frames)
                            df[7] = df[7].str.strip(']')
                            df = df.rename(columns=df.iloc[0])
                            df = df.dropna(axis=0, how='all')
                            df = df.drop(0)
                            if not df.empty:
                                final_df = final_df.append(df, sort = False)
                        
                    elif len(tables)==2:
                        table = tables[1]
                        data=[]
                        rows = table.find_all('tr')
                        for row in rows:
                            row_td = row.find_all('td')
                            str_cells = str(row_td)
                            cleantext = BeautifulSoup(str_cells, "lxml").get_text()
                            data.append(cleantext)
                            
                        df1 = pd.DataFrame(data)
                        df1 = df1[0].str.split(',', expand=True)
                        df1[0] = df1[0].str.strip('[')
                    
                        col_labels = table.find_all('th')
                        all_header = []
                        col_str = str(col_labels)
                        cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
                        all_header.append(cleantext2)
                        df2 = pd.DataFrame(all_header)
                        df2 = df2[0].str.split(',', expand=True)
                        df2[0] = df2[0].str.strip('[')
                        
                        frames = [df2, df1]
                        df = pd.concat(frames)
                        df[7] = df[7].str.strip(']')
                        df = df.rename(columns=df.iloc[0])
                        df = df.dropna(axis=0, how='all')
                        df = df.drop(0)
                        if not df.empty:
                                final_df = final_df.append(df, sort = False)
                        
                    elif len(tables) == 0:
                        sub_links = soup.find_all('a')
                        urls=[]
                        for link in sub_links:
                            urls.append('http://www.fallingrain.com' + link.get('href'))
                        urls = urls[1:]
                        urls.extend(new_url)
                        new_url = urls
                        
                else:
                    print("Error")
            final_df = final_df.dropna(axis=1, how='any')
            final_df = final_df.drop([' What', ' Country'], axis = 1)
            
            final_df.columns = ['City', 'State', 'Latitude', 'Longitude', 'Elevation', 'Estimated Population'] 
            final_df = final_df[['State', 'City', 'Latitude', 'Longitude', 'Elevation', 'Estimated Population']]
            final_df = final_df.dropna(axis=1, how='any')
            
            
            file_exists = os.path.isfile('India.csv')
            with open('India.csv', 'a', encoding="utf-8") as f:
                if not file_exists:
                    final_df.to_csv(f, sep=',', index=None, header=True)
                else:
                    final_df.to_csv(f, sep=',', index=None, header=False)
    else:
        print("Error") 
        
web_scraper() #Calling the web scraper
