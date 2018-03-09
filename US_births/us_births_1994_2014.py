
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


# In[15]:


def dict_limits(input_dict, if_max = True):
    if_first = True
    sign = 2 * if_max - 1
    
    for item in input_dict:
        if if_first:
            comp_item = input_dict[item]
            if_first = False
        else:
            if sign * input_dict[item] > sign * comp_item:
                comp_item = input_dict[item]
            
    return comp_item


# In[16]:


max_cdc_dow_births = dict_limits(input_dict = cdc_dow_births, if_max = True)
min_cdc_dow_births = dict_limits(input_dict = cdc_dow_births, if_max = False)

max_cdc_dom_births = dict_limits(input_dict = cdc_dom_births, if_max = True)
min_cdc_dom_births = dict_limits(input_dict = cdc_dom_births, if_max = False)


# In[17]:


max_cdc_dow_births


# In[18]:


min_cdc_dow_births


# In[19]:


max_cdc_dom_births


# In[20]:


min_cdc_dom_births


# In[21]:


def births_dynamic(data, column, value):
    births_per_year = {}
    births_changes = {}
    min_year = 1994
    
    for item in data:
        year = item[0]
        feature = item[column]
        births = item[4]
        
        if feature == value:
            if year in births_per_year:
                births_per_year[year] = births_per_year[year] + births
            else:
                births_per_year[year] = births
    
    for year_of_birth in births_per_year:
        if year_of_birth == min_year:
            births_changes[year_of_birth] = 0
        else:
            actual = births_per_year[year_of_birth]
            previous = births_per_year[year_of_birth - 1]
            
            births_changes[year_of_birth] = actual - previous
    
    return births_changes


# In[22]:


cdc_saturday_dynamic = births_dynamic(data = cdc_list, column = 3, value = 6)
cdc_march_dynamic = births_dynamic(data = cdc_list, column = 1, value = 3)
cdc_21dom_dynamic = births_dynamic(data = cdc_list, column = 2, value = 21)


# In[23]:


cdc_saturday_dynamic


# In[24]:


cdc_march_dynamic


# In[25]:


cdc_21dom_dynamic


# In[26]:


cdc_list2 = read_csv("US_births_2000-2014_SSA.csv")
cdc_list2


# In[27]:


def data_comb(data1, data2, method = "mean"):
    cdc = {}
    
    for item in data1:
        key = str(item[0]) + str(item[1]) + str(item[2])
        cdc[key] = item
    
    for item in data2:
        key = str(item[0]) + str(item[1]) + str(item[2])
        
        if key in cdc:
            if method == "mean":
                cdc[key][4] = int((cdc[key][4] + item[4]) / 2)
            elif method == "second_data":
                cdc[key][4] = item[4]
        else:
            cdc[key] = item
            
    return cdc


# In[28]:


cdc_comb_list = data_comb(data1 = cdc_list, data2 = cdc_list2, method = "mean")
cdc_comb_list

