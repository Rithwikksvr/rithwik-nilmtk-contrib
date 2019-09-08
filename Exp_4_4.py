#!/usr/bin/env python
# coding: utf-8

# In[1]:


from api import API


# In[3]:


redd = {
  'power': {
    'mains': ['apparent','active'],
    'appliance': ['apparent','active']
  },
  'sample_rate': 60,
  'appliances': ['washing machine','fridge'],
  'methods': {
    'Mean': {},"CO":{},"FHMM_EXACT":{'num_of_states':2},
       'Seq2Point':{'n_epochs':1},
      "Seq2Seq":{'n_epochs':1},'RNN':{'n_epochs':1},"WindowGRU":{'n_epochs':1},
       'DAE':{'n_epochs':1}
  },
    
  'train': {
    'datasets': {
      'UKDALE': {
        'path': '/home/nilmtk/nilmtk-contrib/ukdale.h5',
        'buildings': {
              1: {
                'start_time': '2017-01-05',
                'end_time': '2017-03-05'#
              },
          
        }
      },
        
    }
  },
    
  'test': {
    'datasets': {
      'DRED': {
        'path': '/home/nilmtk/nilmtk-contrib/DRED.h5',
        'buildings': {
              1: {
                    'start_time': '2015-09-21',
                    'end_time': '2015-10-01'
          }
        }
      },
      'REDD': {
        'path': '/home/nilmtk/redd.h5',
        'buildings': {
              1: {
                    'start_time': '2011-04-17',
                    'end_time': '2011-04-27'
          }
        }
      }
    },
    'metrics': ['mae', 'rmse']
  }
}


# In[3]:





# In[3]:


API(redd)


# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:





# In[4]:




