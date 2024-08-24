#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('We importing main libraries') 
import numpy as np 
import pandas as pd     
from bs4 import BeautifulSoup as Soup  
from urllib.request import Request , urlopen 
print('Libraries imported') 

Titles_of_pages = []
Articles_in_the_pages = []


# ### We have imported the libraries Numpy used for the Stastical and mathematical calculations , Pandas is imported mainly fro the file handling , BeautifulSoup for Data sourcing and data extaction it is mainly used to make the data in the readible format , urllib.request to request on the Web pages for extracting the data.

# ### I have started updating the Titles and articles of the web pages 
# ### I am doing this to collect the Titles and their Articles at one place or in one csv file after the data extraction process

# ### We have started Data extraction on the links provided in the Input.xlsx one by one for starting websites , and then after the extraction from the 4 to 5 website we . I will start using loops to extract the data.

# In[2]:


my_url = 'https://insights.blackcoffer.com/ml-and-ai-based-insurance-premium-model-to-predict-premium-to-be-charged-by-the-insurance-company/'
my_req = Request(my_url , headers = {'User-Agent' : 'Chrome/121'} )
my_web_page = urlopen(my_req).read() 


# #### We have taken all the data and ther elements in the my_web_page 

# In[3]:


page_soup = Soup(my_web_page)   


# ### In this , page_soup variable we have Beautify the data and store in it

# In[4]:


H1ss = page_soup.find(name = 'h1' , attrs = {'class' : 'entry-title'})  


# ### In H1ss variable it is storing the heading tag with it's data

# In[5]:


H1ss 


# In[6]:


Title1 = H1ss.get_text(strip = True) 


# #### In Title1 we have stored the Heading of the Articles , extracting the data from H1ss variable.

# In[7]:


Paragraphs = page_soup.find_all(name = 'p'  ) 


# #### In the paragraphs variable we get all the tags and texts which are situated using p tag which is in the web page.

# In[8]:


Paragraphs   


# In[9]:


get_para_data = []
for i in Paragraphs:
    get_para_data.append(i.get_text(strip=True)) 
get_para_data


# In[11]:


get_pararagraph_data = []
get_paragraph_data_text = ' '
count = 0 
for i in range( 0, len(get_para_data[20::]) ):
    if get_para_data[i] in 'Summarization':
        print(i) 
for j in range( 0 , len(get_para_data[20::]) ):
    if j < 26:
        get_paragraph_data_text += get_para_data[j]   
print(get_paragraph_data_text)


# In[12]:


get_paragraph_data_text = f'''                       {Title1}\n\n{get_paragraph_data_text}'''  


# In[13]:


print(get_paragraph_data_text) 
Titles_of_pages.append(Title1)
Articles_in_the_pages.append(get_paragraph_data_text)


# In[ ]:


text_file = open(r'C:\Users\Hp\Downloads\New folder\bctech2011.txt','w') 
text_file.write(get_paragraph_data_text) 
text_file.close() 


# ### In above cell we are storing the data into the file names bctech2011 which is extracted from the given website .

# ## This process will run for all the links which is mentioned in the Input.xlsx table .

# In[14]:


my_url2 = 'https://insights.blackcoffer.com/streamlined-integration-interactive-brokers-api-with-python-for-desktop-trading-application/'
my_req2 = Request(my_url2 , headers = {'User-Agent' : 'Chrome/121'} )
my_web_page2 = urlopen(my_req2).read() 


# In[15]:


page_soup2 = Soup(my_web_page2) 


# In[16]:


H2ss = page_soup2.find(name = 'h1' , attrs = {'class' : 'entry-title'})   


# In[17]:


H2ss 


# In[18]:


Title2 = H2ss.get_text(strip = True) 
print(Title2) 


# In[19]:


Ulss = page_soup2.find_all(name = 'li' ) 


# In[20]:


get_paragraph_text2 = ' '
for i in Ulss:
    get_paragraph_text2 += i.get_text(strip=True)


# In[21]:


get_paragraph_text2 = f'                             {Title2}\n\n{get_paragraph_text2}' 
Titles_of_pages.append(Title2)
Articles_in_the_pages.append(get_paragraph_text2)


# In[25]:


text_file2 = open(r'C:\Users\Hp\Downloads\New folder\bctech2012','w')
text_file2.write(get_paragraph_text2) 
text_file2.close() 


# In[22]:


my_url3 = 'https://insights.blackcoffer.com/efficient-data-integration-and-user-friendly-interface-development-navigating-challenges-in-web-application-deployment/'
my_req3 = Request(my_url3 , headers = {'User-Agent' : 'Chrome/121'} )
my_web_page3 = urlopen(my_req3).read()  


# In[23]:


page_soup3 = Soup(my_web_page3) 
H3ss = page_soup3.find(name = 'h1' , attrs = {'class' : 'entry-title'})
Title3 = H3ss.get_text(strip = True) 
print(Title3) 


# In[24]:


Ulss3 = page_soup3.find_all(name = 'li') 
get_paragraph_text3 = ' ' 
for i in Ulss3:
    get_paragraph_text3 += i.get_text(strip = True)  
get_paragraph_text3 = f'                             {Title3}\n\n{get_paragraph_text3}' 


# In[25]:


get_paragraph_text3 
Titles_of_pages.append(Title3)
Articles_in_the_pages.append(get_paragraph_text3)


# In[31]:


text_file3 = open(r'C:\Users\Hp\Downloads\New folder\bctech2013','w') 
text_file3.write(get_paragraph_text3) 
text_file3.close()


# In[26]:


my_url4 = 'https://insights.blackcoffer.com/effective-management-of-social-media-data-extraction-strategies-for-authentication-security-and-reliability/'
my_req4 = Request(my_url4 , headers = {'User-Agent' : 'Chrome/121'} )
my_web_page4 = urlopen(my_req4).read()   


# In[27]:


page_soup4 = Soup(my_web_page4)   


# In[28]:


H4ss = page_soup4.find(name = 'h1' , attrs = {'class' : 'entry-title'})
Title4 = H4ss.get_text(strip = True) 
print(Title4) 


# In[29]:


Ulss4 = page_soup4.find_all(name = 'li' ) 


# In[30]:


get_paragraph_text4 = ' ' 
for i in Ulss4:
    get_paragraph_text4 += i.get_text(strip=True) 
get_paragraph_text4 = f'''         {Title4}\n\n {get_paragraph_text4}'''


# In[32]:


get_paragraph_text4
Titles_of_pages.append(Title4)
Articles_in_the_pages.append(get_paragraph_text4)


# In[50]:


text_file4 = open(r'C:\Users\Hp\Downloads\New folder\bctech2014','w') 
text_file4.write(get_paragraph_text4) 
text_file4.close()


# In[33]:


my_url5 = 'https://insights.blackcoffer.com/streamlined-trading-operations-interface-for-metatrader-4-empowering-efficient-management-and-monitoring/'
my_req5 = Request(my_url5 , headers = {'User-Agent' : 'Chrome/121'} )
my_web_page5 = urlopen(my_req5).read()  

page_soup5 = Soup(my_web_page5) 



H5ss = page_soup5.find(name = 'h1' , attrs = {'class' : 'entry-title'})
Title5 = H5ss.get_text(strip = True) 
print(Title5) 


# In[34]:


Ul5ss = page_soup5.find_all(name = 'li')
get_paragraph_text5 = ' '
for i in Ul5ss:
    get_paragraph_text5 += i.get_text(strip = True) 
get_paragraph_text5 = f'''       {Title5}\n\n{get_paragraph_text5}'''


# In[35]:


print(get_paragraph_text5)
Titles_of_pages.append(Title5) 
Articles_in_the_pages.append(get_paragraph_text5)


# In[10]:


df_excel = pd.read_excel(r"C:\Users\Hp\Downloads\New folder\Input.xlsx", sheet_name = 'Sheet1')     
len(df_excel)


# #### In the above cell we have imported the dataset known as Input.xlsx in which all the links and URL_IDs are mentioned 

# In[37]:


get_paragraph_texts5 = []
import time
for i in df_excel['URL'][6:12]:
    time.sleep(10)
    my_urls = i 
    my_request = Request(my_urls , headers = {'User-Agent' : 'Chrome/121'} )
    my_web_pages = urlopen(my_request).read() 
    page_soups = Soup(my_web_pages)
    
    Headings = page_soups.find(name = 'h1' , attrs = {'Class' , 'entry-title'}) 
    
    Titles = Headings.get_text(strip = True) 
    
    Ulsss = page_soups.find_all(name = 'li') 
    
    get_paragraphs_text = ' '
    
    for j in Ulsss:
        get_paragraphs_text += j.get_text(strip = True) 
        
    get_paragraphs_text = f'''     {Titles}\n\n{get_paragraphs_text}''' 
    
    get_paragraph_texts5.append(get_paragraphs_text) 
    
    Titles_of_pages.append(Titles)
    Articles_in_the_pages.append(get_paragraphs_text)
    print(Titles)


# ## We have extracted the data from the different websited using for loop

# In[45]:


text_file5 = open(r'C:\Users\Hp\Downloads\New folder\bctech2015','w') 
text_file5.write(get_paragraph_texts5[0]) 
text_file5.close()


# In[46]:


text_file6 = open(r'C:\Users\Hp\Downloads\New folder\bctech2016','w') 
text_file6.write(get_paragraph_texts5[1]) 
text_file6.close()


# In[47]:


text_file7 = open(r'C:\Users\Hp\Downloads\New folder\bctech2017','w') 
text_file7.write(get_paragraph_texts5[2]) 
text_file7.close()


# In[48]:


text_file8 = open(r'C:\Users\Hp\Downloads\New folder\bctech2018','w') 
text_file8.write(get_paragraph_texts5[3]) 
text_file8.close()


# In[49]:


text_file9 = open(r'C:\Users\Hp\Downloads\New folder\bctech2019','w') 
text_file9.write(get_paragraph_texts5[4]) 
text_file9.close()


# In[50]:


text_file10 = open(r'C:\Users\Hp\Downloads\New folder\bctech2020','w') 
text_file10.write(get_paragraph_texts5[5]) 
text_file10.close()


# In[37]:


len(get_paragraph_texts5) 


# In[38]:


get_paragraph_texts10 = []
import time
for i in df_excel['URL'][11:23]:
    time.sleep(6)
    my_urls = i 
    my_request = Request(my_urls , headers = {'User-Agent' : 'Chrome/121'} )
    my_web_pages = urlopen(my_request).read() 
    page_soups = Soup(my_web_pages)
    
    Headings = page_soups.find(name = 'h1' , attrs = {'Class' , 'entry-title'}) 
    
    Titles = Headings.get_text(strip = True) 
    
    Ulsss = page_soups.find_all(name = 'li') 
     
    Parass = page_soups.find_all(name = 'p')  
    
    Ulssss = Ulsss + Parass 
    
    get_paragraphs_text = ' '
    
    for j in Ulssss:
        get_paragraphs_text += j.get_text(strip = True) 
        
    get_paragraphs_text = f'''     {Titles}\n\n{get_paragraphs_text}''' 
    
    get_paragraph_texts10.append(get_paragraphs_text) 
    
    Titles_of_pages.append(Titles)    
    Articles_in_the_pages.append(get_paragraphs_text)
    
    print(Titles)


# In[53]:


text_file11 = open(r'C:\Users\Hp\Downloads\New folder\bctech2022','w') 
text_file11.write(get_paragraph_texts10[0])  
text_file11.close()


# In[54]:


text_file12 = open(r'C:\Users\Hp\Downloads\New folder\bctech2023','w') 
text_file12.write(get_paragraph_texts10[1]) 
text_file12.close()


# In[55]:


text_file13 = open(r'C:\Users\Hp\Downloads\New folder\bctech2024','w') 
text_file13.write(get_paragraph_texts10[2]) 
text_file13.close()


# In[56]:


text_file14 = open(r'C:\Users\Hp\Downloads\New folder\bctech2025','w') 
text_file14.write(get_paragraph_texts10[3]) 
text_file14.close()


# In[57]:


text_file15 = open(r'C:\Users\Hp\Downloads\New folder\bctech2026','w') 
text_file15.write(get_paragraph_texts10[4]) 
text_file15.close()


# In[58]:


text_file16 = open(r'C:\Users\Hp\Downloads\New folder\bctech2027','w') 
text_file16.write(get_paragraph_texts10[5]) 
text_file16.close()


# In[59]:


text_file17 = open(r'C:\Users\Hp\Downloads\New folder\bctech2028','w') 
text_file17.write(get_paragraph_texts10[6]) 
text_file17.close()


# In[60]:


text_file18 = open(r'C:\Users\Hp\Downloads\New folder\bctech2029','w') 
text_file18.write(get_paragraph_texts10[7]) 
text_file18.close()


# In[61]:


text_file19 = open(r'C:\Users\Hp\Downloads\New folder\bctech2030','w') 
text_file19.write(get_paragraph_texts10[8]) 
text_file19.close()


# In[62]:


text_file20 = open(r'C:\Users\Hp\Downloads\New folder\bctech2031','w') 
text_file20.write(get_paragraph_texts10[9]) 
text_file20.close() 


# In[39]:


my_url32 = 'https://insights.blackcoffer.com/gpt-ocr-api/'
my_req32 = Request(my_url32 , headers = {'User-Agent' : 'Chrome/121'} )
my_web_page32 = urlopen(my_req32).read()  


# In[40]:


page_soup32 = Soup(my_web_page32)   


# In[41]:


Headings32 = page_soup32.find(name = 'h1' , attrs = {'Class' , 'entry-title'}) 


# In[42]:


Title32 = Headings32.get_text(strip = 32)  


# In[43]:


paragraphs32 = page_soup32.find_all(name = 'p')


# In[44]:


olss32 = page_soup32.find_all(name = 'ol') 


# In[45]:


Texts = paragraphs32 + olss32 
get_paragraph_text32 = ' '
for i in Texts:
    get_paragraph_text32 += i.get_text(strip = True) 
get_paragraph_text32 = f'''                                                   {Title32}\n\n{get_paragraph_text32}''' 
print(get_paragraph_text32)


# In[46]:


Titles_of_pages.append(Title32)
Articles_in_the_pages.append(get_paragraph_text32)
    


# In[88]:


text_file32 = open(r'C:\Users\Hp\Downloads\New folder\bctech2032','w')
text_file32.write(get_paragraph_text32) 
text_file32.close()


# In[47]:


get_paragraph_texts20 = []
import time  
for i in df_excel['URL'][22:40]:
    time.sleep(6)
    my_urls = i 
    my_request = Request(my_urls , headers = {'User-Agent' : 'Chrome/121'} )
    my_web_pages = urlopen(my_request).read() 
    page_soups = Soup(my_web_pages)
    
    Headings = page_soups.find(name = 'h1' , attrs = {'Class' , 'entry-title'}) 
    
    Titles = Headings.get_text(strip = True) 
    
    Ulsss = page_soups.find_all(name = 'li') 
     
    Parass = page_soups.find_all(name = 'p')  
    
    Ulssss = Ulsss + Parass 
    
    get_paragraphs_text = ' '
    
    for j in Ulssss:
        get_paragraphs_text += j.get_text(strip = True) 
        
    get_paragraphs_text = f'''     {Titles}\n\n{get_paragraphs_text}''' 
    
    get_paragraph_texts20.append(get_paragraphs_text) 
    
    Titles_of_pages.append(Titles)    
    Articles_in_the_pages.append(get_paragraphs_text)
    
    
    print(Titles)


# In[95]:


text_file33 = open(r'C:\Users\Hp\Downloads\New folder\bctech2033','w')
text_file33.write(get_paragraph_texts20[0]) 
text_file33.close()


# In[96]:


text_file34 = open(r'C:\Users\Hp\Downloads\New folder\bctech2034','w')
text_file34.write(get_paragraph_texts20[1]) 
text_file34.close()


# In[97]:


text_file35 = open(r'C:\Users\Hp\Downloads\New folder\bctech2035','w')
text_file35.write(get_paragraph_texts20[2]) 
text_file35.close()


# In[98]:


text_file36 = open(r'C:\Users\Hp\Downloads\New folder\bctech2036','w')
text_file36.write(get_paragraph_texts20[3]) 
text_file36.close()


# In[99]:


text_file37 = open(r'C:\Users\Hp\Downloads\New folder\bctech2037','w')
text_file37.write(get_paragraph_texts20[4]) 
text_file37.close()


# In[100]:


text_file38 = open(r'C:\Users\Hp\Downloads\New folder\bctech2038','w')
text_file38.write(get_paragraph_texts20[5]) 
text_file38.close()


# In[101]:


text_file39 = open(r'C:\Users\Hp\Downloads\New folder\bctech2039','w')
text_file39.write(get_paragraph_texts20[6]) 
text_file39.close()


# In[102]:


text_file40 = open(r'C:\Users\Hp\Downloads\New folder\bctech2040','w')
text_file40.write(get_paragraph_texts20[7]) 
text_file40.close()


# In[103]:


text_file41 = open(r'C:\Users\Hp\Downloads\New folder\bctech2041','w')
text_file41.write(get_paragraph_texts20[8]) 
text_file41.close()


# In[104]:


text_file42 = open(r'C:\Users\Hp\Downloads\New folder\bctech2042','w')
text_file42.write(get_paragraph_texts20[9]) 
text_file42.close()


# In[105]:


text_file43 = open(r'C:\Users\Hp\Downloads\New folder\bctech2043','w')
text_file43.write(get_paragraph_texts20[10]) 
text_file43.close()


# In[106]:


text_file44 = open(r'C:\Users\Hp\Downloads\New folder\bctech2044','w')
text_file44.write(get_paragraph_texts20[11]) 
text_file44.close()


# In[108]:


text_file46 = open(r'C:\Users\Hp\Downloads\New folder\bctech2046','w')
text_file46.write(get_paragraph_texts20[13]) 
text_file46.close()


# In[109]:


text_file47 = open(r'C:\Users\Hp\Downloads\New folder\bctech2047','w')
text_file47.write(get_paragraph_texts20[14]) 
text_file47.close()


# In[110]:


text_file48 = open(r'C:\Users\Hp\Downloads\New folder\bctech2048','w')
text_file48.write(get_paragraph_texts20[15]) 
text_file48.close()


# In[111]:


text_file49 = open(r'C:\Users\Hp\Downloads\New folder\bctech2049','w')
text_file49.write(get_paragraph_texts20[16]) 
text_file49.close()


# In[112]:


text_file50 = open(r'C:\Users\Hp\Downloads\New folder\bctech2050','w')
text_file50.write(get_paragraph_texts20[17]) 
text_file50.close()


# In[ ]:


get_paragraph_texts20[12]


# In[ ]:


my_url45 = 'https://insights.blackcoffer.com/ner-task-using-bert-with-data-in-xml-format/'
my_req45 = Request(my_url45 , headers = {'User-Agent' : 'Chrome/121'} )
my_web_page45 = urlopen(my_req45).read()  


# In[ ]:


page_soup45 = Soup(my_web_page45)  


# In[ ]:


Paragraphs45 = page_soup45.find_all(name = 'p')  


# In[ ]:


get_paragraph_text45 = ' '
for i in Paragraphs45:
    get_paragraph_text45 += i.get_text(strip=True) 
print(get_paragraph_text45)


# In[ ]:


Title45 = page_soup45.find(name = 'h1' , attrs = {'Class' , 'entry-title'}).get_text(strip = True)  
print(Title45)


# In[ ]:


get_paragraph_text45 = f'''        {Title45} 
{get_paragraph_text45}'''


# In[ ]:


get_paragraph_text45


# In[172]:


text_file45 = open(r'C:\Users\Hp\Downloads\New folder\bctech2045','w' , encoding="utf-8")
text_file45.write(get_paragraph_text45) 
text_file45.close()


# In[ ]:


for i in df_excel['URL'][40:70]:
    print(i)


# In[48]:


get_paragraph_texts25 = []
import time
for i in df_excel['URL'][40:70]: 
    time.sleep(6)
    my_urls = i 
    my_request = Request(my_urls , headers = {'User-Agent' : 'Chrome/121'} )
    my_web_pages = urlopen(my_request).read() 
    page_soups = Soup(my_web_pages)
    
    Headings = page_soups.find(name = 'h1' , attrs = {'Class' , 'entry-title'}) 
    
    Titles = Headings.get_text(strip = True) 
    
    Ulsss = page_soups.find_all(name = 'li') 
     
    Parass = page_soups.find_all(name = 'p')  
    
    Ulssss = Ulsss + Parass 
    
    get_paragraphs_text = ' '
    
    for j in Ulssss:
        get_paragraphs_text += j.get_text(strip = True) 
        
    get_paragraphs_text = f'''     {Titles}\n\n{get_paragraphs_text}''' 
    
    get_paragraph_texts25.append(get_paragraphs_text) 
    
    Titles_of_pages.append(Titles)    
    Articles_in_the_pages.append(get_paragraphs_text)
    
    
    print(Titles)


# In[176]:


text_file51 = open(r'C:\Users\Hp\Downloads\New folder\bctech2051','w')
text_file51.write(get_paragraph_texts25[0]) 
text_file51.close()


# In[206]:


text_file52 = open(r'C:\Users\Hp\Downloads\New folder\bctech2052','w' , encoding = 'utf-8')
text_file52.write(get_paragraph_texts25[1]) 
text_file52.close()


# In[207]:


text_file53 = open(r'C:\Users\Hp\Downloads\New folder\bctech2053','w' , encoding = 'utf-8') 
text_file53.write(get_paragraph_texts25[2]) 
text_file53.close()


# In[179]:


text_file54 = open(r'C:\Users\Hp\Downloads\New folder\bctech2054','w')
text_file54.write(get_paragraph_texts25[3]) 
text_file54.close()


# In[208]:


text_file55 = open(r'C:\Users\Hp\Downloads\New folder\bctech2055','w' , encoding = 'utf-8')
text_file55.write(get_paragraph_texts25[4]) 
text_file55.close()


# In[181]:


text_file56 = open(r'C:\Users\Hp\Downloads\New folder\bctech2056','w')
text_file56.write(get_paragraph_texts25[5]) 
text_file56.close()


# In[182]:


text_file57 = open(r'C:\Users\Hp\Downloads\New folder\bctech2057','w')
text_file57.write(get_paragraph_texts25[6]) 
text_file57.close()


# In[183]:


text_file58 = open(r'C:\Users\Hp\Downloads\New folder\bctech2058','w')
text_file58.write(get_paragraph_texts25[7]) 
text_file58.close()


# In[184]:


text_file59 = open(r'C:\Users\Hp\Downloads\New folder\bctech2059','w')
text_file59.write(get_paragraph_texts25[8]) 
text_file59.close()


# In[185]:


text_file60 = open(r'C:\Users\Hp\Downloads\New folder\bctech2060','w')
text_file60.write(get_paragraph_texts25[9]) 
text_file60.close()


# In[186]:


text_file61 = open(r'C:\Users\Hp\Downloads\New folder\bctech2061','w')
text_file61.write(get_paragraph_texts25[10]) 
text_file61.close()


# In[187]:


text_file62 = open(r'C:\Users\Hp\Downloads\New folder\bctech2062','w')
text_file62.write(get_paragraph_texts25[11]) 
text_file62.close()


# In[188]:


text_file63 = open(r'C:\Users\Hp\Downloads\New folder\bctech2063','w')
text_file63.write(get_paragraph_texts25[12]) 
text_file63.close()


# In[189]:


text_file64 = open(r'C:\Users\Hp\Downloads\New folder\bctech2064','w')
text_file64.write(get_paragraph_texts25[13]) 
text_file64.close()


# In[190]:


text_file65 = open(r'C:\Users\Hp\Downloads\New folder\bctech2065','w')
text_file65.write(get_paragraph_texts25[14]) 
text_file65.close()


# In[191]:


text_file66 = open(r'C:\Users\Hp\Downloads\New folder\bctech2066','w')
text_file66.write(get_paragraph_texts25[15]) 
text_file66.close()


# In[192]:


text_file67 = open(r'C:\Users\Hp\Downloads\New folder\bctech2067','w')
text_file67.write(get_paragraph_texts25[16]) 
text_file67.close()


# In[193]:


text_file68 = open(r'C:\Users\Hp\Downloads\New folder\bctech2068','w')
text_file68.write(get_paragraph_texts25[17]) 
text_file68.close()


# In[194]:


text_file69 = open(r'C:\Users\Hp\Downloads\New folder\bctech2069','w')
text_file69.write(get_paragraph_texts25[18])  
text_file69.close()


# In[195]:


text_file70 = open(r'C:\Users\Hp\Downloads\New folder\bctech2070','w')
text_file70.write(get_paragraph_texts25[19]) 
text_file70.close()


# In[196]:


text_file71 = open(r'C:\Users\Hp\Downloads\New folder\bctech2071','w')
text_file71.write(get_paragraph_texts25[20]) 
text_file71.close()


# In[197]:


text_file72 = open(r'C:\Users\Hp\Downloads\New folder\bctech2072','w')
text_file72.write(get_paragraph_texts25[21]) 
text_file72.close()


# In[210]:


text_file73 = open(r'C:\Users\Hp\Downloads\New folder\bctech2073','w' , encoding = 'utf-8')
text_file73.write(get_paragraph_texts25[22]) 
text_file73.close()


# In[199]:


text_file74 = open(r'C:\Users\Hp\Downloads\New folder\bctech2074','w')
text_file74.write(get_paragraph_texts25[23]) 
text_file74.close()


# In[200]:


text_file75 = open(r'C:\Users\Hp\Downloads\New folder\bctech2075','w')
text_file75.write(get_paragraph_texts25[24]) 
text_file75.close()


# In[201]:


text_file76 = open(r'C:\Users\Hp\Downloads\New folder\bctech2076','w')
text_file76.write(get_paragraph_texts25[25]) 
text_file76.close()


# In[202]:


text_file77 = open(r'C:\Users\Hp\Downloads\New folder\bctech2077','w')
text_file77.write(get_paragraph_texts25[26]) 
text_file77.close()


# In[203]:


text_file78 = open(r'C:\Users\Hp\Downloads\New folder\bctech2078','w')
text_file78.write(get_paragraph_texts25[27]) 
text_file78.close()


# In[204]:


text_file79 = open(r'C:\Users\Hp\Downloads\New folder\bctech2079','w')
text_file79.write(get_paragraph_texts25[28]) 
text_file79.close()


# In[205]:


text_file80 = open(r'C:\Users\Hp\Downloads\New folder\bctech2080','w')
text_file80.write(get_paragraph_texts25[29]) 
text_file80.close()


# In[7]:


df_excel['URL'][70:len(df_excel)]


# In[49]:


get_paragraph_texts30 = []
import time
for i in df_excel['URL'][70:len(df_excel)]:
    time.sleep(4)
    my_urls = i 
    my_request = Request(my_urls , headers = {'User-Agent' : 'Chrome/121'} )
    my_web_pages = urlopen(my_request).read() 
    page_soups = Soup(my_web_pages)
    
    Headings = page_soups.find(name = 'h1' , attrs = {'Class' , 'entry-title'}) 
    
    Titles = Headings.get_text(strip = True) 
    
    Ulsss = page_soups.find_all(name = 'li') 
     
    Parass = page_soups.find_all(name = 'p')  
    
    Ulssss = Ulsss + Parass 
    
    get_paragraphs_text = ' '
    
    for j in Ulssss:
        get_paragraphs_text += j.get_text(strip = True) 
        
    get_paragraphs_text = f'''     {Titles}\n\n{get_paragraphs_text}''' 
    
    get_paragraph_texts30.append(get_paragraphs_text) 
    
    Titles_of_pages.append(Titles)    
    Articles_in_the_pages.append(get_paragraphs_text)
    
    
    print(Titles)


# In[14]:


text_file81 = open(r'C:\Users\Hp\Downloads\New folder\bctech2081','w')
text_file81.write(get_paragraph_texts30[0]) 
text_file81.close()  

text_file82 = open(r'C:\Users\Hp\Downloads\New folder\bctech2082','w')
text_file82.write(get_paragraph_texts30[1]) 
text_file82.close()  

text_file83 = open(r'C:\Users\Hp\Downloads\New folder\bctech2083','w')
text_file83.write(get_paragraph_texts30[2]) 
text_file83.close()  

text_file84 = open(r'C:\Users\Hp\Downloads\New folder\bctech2084','w')
text_file84.write(get_paragraph_texts30[3]) 
text_file84.close()  


text_file85 = open(r'C:\Users\Hp\Downloads\New folder\bctech2085','w')
text_file85.write(get_paragraph_texts30[4]) 
text_file85.close()  

text_file86 = open(r'C:\Users\Hp\Downloads\New folder\bctech2086','w')
text_file86.write(get_paragraph_texts30[5]) 
text_file86.close()  



text_file87 = open(r'C:\Users\Hp\Downloads\New folder\bctech2087','w')
text_file87.write(get_paragraph_texts30[6]) 
text_file87.close()  



text_file88 = open(r'C:\Users\Hp\Downloads\New folder\bctech2088','w')
text_file88.write(get_paragraph_texts30[7]) 
text_file88.close()  



text_file89 = open(r'C:\Users\Hp\Downloads\New folder\bctech2089','w')
text_file89.write(get_paragraph_texts30[8]) 
text_file89.close()  



text_file90 = open(r'C:\Users\Hp\Downloads\New folder\bctech2090','w')
text_file90.write(get_paragraph_texts30[9]) 
text_file90.close()  



text_file91 = open(r'C:\Users\Hp\Downloads\New folder\bctech2091','w')
text_file91.write(get_paragraph_texts30[10]) 
text_file91.close() 


text_file92 = open(r'C:\Users\Hp\Downloads\New folder\bctech2092','w')
text_file92.write(get_paragraph_texts30[11]) 
text_file92.close()  


text_file93 = open(r'C:\Users\Hp\Downloads\New folder\bctech2093','w')
text_file93.write(get_paragraph_texts30[12]) 
text_file93.close()  

text_file94 = open(r'C:\Users\Hp\Downloads\New folder\bctech2094','w')
text_file94.write(get_paragraph_texts30[13]) 
text_file94.close()  

text_file95 = open(r'C:\Users\Hp\Downloads\New folder\bctech2095','w')
text_file95.write(get_paragraph_texts30[14]) 
text_file95.close()  

text_file96 = open(r'C:\Users\Hp\Downloads\New folder\bctech2096','w')
text_file96.write(get_paragraph_texts30[15]) 
text_file96.close()  

text_file97 = open(r'C:\Users\Hp\Downloads\New folder\bctech2097','w')
text_file97.write(get_paragraph_texts30[16]) 
text_file97.close()  

text_file98 = open(r'C:\Users\Hp\Downloads\New folder\bctech2098','w')
text_file98.write(get_paragraph_texts30[17]) 
text_file98.close()  


text_file99 = open(r'C:\Users\Hp\Downloads\New folder\bctech2099','w')
text_file99.write(get_paragraph_texts30[18]) 
text_file99.close()  

text_file100 = open(r'C:\Users\Hp\Downloads\New folder\bctech20100','w')
text_file100.write(get_paragraph_texts30[19]) 
text_file100.close()  

text_file101 = open(r'C:\Users\Hp\Downloads\New folder\bctech20101','w')
text_file101.write(get_paragraph_texts30[20]) 
text_file101.close()  


text_file102 = open(r'C:\Users\Hp\Downloads\New folder\bctech20102','w')
text_file102.write(get_paragraph_texts30[21]) 
text_file102.close()  


text_file103 = open(r'C:\Users\Hp\Downloads\New folder\bctech20103','w')
text_file103.write(get_paragraph_texts30[22]) 
text_file103.close()  


text_file104 = open(r'C:\Users\Hp\Downloads\New folder\bctech20104','w')
text_file104.write(get_paragraph_texts30[23]) 
text_file104.close()  


text_file105 = open(r'C:\Users\Hp\Downloads\New folder\bctech20105','w')
text_file105.write(get_paragraph_texts30[24]) 
text_file105.close()  

text_file106 = open(r'C:\Users\Hp\Downloads\New folder\bctech20106','w')
text_file106.write(get_paragraph_texts30[25]) 
text_file106.close()  

text_file107 = open(r'C:\Users\Hp\Downloads\New folder\bctech20107','w')
text_file107.write(get_paragraph_texts30[26]) 
text_file107.close()  

text_file108 = open(r'C:\Users\Hp\Downloads\New folder\bctech20108','w')
text_file108.write(get_paragraph_texts30[27]) 
text_file108.close()  


text_file109 = open(r'C:\Users\Hp\Downloads\New folder\bctech20109','w')
text_file109.write(get_paragraph_texts30[28]) 
text_file109.close()  


text_file110 = open(r'C:\Users\Hp\Downloads\New folder\bctech20110','w')
text_file110.write(get_paragraph_texts30[29]) 
text_file110.close()  

text_file111 = open(r'C:\Users\Hp\Downloads\New folder\bctech20111','w')
text_file111.write(get_paragraph_texts30[30]) 
text_file111.close()  

text_file112 = open(r'C:\Users\Hp\Downloads\New folder\bctech20112','w')
text_file112.write(get_paragraph_texts30[31]) 
text_file112.close()  

text_file113 = open(r'C:\Users\Hp\Downloads\New folder\bctech20113','w')
text_file113.write(get_paragraph_texts30[32]) 
text_file113.close()  

text_file114 = open(r'C:\Users\Hp\Downloads\New folder\bctech20114','w')
text_file114.write(get_paragraph_texts30[33]) 
text_file114.close()  

text_file115 = open(r'C:\Users\Hp\Downloads\New folder\bctech20115','w')
text_file115.write(get_paragraph_texts30[34]) 
text_file115.close()  

text_file116 = open(r'C:\Users\Hp\Downloads\New folder\bctech20116','w')
text_file116.write(get_paragraph_texts30[35]) 
text_file116.close()  

text_file117 = open(r'C:\Users\Hp\Downloads\New folder\bctech20117','w')
text_file117.write(get_paragraph_texts30[36]) 
text_file117.close()  

text_file118 = open(r'C:\Users\Hp\Downloads\New folder\bctech20118','w')
text_file118.write(get_paragraph_texts30[37]) 
text_file118.close()  

text_file119 = open(r'C:\Users\Hp\Downloads\New folder\bctech20119','w')
text_file119.write(get_paragraph_texts30[38]) 
text_file119.close()  

text_file120 = open(r'C:\Users\Hp\Downloads\New folder\bctech20120','w')
text_file120.write(get_paragraph_texts30[39]) 
text_file120.close()  


text_file121 = open(r'C:\Users\Hp\Downloads\New folder\bctech20121','w' , encoding = 'utf-8')
text_file121.write(get_paragraph_texts30[40]) 
text_file121.close()  

text_file122 = open(r'C:\Users\Hp\Downloads\New folder\bctech20122','w')
text_file122.write(get_paragraph_texts30[41]) 
text_file122.close()  

text_file123 = open(r'C:\Users\Hp\Downloads\New folder\bctech20123','w')
text_file123.write(get_paragraph_texts30[42]) 
text_file123.close()  


text_file124 = open(r'C:\Users\Hp\Downloads\New folder\bctech20124','w')
text_file124.write(get_paragraph_texts30[43]) 
text_file124.close()  

text_file125 = open(r'C:\Users\Hp\Downloads\New folder\bctech20125','w')
text_file125.write(get_paragraph_texts30[44]) 
text_file125.close()  

text_file126 = open(r'C:\Users\Hp\Downloads\New folder\bctech20126','w')
text_file126.write(get_paragraph_texts30[45]) 
text_file126.close()  

text_file127 = open(r'C:\Users\Hp\Downloads\New folder\bctech20127','w')
text_file127.write(get_paragraph_texts30[46]) 
text_file127.close()  

text_file128 = open(r'C:\Users\Hp\Downloads\New folder\bctech20128','w')
text_file128.write(get_paragraph_texts30[47]) 
text_file128.close()  

text_file129 = open(r'C:\Users\Hp\Downloads\New folder\bctech20129','w')
text_file129.write(get_paragraph_texts30[48]) 
text_file129.close()  

text_file130 = open(r'C:\Users\Hp\Downloads\New folder\bctech20130','w')
text_file130.write(get_paragraph_texts30[49]) 
text_file130.close()  

text_file131 = open(r'C:\Users\Hp\Downloads\New folder\bctech20131','w')
text_file131.write(get_paragraph_texts30[50]) 
text_file131.close()  

text_file132 = open(r'C:\Users\Hp\Downloads\New folder\bctech20132','w')
text_file132.write(get_paragraph_texts30[51]) 
text_file132.close()  

text_file133 = open(r'C:\Users\Hp\Downloads\New folder\bctech20133','w')
text_file133.write(get_paragraph_texts30[52]) 
text_file133.close()  

text_file134 = open(r'C:\Users\Hp\Downloads\New folder\bctech20134','w')
text_file134.write(get_paragraph_texts30[53]) 
text_file134.close()  

text_file135 = open(r'C:\Users\Hp\Downloads\New folder\bctech20135','w')
text_file135.write(get_paragraph_texts30[53]) 
text_file135.close()  

text_file136 = open(r'C:\Users\Hp\Downloads\New folder\bctech20136','w')
text_file136.write(get_paragraph_texts30[54]) 
text_file136.close()  

text_file137 = open(r'C:\Users\Hp\Downloads\New folder\bctech20137','w')
text_file137.write(get_paragraph_texts30[55]) 
text_file137.close()  

text_file138 = open(r'C:\Users\Hp\Downloads\New folder\bctech20138','w')
text_file138.write(get_paragraph_texts30[56]) 
text_file138.close()  

text_file139 = open(r'C:\Users\Hp\Downloads\New folder\bctech20139','w')
text_file139.write(get_paragraph_texts30[57]) 
text_file139.close()  

text_file140 = open(r'C:\Users\Hp\Downloads\New folder\bctech20140','w')
text_file140.write(get_paragraph_texts30[58]) 
text_file140.close()  


text_file141 = open(r'C:\Users\Hp\Downloads\New folder\bctech20141','w')
text_file141.write(get_paragraph_texts30[59]) 
text_file141.close()  

text_file142 = open(r'C:\Users\Hp\Downloads\New folder\bctech20142','w')
text_file142.write(get_paragraph_texts30[60]) 
text_file142.close()  

text_file143 = open(r'C:\Users\Hp\Downloads\New folder\bctech20143','w')
text_file143.write(get_paragraph_texts30[61]) 
text_file143.close()  

text_file144 = open(r'C:\Users\Hp\Downloads\New folder\bctech20144','w')
text_file144.write(get_paragraph_texts30[62]) 
text_file144.close()  

text_file145 = open(r'C:\Users\Hp\Downloads\New folder\bctech20145','w')
text_file145.write(get_paragraph_texts30[63]) 
text_file145.close()  

text_file146 = open(r'C:\Users\Hp\Downloads\New folder\bctech20146','w')
text_file146.write(get_paragraph_texts30[64]) 
text_file146.close()  

text_file147 = open(r'C:\Users\Hp\Downloads\New folder\bctech20147','w')
text_file147.write(get_paragraph_texts30[65]) 
text_file147.close()  

text_file148 = open(r'C:\Users\Hp\Downloads\New folder\bctech20148','w')
text_file148.write(get_paragraph_texts30[66]) 
text_file148.close()  

text_file149 = open(r'C:\Users\Hp\Downloads\New folder\bctech20149','w')
text_file149.write(get_paragraph_texts30[67]) 
text_file149.close()  

text_file150 = open(r'C:\Users\Hp\Downloads\New folder\bctech20150','w')
text_file150.write(get_paragraph_texts30[68]) 
text_file150.close()  

text_file151 = open(r'C:\Users\Hp\Downloads\New folder\bctech20151','w')
text_file151.write(get_paragraph_texts30[69]) 
text_file151.close()  

text_file152 = open(r'C:\Users\Hp\Downloads\New folder\bctech20152','w' , encoding = 'utf-8')
text_file152.write(get_paragraph_texts30[70]) 
text_file152.close()  

text_file153 = open(r'C:\Users\Hp\Downloads\New folder\bctech20153','w', encoding='utf-8')
text_file153.write(get_paragraph_texts30[71]) 
text_file153.close()  

text_file154 = open(r'C:\Users\Hp\Downloads\New folder\bctech20154','w' , encoding='utf-8')
text_file154.write(get_paragraph_texts30[72]) 
text_file154.close()  

text_file155 = open(r'C:\Users\Hp\Downloads\New folder\bctech20155','w' , encoding='utf-8')
text_file155.write(get_paragraph_texts30[73]) 
text_file155.close()  

text_file156 = open(r'C:\Users\Hp\Downloads\New folder\bctech20156','w' , encoding='utf-8')
text_file156.write(get_paragraph_texts30[74]) 
text_file156.close()  

text_file157 = open(r'C:\Users\Hp\Downloads\New folder\bctech20157','w' , encoding='utf-8')
text_file157.write(get_paragraph_texts30[75]) 
text_file157.close()  


# ### We have extracted the data from all the websites mentioned in the Input.xlsx , and store their data into the different files. 
# ### For Each link and article different text documents are created by naming them with their URL_ID

# In[ ]:


print(len(get_paragraph_texts30))


# In[ ]:


print(len(Articles_of_the_pages))
print(len(Titles_of_pages))


# In[ ]:


if len(Articles_of_the_pages) == len(df_excel):
    print(True)
else:
    print(False)


# In[57]:


print(Titles_of_pages)
print(Articles_in_the_pages)


# ### In starting as I mentioned that I have declared two empty lists , and continously updating them as we are extracting Titles and Articles form different mentioned websites from Input.xlsx

# In[127]:


Sentiment_text_df = pd.DataFrame(columns = ['Title','Article_data'])    


# In[128]:


Sentiment_text_df['Title'] = Titles_of_pages


# In[129]:


Sentiment_text_df['Article_data'] = Articles_in_the_pages


# In[130]:


Sentiment_text_df.drop_duplicates(inplace = True)


# In[131]:


print(len(Sentiment_text_df))


# ### Here we have created new csv file , with column names is 'Title' and 'Article_data' , imputing this csv file lists which we have created and now , we start analysins on them using different guidelines .

# In[132]:


Sentiment_text_df   


# In[133]:


Sentiment_text_df.to_csv(r"C:\Users\hp\Downloads\Dataset_analysis.csv") 


# ## Now , we have saved the dataset into out PC using to_csv and in which we have given the path wehere we have to save the data.

# In[113]:


Sentiment_text_df = pd.read_csv('Downloads\Dataset_analysis.csv')
Sentiment_text_df


# ## Analysis work

# ### 1. Sentiment

# ## Cleaning 
# #### Using Stopwords to clean up the dataset

# ### Now we are creating the dictionaries for the stopwords

# In[114]:


read_names_txt = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\StopWords_Names.txt')     


# In[115]:


read_names_txt.columns 


# ### We have stored the stopwords in the StopWords_Names variable 

# In[116]:


StopWords_Names = read_names_txt['SMITH  | Surnames'].values  
StopWords_Names_list = []
for i in StopWords_Names:
    StopWords_Names_list.append(str(i).lower())
print(StopWords_Names_list)


# In[117]:


read_geographic_txt = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\StopWords_Geographic.txt')     


# ## Similarily we are storing the Stopwords from the Geographic.txt dcument into the StopWords_Geographic

# In[118]:


StopWords_Geographic = read_geographic_txt['UNITED  | Geographic'].values 
StopWords_Geographic_list = []
for i in StopWords_Geographic:
    StopWords_Geographic_list.append(str(i).lower()) 
removable = []
removed = 0
for j in StopWords_Geographic_list:
    removed = j.replace('|',',')  
    removable.append(removed) 
StopWords_Geographic_list = removable 
print(StopWords_Geographic_list)


# In[119]:


read_GenericLong_txt = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\StopWords_GenericLong.txt')     


# ## Now again we are doing same work to store the  GenericLongWords into the StopWords_GenericLong_list

# In[120]:


StopWords_GenericLong = read_GenericLong_txt['a'].values 
StopWords_GenericLong_list = []
for i in StopWords_GenericLong:
    StopWords_GenericLong_list.append(str(i).lower()) 
#print(StopWords_GenericLong_list)
print(len(StopWords_GenericLong_list))
removed = 0 
removable = [] 
for j in StopWords_GenericLong_list:
    removed = j.replace('|',',')
    removable.append(removed) 
StopWords_GenericLong_list = removable 
len(StopWords_GenericLong_list)


# In[121]:


read_Generic_txt = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\StopWords_Generic.txt')     


# In[122]:


read_Generic_txt.columns 


# ## Again we are stroing the Generic words extracted form the text file which contains the StopWords_Generic 

# In[123]:


StopWords_Generic = read_Generic_txt['ABOUT'].values 
StopWords_Generic_list = []
for i in StopWords_Generic:
    StopWords_Generic_list.append(str(i).lower()) 
#print(StopWords_GenericLong_list)
print(len(StopWords_Generic_list))
removed = 0 
removable = [] 
for j in StopWords_Generic_list:
    removed = j.replace('|',',')
    removable.append(removed) 
StopWords_Generic_list = removable 
len(StopWords_Generic_list)


# ## Printed only for the checking purpose just checking weather they are appended into the list or not

# In[124]:


StopWords_Generic_list


# In[125]:


read_DateSandNumbers_txt = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\StopWords_DateSandNumbers.txt')    


# In[126]:


read_DateSandNumbers_txt.columns


# ## Again we have created the list and appending all the words which are in the StopWords_DateSandNumbers.txt 

# In[127]:


StopWords_DateSandNumbers = read_DateSandNumbers_txt['HUNDRED  | Denominations'].values 
StopWords_DateSandNumbers_list = []
for i in StopWords_DateSandNumbers:
    StopWords_DateSandNumbers_list.append(str(i).lower()) 
#print(StopWords_GenericLong_list)
print(len(StopWords_DateSandNumbers_list))
removed = 0 
removable = [] 
for j in StopWords_DateSandNumbers_list:
    removed = j.replace('|',',')
    removable.append(removed) 
StopWords_DateSandNumbers_list = removable 
len(StopWords_DateSandNumbers_list)


# In[ ]:


read_Currencies_txt = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\StopWords_Currencies.txt' , encoding='ISO-8859-1') 
read_Currencies_txt.columns


# ## We have created the list in which all the words situated in the StopWords_Currencies.txt are appending in the list.

# In[129]:


StopWords_Currencies = read_Currencies_txt['AFGHANI  | Afghanistan'].values 
StopWords_Currencies_list = []
for i in StopWords_Currencies:
    StopWords_Currencies_list.append(str(i).lower()) 
#print(StopWords_GenericLong_list)
print(len(StopWords_Currencies_list))
removed = 0 
removable = [] 
for j in StopWords_Currencies_list:
    removed = j.replace('|',',')
    removable.append(removed) 
StopWords_Currencies_list = removable 
len(StopWords_Currencies_list) 
print(StopWords_Currencies_list)


# In[130]:


read_Auditor_txt = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\StopWords_Auditor.txt')     


# ## We have created the list StopWords_Auditor which is going to append the list elements into the created list which is extracted from the file read_Auditor

# In[131]:


StopWords_Auditor = read_Auditor_txt.values
StopWords_Auditor_list = []
for i in StopWords_Auditor:
    new_text = ' '
    for j in i:
        if j not in '[]':
            new_text += j 
        StopWords_Auditor_list.append(new_text) 
lower_case = []
for k in StopWords_Auditor_list:
    lower_case.append(k.lower()) 
StopWords_Auditor_list = lower_case 
print(StopWords_Auditor_list)
    


# ###  We have created a empty list in which we are going to append the articles which are present into the table Sentiment_text_df in the column name 'Article_data'  , we have done it to delete the stopwords from the Articles on which we are going to perform analysis.

# In[132]:


Articles_in_the_pages_lists = []

count = 0 

for i in Sentiment_text_df['Article_data']:
    
    lists_11 = i.split(" ")
    count += 1 
    print(f'Done {count}')
    Articles_in_the_pages_lists.append(lists_11)


# ## Now , we are removing all the stopwords form the Articles 

# In[133]:


for i in Articles_in_the_pages_lists:
    for j in i: 
        if j.lower() in StopWords_Geographic_list:
            i.remove(j)      


# ### Above code has removed all the Geographic stopwords which are present into the list.

# In[134]:


for i in Articles_in_the_pages_lists:
    for j in i: 
        if j.lower() in StopWords_Names_list:
            i.remove(j)      


# ### Above code has removed all the Names stopwords which are present into the list.

# In[135]:


for i in Articles_in_the_pages_lists:
    for j in i: 
        if j.lower() in StopWords_GenericLong_list:
            i.remove(j)      


# ### Above code has removed all the GenericLong stopwords which are present into the list.

# In[136]:


for i in Articles_in_the_pages_lists:
    for j in i: 
        if j.lower() in StopWords_Generic_list:
            i.remove(j)      


# ### Above code has removed all the Generic stopwords which are present into the list.

# In[137]:


for i in Articles_in_the_pages_lists:
    for j in i: 
        if j.lower() in StopWords_DateSandNumbers_list:
            i.remove(j)      


# ### Above code has removed all the DayeSandNumbers stopwords which are present into the list.

# In[138]:


for i in Articles_in_the_pages_lists:
    for j in i: 
        if j.lower() in StopWords_Currencies_list:
            i.remove(j)      


# ### Above code has removed all the Currencies stopwords which are present into the list.

# In[139]:


for i in Articles_in_the_pages_lists:
    for j in i: 
        if j.lower() in StopWords_Auditor_list:
            i.remove(j)      


# ### Above code has removed all the Auditors stopwords which are present into the list.

# In[ ]:


Articles_cleaned = [] 

for j in Articles_in_the_pages_lists:
    Articles_in_string = ' '
    for i in j:
        Articles_in_string += ' ' + i 
    Articles_cleaned.append(Articles_in_string) 


# ### In the above code we are storing all the celaned articles

# In[141]:


count = 0 
for i in Articles_cleaned:
    count += 1
    print(f'Done {count}') 
    print(i)


# ### Now I am going to Initialize the Articles_cleaned variable in the Sentiment_text_df table 

# In[142]:


Articles_cleaned = pd.DataFrame(Articles_cleaned)    


# In[143]:


Articles_cleaned.drop_duplicates(inplace = True) 
print(len(Articles_cleaned))


# ### Here , I have removed all the duplications into the rows and columns

# In[144]:


Sentiment_text_df['Article_data'] = Articles_cleaned 


# In[145]:


Sentiment_text_df 


# ### Now , it is our imported dataset on which we are going to perform various analysis tasks

# ## Now, we are going to analyze the sentiment for each of the articles by importing negative and positive elements from the MasterDictionery text files which has both positive and negative text files.

# ### Importing Positive and Negative texts files

# In[146]:


Positive_texts_analysis = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\positive-words.txt')    


# ### In above code we have imported all the positive words which is present in the MasterDictionery

# In[147]:


Positive_texts_analysis = Positive_texts_analysis.values     


# ### We have Stored all the positive values into the Positive_texts_analysis

# In[148]:


Negative_texts_analysis = pd.read_fwf(r'C:\Users\Hp\Downloads\New folder\negative-words.txt' , encoding='ISO-8859-1') 
Negative_texts_analysis = Negative_texts_analysis.values  


# ### In above code we have imported all the positive words which is present in the MasterDictionery 
# ### We have Stored all the positive values into the Positive_texts_analysis

# In[149]:


print('Hellow')


# ### Importing the nltk library to tokenize the words for each articles for which returns list of the words.

# In[150]:


from nltk.tokenize import word_tokenize 
import nltk   
nltk.download('punkt')
print('Library imported') 


# In[151]:


tokens = word_tokenize(Sentiment_text_df['Article_data'][0])  


# ## Tokenization is one of the important aspect of the Natural Language Processing it is use to break complete sentence into the form of words.

# ## Checking it weather it is tokenizing the article properly or not.

# In[152]:


for i in tokens:
    print(i)
    


# ### Yes they are tokenizing the articles properly .

# ## Now , we are going to create a positive , negative elements 

# In[153]:


Positive_counts_per_article_list = [] 
Negative_counts_per_article_list = []
Polarity_score = []

count = 0 





for i in Sentiment_text_df['Article_data']:
    
    Positive_counts_per_article = 0 
    Negative_counts_per_article = 0
    
    tokens = word_tokenize(i) 
    
    for j in tokens:
        
        if j.lower() in Positive_texts_analysis:
            Positive_counts_per_article += 1
            
        if j.lower() in Negative_texts_analysis:
            Negative_counts_per_article += -1
        
    Positive_counts_per_article_list.append(Positive_counts_per_article) 
    
    Negative_counts_per_article_list.append(Negative_counts_per_article * -1) 
    
    count +=1 
    print(f'Done for article {count} ')


# ### Now, we have created the lists in which we are storing all the positive and negative words which are there in the Article .

# In[154]:


print(Positive_counts_per_article_list)
print(Negative_counts_per_article_list)


# ### Now we are going to add two more columns in the Positive_score and negative_score in the table 

# In[155]:


Sentiment_text_df['Positive Score'] =  Positive_counts_per_article_list
Sentiment_text_df['Negative Score'] = Negative_counts_per_article_list 


# In[156]:


Sentiment_text_df.isnull().sum()


# ### Now , we check the polarity score for the Articles based upon there it's range will lie form -1 to +1 . As it's range moves from -1 to +1 which means +1 score is showing the Text is positive and -1 is showing that Text is not on favour.

# In[157]:


Sentiment_text_df['Polarity Score'] = (Sentiment_text_df['Positive Score'] - Sentiment_text_df['Negative Score']) / ( ( Sentiment_text_df['Positive Score'] + Sentiment_text_df['Negative Score']  ) +0.000001 )


# ### Now, we are going to calculate the Subjectivity of the article it , shows if the articles is about the fact or it may be personal opinion.
# ### It's range is always from 0 to 1 , if the score is close to 1 then , it is factual text  , but if it is 0 then it is opinion .

# In[158]:


Sentiment_text_df['SUBJECTIVITY SCORE'] = ( Sentiment_text_df['Positive Score'] + Sentiment_text_df['Negative Score']  ) / ( len(Sentiment_text_df['Article_data']) + 0.000001)


# ## 2. Analysis of Readbility

# In[159]:


Sentiment_text_df.to_csv(r"C:\Users\hp\Downloads\Dataset_analysis2.csv")   


# In[160]:


Sentiment_text_df = pd.read_csv('Downloads/Dataset_analysis2.csv')   


# In[161]:


Sentiment_text_df.columns


# ## I have saved the table Sentiment_text_df by using the to_csv function.

# ## Calculating the number of words per article

# In[162]:


number_of_words = []
for i in Sentiment_text_df['Article_data']:
    tokens = word_tokenize(i) 
    number_of_words.append(len(tokens)) 
print(number_of_words)


# ## Now we have to calculate the ,  average_sentence_lenght for which we have to calculate the number of words and number of sentences 

# In[163]:


number_of_sentences = [] 
for i in Sentiment_text_df['Article_data']:
    tokens = i.split(",") 
    number_of_sentences.append(len(tokens)) 
print(number_of_sentences)  


# ## In the above code  , I have to calculated the number of sentences per article 

# In[166]:


Sentiment_text_df['AVG SENTENCE LENGTH'] = number_of_words['number_of_words'] / number_of_sentences['number_of_sentences']  


# ## I the above code I , have calculated the Average sentence lenght by dividing number of words with the number of sentences.

# In[165]:


number_of_words = pd.DataFrame(number_of_words , columns = ['number_of_words'])  
number_of_sentences = pd.DataFrame(number_of_sentences , columns = ['number_of_sentences']) 


# ## I have calculated the number of words per article .

# In[167]:


number_of_complex_words = [] 
for i in Sentiment_text_df['Article_data']:
    tokens = word_tokenize(i) 
    counts_per_words = 0 
    counts_per_article = 0 
    for j in tokens:
        for k in j:
            if k in 'aeiouAEIOU':
                counts_per_words += 1 
        if counts_per_words > 2:
            counts_per_article += 1 
        counts_per_words = 0 
    number_of_complex_words.append(counts_per_article) 
print(number_of_complex_words)


# ## In the above code we have calculated the number_of_complex_words these words contains more than two vowels.

# In[168]:


len(number_of_complex_words) 


# In[169]:


number_of_complex_words = pd.DataFrame(number_of_complex_words, columns = ['number_of_complex_words']) 


# In[170]:


Sentiment_text_df['PERCENTAGE OF COMPLEX WORDS'] = number_of_complex_words['number_of_complex_words'] / number_of_words['number_of_words']


# ## In the above code we have calculated the Percentage of the complex words in which by using the formula Percentage_of_complex_words = number_of_complex_words / number_of_words.

# In[171]:


Sentiment_text_df['FOG INDEX'] = 0.4 * (Sentiment_text_df['AVG SENTENCE LENGTH'] + Sentiment_text_df['PERCENTAGE OF COMPLEX WORDS'])


# ## In the above code we have calculated the FOG INDEX it is to determine the level of dificulty the text contains.
# ## Calculated it by using formula FOG INDEX = Average_lenght_of_sentence / Percentage of complex words

# ## Average Number of words per sentence

# In[172]:


Sentiment_text_df['AVG NUMBERS OF WORDS PER SENTENCE'] = number_of_words['number_of_words'] / number_of_sentences['number_of_sentences']


# ### In the above code we are calculating the average_number_of_words_per_sentence by using this formula : 
# ### number_of_words / number_of_sentences.

# ## Complex Word Count

# In[173]:


Sentiment_text_df['COMPLEX WORD COUNT'] = number_of_complex_words['number_of_complex_words'] 


# In[174]:


Sentiment_text_df['WORD COUNT'] = len(Sentiment_text_df['Article_data']) 


# ## By calculating all the required parameters we have also added them as columns in our dataset Sentiment_text_df.

# ## 6. Syllabe per Count

# In[175]:


number_complex_per_articless = []
for i in Sentiment_text_df['Article_data']:
    complex_per_syllabe = 0 
    for j in i:
        if (j.endswith('es')) or (j.endswith('ed')) :
            pass 
        else:
            for k in j:
                complex_per_syllabe += 1 
    number_complex_per_articless.append(complex_per_syllabe) 


# ## Now , we have started adding all the vowels in the words and calculating the SYLLABE PER WORD  by adding them into the list and then putting them seperately.

# In[176]:


print(len(number_complex_per_articless))
number_complex_per_articless = pd.DataFrame(number_complex_per_articless , columns = ['complex_per_word']) 


# In[177]:


Sentiment_text_df['SYLLABE PER WORD'] = number_complex_per_articless['complex_per_word'] 


# ## In the above code we have added one more column  into our dataset which contains all the complex_words

# In[178]:


number_of_personal_pronouns = [] 
pronouns = ['I' , 'we' , 'my' , 'ours' , 'us'] 
for i in Sentiment_text_df['Article_data']:
    tokens = word_tokenize(i)
    counts_per_pronouns = 0 
    for j in tokens:
        if j in pronouns:
            counts_per_pronouns += 1
    number_of_personal_pronouns.append(counts_per_pronouns) 
print(number_of_personal_pronouns)


# In[179]:


Sentiment_text_df['PERSONAL PRONOUNS'] = pd.DataFrame(number_of_personal_pronouns)  


# ## In the above codes we have counted the number of personal pronouns which are present into the articles.

# In[180]:


sum_of_total_number_of_charecter = []
for i in Sentiment_text_df['Article_data']:
    sum_of_charecters = 0
    for j in i:
        if j != ' ':
            sum_of_charecters += 1 
    sum_of_total_number_of_charecter.append(sum_of_charecters) 
print(sum_of_total_number_of_charecter)


# In[181]:


sum_of_total_number_of_charecter = pd.DataFrame(sum_of_total_number_of_charecter , columns = ['sum_of_charecters'])


# In[182]:


Sentiment_text_df['AVG WORD LENGTH'] = sum_of_total_number_of_charecter['sum_of_charecters'] / number_of_words['number_of_words'] 


# ## Now , we have to calculate and add the average word lenght per article so , we are adding the sum_of_charecters per word into the sum_of_total_number_of_charecter list , we already have the words per articles. 
# ## We use the sum_of_charecters / total_number_words for calculating the Average_word_length

# In[183]:


Sentiment_text_df.drop_duplicates(inplace = True)


# In[184]:


len(Sentiment_text_df)


# In[185]:


df_excel['URL']


# In[186]:


Sentiment_text_df.columns


# ### we are checking weather all the columns are added properly or not.

# In[187]:


Output_data_Structure = pd.read_excel('Downloads/New folder/Output Data Structure.xlsx')


# In[188]:


Output_data_Structure.columns 


# ### In the above code , we have imported the Output_data_Structure in which according to assignment we have to fill all the missing values which are there into the Output_data_structure excel file.

# In[221]:


Output_data_Structure['POSITIVE SCORE'] = Sentiment_text_df['Positive Score'] 


# In[222]:


Output_data_Structure['NEGATIVE SCORE'] = Sentiment_text_df['Negative Score']


# In[223]:


Output_data_Structure['POLARITY SCORE'] = Sentiment_text_df['Polarity Score']  


# In[224]:


Output_data_Structure['SUBJECTIVITY SCORE'] = Sentiment_text_df['SUBJECTIVITY SCORE']   


# In[225]:


Output_data_Structure['AVG SENTENCE LENGHT'] = Sentiment_text_df['AVG SENTENCE LENGTH']    


# In[226]:


Output_data_Structure['PERCENTAGE OF COMPLEX WORDS'] = Sentiment_text_df['PERCENTAGE OF COMPLEX WORDS']   


# In[227]:


Output_data_Structure['FOG INDEX'] = Sentiment_text_df['FOG INDEX']   


# In[228]:


Output_data_Structure['AVG NUMBER OF WORDS PER SENTENCE'] = Sentiment_text_df['AVG NUMBERS OF WORDS PER SENTENCE']    


# In[229]:


Output_data_Structure['COMPLEX WORD COUNT'] = Sentiment_text_df['COMPLEX WORD COUNT']


# In[230]:


Output_data_Structure['WORD COUNT'] = Sentiment_text_df['WORD COUNT']


# In[231]:


Output_data_Structure['SYLLABLE PER WORD'] = Sentiment_text_df['SYLLABE PER WORD']


# In[232]:


Output_data_Structure['PERSONAL PRONOUNS'] = Sentiment_text_df['PERSONAL PRONOUNS']


# In[233]:


Output_data_Structure['AVG WORD LENGTH'] = Sentiment_text_df['AVG WORD LENGTH'] 


# In[234]:


Output_data_Structure.to_excel(r'C:\Users\Hp\Downloads\Output_data_Structure3.xlsx') 


# ## In those above codes we have assigned the values into , the null columns of the Output_data_Structure.xlsx file , 
# ### All the columns are filled with the appropiate values where they are required. 

# In[235]:


Sentiment_text_df['AVG SENTENCE LENGTH']   


# In[241]:


Output_data_Structure['AVG SENTENCE LENGHT']  


# In[240]:


Output_data_Structure['AVG SENTENCE LENGTH'] = Output_data_Structure['AVG SENTENCE LENGHT'] 


# In[242]:


Output_data_Structure['AVG SENTENCE LENGTH']


# ## I think , I data is not imputed right in the average_sentence_lenght column so , we are going to fill them right at their place . Because when I go and opened the file these values are missing . 

# In[ ]:





# In[243]:


Output_data_Structure.head()


# In[244]:


Output_data_Structure.to_excel(r'C:\Users\Hp\Downloads\Output_data_Structure4.xlsx') 


# In[254]:


import string as str1

lenghts_per_article = []

str_punct =  str1.punctuation

for i in Sentiment_text_df['Article_data']:
    
    tokenize = word_tokenize(i) 
    
    counts_per_word = 0 
    
    for j in tokenize:
        if i not in str_punct:
            counts_per_word += 1 
    lenghts_per_article.append(counts_per_word)


# In[256]:


lenghts_per_article = pd.DataFrame(lenghts_per_article , columns = ['WORD COUNT']) 


# In[258]:


Output_data_Structure['WORD COUNT'] = lenghts_per_article['WORD COUNT']


# ## As here in the dataset we have seen that the words are coming to be same but it is probably not possible because each of the articles contains different count of words , so I have again processed that code and assiging the values properly.

# In[260]:


Output_data_Structure.head(20)


# ## Now , they are correct.

# In[263]:


pronouns_list = ['I','we','my','ours','us','WE','We','MY','My','Our\'s','OUR\'S']


# In[266]:


personal_pronouns_list = []

for i in Sentiment_text_df['Article_data']:
    tokens =  word_tokenize(i)
    
    count_personal_pronouns = 0 
    for j in tokens:
        if j in pronouns_list:
            count_personal_pronouns += 1 
    
    personal_pronouns_list.append(count_personal_pronouns) 
print(personal_pronouns_list)


# In[267]:


personal_pronouns_list = pd.DataFrame(personal_pronouns_list , columns = ['PERSONAL PRONOUNS'])


# In[268]:


Output_data_Structure['PERSONAL PRONOUNS'] = personal_pronouns_list['PERSONAL PRONOUNS']


# ## I again takeout all the pronouns names andproces them , as I am not satisfied with the presious result , but now also I am getting same result , so I am going with it.

# In[269]:


Output_data_Structure.head()


# In[274]:


#Output_data_Structure.to_excel(r'C:\Users\Hp\Downloads\Output_data_Structure5.xlsx')
Output_data_Structure.columns


# In[ ]:





# # Conclusion
# ### 1. Finally we have done our work to fill all the emply variables present in the Output_datastructure file . Now , we are going to .
# ### 2. In this analysis I get to know about various things and like how to analyze the text .
# ### 3. How , important it is to checking for all of those parameters , plays vital role in the bussinesses.
# ### 4. In the above result we come to know about various results , are averagely about , 29 words are positive per article, 4 words are negative per activles .
# ### 5. In polarity we come to know that on the average basis our articles are moving towards positivity because as we know that polarity ranges from -1 to +1 in which the how much the score is pointing towards 1 it can be positive sign.
# ### 6. In Subjectivity we come to know that most of the articles are factual.
# ### 7. In Fog Index column we come to know tha out articles are averagely so easy as it's complexity is less due to which more and more people prefer to read . 
# ### 8. Average number of words per sentence is about 9 for every article.
# ### 9 . There are about 559 average complex words count per article , for technical aspect it is good sign.
# ### 10 . In average sentence lenght we have come to know that it is about 8 , whcih is easy to udnerstand and splits it also help us to recognize the sentences properly. 

# In[ ]:




