
# coding: utf-8

# In[1]:


f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
births_list = f.read().split("\n")
births_list[0:10]


# In[2]:


def read_csv(csv_name):
    f = open(csv_name, "r")
    string_list = f.read().split("\n")
    string_list = string_list[1:len(string_list)]
    
    final_list = []
    
    for item in string_list:
        int_fields = []
        string_fields = item.split(",")
        
        for each in string_fields:
            int_fields.append(int(each))
        
        final_list.append(int_fields)
    
    return final_list


# In[3]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[4]:


cdc_list[0:10]


# In[5]:


def month_births(births_list):
    births_per_month = {}
    
    for item in births_list:
        month = item[1]
        births = item[4]
        
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
        
    return births_per_month


# In[6]:


cdc_month_births = month_births(cdc_list)


# In[7]:


cdc_month_births


# In[8]:


def dow_births(births_list):
    births_per_dow = {}
    
    for item in births_list:
        dow = item[3]
        births = item[4]
        
        if dow in births_per_dow:
            births_per_dow[dow] = births_per_dow[dow] + births
        else:
            births_per_dow[dow] = births
        
    return births_per_dow


# In[9]:


cdc_day_births = dow_births(cdc_list)
cdc_day_births


# In[10]:


def calc_counts(data, column):
    births_per_feature = {}
    
    for item in data:
        feature = item[column]
        births = item[4]
        
        if feature in births_per_feature:
            births_per_feature[feature] = births_per_feature[feature] + births
        else:
            births_per_feature[feature] = births
        
    return births_per_feature


# In[11]:


cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)

cdc_year_births


# In[12]:


cdc_month_births


# In[13]:


cdc_dom_births


# In[14]:


cdc_dow_births

