import pandas as pd 

df1 = pd.DataFrame([  
          ['ABC', 'P1']
        , ['BCD', 'P2']
        , ['CDE', 'P3']
       ]
    ,columns = ['task_name', 'pipeline_name']
)

df2 = pd.DataFrame([  
          ['RR', 'C1']
        , ['BC', 'C2']
        , ['HG', 'C3']
        , ['AB', 'C4']
       ]
    ,columns = ['partial_task_name', 'extra_value']
)

df1['join'] = 1
df2['join'] = 1

dfFull = df1.merge(df2, on='join').drop('join', axis=1)
df2.drop('join', axis=1, inplace=True)

dfFull['match'] = dfFull.apply(lambda x: x.task_name.find(x.partial_task_name), axis=1).ge(0)
dfResult = dfFull.groupby(["task_name", "pipeline_name"]).max().reset_index()[['task_name','pipeline_name','match']]

dfResult[~dfResult['match']][['task_name','pipeline_name']]