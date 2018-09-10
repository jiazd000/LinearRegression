# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import datetime
import lightgbm as lgb
from sklearn.decomposition import PCA
from sklearn import preprocessing
from collections import Counter


def Chara_mean(Df,num):
    Df_new = pd.DataFrame()
    for i in range(num):

        name = 'FTR%d' % i

        Dfn = Df[name].astype(float).groupby(Df['PERSONID'],sort=False).mean()

        Dfn = pd.DataFrame({name: Dfn})

        Df_new = pd.concat([Df_new,Dfn],axis=1)


    return Df_new

def Chara_count(Df):
    Df_new = pd.DataFrame()


    name = 'FTR%d' % 0

    Dfn = Df['FTR0'].astype(float).groupby(Df['PERSONID'],sort=False).count()

    Dfn = pd.DataFrame({'FTRcount': Dfn})

    Df_new = pd.concat([Df_new,Dfn],axis=1)

    return Df_new

def Chara_max(Df,num):
    Df_new = pd.DataFrame()
    for i in range(num):

        name = 'FTR%d' % i

        Dfn = Df[name].astype(float).groupby(Df['PERSONID'],sort=False).max()

        Dfn = pd.DataFrame({name: Dfn})

        Df_new = pd.concat([Df_new,Dfn],axis=1)

    return Df_new

def Chara_min(Df,num):
    Df_new = pd.DataFrame()
    for i in range(num):

        name = 'FTR%d' % i

        Dfn = Df[name].astype(float).groupby(Df['PERSONID'],sort=False).min()

        Dfn = pd.DataFrame({name: Dfn})

        Df_new = pd.concat([Df_new,Dfn],axis=1)

    return Df_new



def Chara_std(Df,num):
    Df_new = pd.DataFrame()
    for i in range(num):

        name = 'FTR%d' % i

        Dfn = Df[name].astype(float).groupby(Df['PERSONID'],sort=False).std()

        Dfn = pd.DataFrame({name: Dfn})

        Df_new = pd.concat([Df_new,Dfn],axis=1)

    return Df_new

def Chara_FTRfre(Df,num):
    Df_new = pd.DataFrame()
    for i in range(num):
        nn = 'FTR%d' % i
        Df_FT = pd.DataFrame()

        for name, group in Df.groupby(['PERSONID'], sort=False):
            print group
            print name
            FT = list(group[nn])
            FT = Counter(FT).values()

            Dfn = pd.DataFrame({nn+'max': [max(FT)],nn+'min': [min(FT)],nn+'mean': [sum(FT)/len(FT)],nn+'var': [np.var(np.array(FT))]})

            Df_FT = pd.concat([Df_FT,Dfn],axis=0)

        Df_new = pd.concat([Df_new, Df_FT], axis=1)

    return Df_new




def Chara_date(Df):
    Df_new = pd.DataFrame()
    time_list = []
    delta_time = 0
    for name,group in Df.groupby(['PERSONID'],sort=False):

        group = group.sort_values(['CREATETIME'])
        print group

        time_min = group.iloc[0]['CREATETIME']
        time_max = group.iloc[group.shape[0]-1]['CREATETIME']

        time_min = datetime.datetime.strptime(time_min, '%Y-%m-%d')
        time_max = datetime.datetime.strptime(time_max, '%Y-%m-%d')
        print time_min,time_max
        print '.....................'
        print (time_max-time_min).days

        Dt = pd.DataFrame({'Deltatime': [(time_max-time_min).days]})

        Df_new = pd.concat([Df_new,Dt],axis=0)

    return Df_new

def Chara_date2(Df):
    Df_new = pd.DataFrame()

    delta_time = 0
    for name,group in Df.groupby(['PERSONID'],sort=False):
        time_list = []
        group = group.sort_values(['CREATETIME'])
        print group
        if group.shape[0]<2:
            time_list_mean = 0
            time_list_max = 0
            time_list_min = 0
            time_list_var = 0
        else:
            for i in range(group.shape[0]-1):


                time1 = group.iloc[i]['CREATETIME']
                time2 = group.iloc[i+1]['CREATETIME']

                time1 = datetime.datetime.strptime(time1, '%Y-%m-%d')
                time2 = datetime.datetime.strptime(time2, '%Y-%m-%d')
                print time1,time2
                print '.....................'
                print (time2-time1).days

                time_list.append((time2-time1).days)
            time_list_mean = np.mean(np.array(time_list))
            time_list_max = max(time_list)
            time_list_min = min(time_list)
            time_list_var = np.var(np.array(time_list))

        Dt = pd.DataFrame({'Time_mean': [time_list_mean],'Time_max':[time_list_max],'Time_min':[time_list_min],'Time_var':[time_list_var]})

        Df_new = pd.concat([Df_new,Dt],axis=0)

    return Df_new

def Chara_date_fre(Df):
    Df_new = pd.DataFrame()
    for name,group in Df.groupby(['PERSONID'],sort=False):
        time_list = []
        group = group.sort_values(['CREATETIME'])
        print group
        for i in range(group.shape[0]):

            time = group.iloc[i]['CREATETIME']

            print time
            print '.....................'

            time_list.append(time)
        time_list = Counter(time_list).values()
        time_list_mean = sum(time_list)/len(time_list)
        time_list_max = max(time_list)
        time_list_min = min(time_list)
        time_list_var = np.var(np.array(time_list))

        Dt = pd.DataFrame({'Timefre_mean': [time_list_mean],'Timefre_max':[time_list_max],'Timefre_min':[time_list_min],'Timefre_var':[time_list_var]})

        Df_new = pd.concat([Df_new,Dt],axis=0)

    return Df_new

def Chara_fre(Df,date_name1):

    Delttime = pd.read_csv(date_name1, sep='\t', header=0)

    print Delttime.head()
    Df_new = pd.DataFrame()

    Dfn = Df['FTR0'].astype(float).groupby(Df['PERSONID'],sort=False).count()

    Dfn = pd.DataFrame({'FTRcount': Dfn})
    Dfn = Dfn.reset_index(drop=True)

    Df_fre = Delttime['Deltatime'].div(Dfn['FTRcount'],fill_value=0)
    # Df_fre = Df_fre.div(100)

    Df_new = pd.concat([Df_new,Df_fre],axis=1)

    # Df_new = Df_new.columns = ['fre']
    return Df_new

def Chara_medi(Df):
    Df_new = pd.DataFrame()

    for name,group in Df.groupby(['PERSONID'],sort=False):
        medicine_list = []
        group = group.sort_values(['FTR51'])
        print group

        for i in range(group.shape[0]):

            medicine = group.iloc[i]['FTR51']

            num_medi = medicine.count(',')+1

            print num_medi
            print '......................'
            medicine_list.append(num_medi)

        medicine_list_mean = np.mean(np.array(medicine_list))
        medicine_list_max = max(medicine_list)
        medicine_list_min = min(medicine_list)
        medicine_list_var = np.var(np.array(medicine_list))
        medicine_list_sum = sum(medicine_list)

        Dt = pd.DataFrame({'medicine_mean': [medicine_list_mean],'medicine_max':[medicine_list_max],'medicine_min':[medicine_list_min],'medicine_var':[medicine_list_var],'medicine_sum':[medicine_list_sum]})

        Df_new = pd.concat([Df_new,Dt],axis=0)

    return Df_new

def Chara_meditype(Df):
    Df_new = pd.DataFrame()

    for name,group in Df.groupby(['PERSONID'],sort=False):
        meditype_list = []
        meditypesum_list = []
        group = group.sort_values(['FTR51'])
        print group

        for i in range(group.shape[0]):

            meditype = group.iloc[i]['FTR51']

            meditype = meditype.split(',')

            meditypesum_list = list(set(meditypesum_list+meditype))    #去除列表重复项

            num_meditype = len(Counter(meditype).values())

            print num_meditype
            print meditypesum_list
            print '......................'
            meditype_list.append(num_meditype)

        meditype_list_mean = np.mean(np.array(meditype_list))
        meditype_list_max = max(meditype_list)
        meditype_list_min = min(meditype_list)
        meditype_list_var = np.var(np.array(meditype_list))
        meditype_list_sum = len(meditypesum_list)

        Dt = pd.DataFrame({'meditype_mean': [meditype_list_mean],'meditype_max':[meditype_list_max],'meditype_min':[meditype_list_min],'meditype_var':[meditype_list_var],'meditype_sum':[meditype_list_sum]})

        Df_new = pd.concat([Df_new,Dt],axis=0)

    return Df_new

def Chara_meditype_fre(Df):
    Df_new = pd.DataFrame()

    for name,group in Df.groupby(['PERSONID'],sort=False):
        meditypesum_list = []
        group = group.sort_values(['FTR51'])
        print group

        for i in range(group.shape[0]):

            meditype = group.iloc[i]['FTR51']

            meditype = meditype.split(',')

            meditypesum_list = meditypesum_list+meditype

            print meditypesum_list
            print '......................'
        meditypefre_list = Counter(meditypesum_list).values()

        meditype_list_mean = np.mean(np.array(meditypefre_list))
        meditype_list_max = max(meditypefre_list)
        meditype_list_min = min(meditypefre_list)
        meditype_list_var = np.var(np.array(meditypefre_list))

        Dt = pd.DataFrame({'meditypefre_mean': [meditype_list_mean],'meditypefre_max':[meditype_list_max],'meditypefre_min':[meditype_list_min],'meditypefre_var':[meditype_list_var]})

        Df_new = pd.concat([Df_new,Dt],axis=0)

    return Df_new

def Chara_all(Df,num,date_name1,date_name2,medi_name,meditype_name,meditypefre_name,date_fre,FTRfre_name,FTRsum_name,FTRNo0_name):

    Delttime = pd.read_csv(date_name1, sep='\t', header=0)
    Df_date = pd.read_csv(date_name2, sep='\t', header=0)
    Df_medi = pd.read_csv(medi_name, sep='\t', header=0)
    Df_meditype = pd.read_csv(meditype_name, sep='\t', header=0)
    Df_meditypefre = pd.read_csv(meditypefre_name, sep='\t', header=0)
    Df_date_fre = pd.read_csv(date_fre, sep='\t', header=0)
    Df_FTR_fre = pd.read_csv(FTRfre_name, sep='\t', header=0)
    Df_FTR_sum = pd.read_csv(FTRsum_name, sep='\t', header=0)
    Df_FTR_No0 = pd.read_csv(FTRNo0_name, sep='\t', header=0)


    Df_date = Df_date.reset_index(drop=True)
    Df_medi = Df_medi.reset_index(drop=True)    #由于数据存储index =false
    Df_meditype = Df_meditype.reset_index(drop=True)
    Df_meditypefre = Df_meditypefre.reset_index(drop=True)
    Df_date_fre = Df_date_fre.reset_index(drop=True)
    Df_FTR_fre = Df_FTR_fre.reset_index(drop=True)
    Df_FTR_sum = Df_FTR_sum.reset_index(drop=True)
    Df_FTR_No0 = Df_FTR_No0.reset_index(drop=True)

    Df_mean = Chara_mean(Df,num)
    Df_count = Chara_count(Df)
    Df_max = Chara_max(Df, num)
    Df_min = Chara_min(Df, num)
    Df_std = Chara_std(Df, num)

    Df_fre = Chara_fre(Df,date_name1)

    Df_new = pd.concat([Df_mean, Df_count,Df_max,Df_min,Df_std], axis=1)

    Df_new = Df_new.reset_index(drop=True)

    Df_new = pd.concat([Df_new,Delttime,Df_fre,Df_date,Df_medi,Df_meditype['meditype_sum'],Df_meditypefre,Df_FTR_fre,Df_date_fre,Df_FTR_sum],axis=1)  # Df_FTR_No0

    return Df_new
