
# coding: utf-8

# In[4]:


f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
births_list = f.read().split("\n")
births_list[0:10]


# In[5]:


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


# In[6]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[7]:


cdc_list[0:10]


# In[8]:


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


# In[9]:


cdc_month_births = month_births(cdc_list)


# In[10]:


cdc_month_births


# In[11]:


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


# In[12]:


cdc_day_births = dow_births(cdc_list)
cdc_day_births


# In[13]:


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


# In[14]:


cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)

cdc_year_births


# In[15]:


cdc_month_births


# In[16]:


cdc_dom_births


# In[17]:


cdc_dow_births


# In[41]:


def dict_limits(input_dict, if_max = True):
    counter = 0
    sign = 2 * if_max - 1
    
    for item in input_dict:
        if counter == 0:
            comp_item = input_dict[item]
        else:
            if sign * input_dict[item] > sign * comp_item:
                comp_item = input_dict[item]
        
        counter = counter + 1
            
    return comp_item


# In[45]:


max_cdc_dow_births = dict_limits(input_dict = cdc_dow_births, if_max = True)
min_cdc_dow_births = dict_limits(input_dict = cdc_dow_births, if_max = False)

max_cdc_dom_births = dict_limits(input_dict = cdc_dom_births, if_max = True)
min_cdc_dom_births = dict_limits(input_dict = cdc_dom_births, if_max = False)


# In[43]:


max_cdc_dow_births


# In[44]:


min_cdc_dow_births


# In[46]:


max_cdc_dom_births


# In[47]:


min_cdc_dom_births

