import datetime
#preparations:
import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt

#直接读txt看不到各种报错，只能自己下载txt看看表头了，一看好家伙没有表头。
#第一行：H8AK00132|SHEIN, DIMITRI|C|1|DEM|0|0|367.52|0|367.52|0|0|0|0|367.52|0|0|0|AK|00||||||0|0|09/30/2019|0|0
raw_data = pd.read_csv(r'weball20.txt', sep = '|' )

print(raw_data.head())

#其实不是很懂这些数据表示什么，所以只能抄官方文档了：

# 读取候选人信息，由于原始数据没有表头，需要添加表头
raw_candi = pd.read_csv("weball20.txt", sep = '|',names=['CAND_ID','CAND_NAME','CAND_ICI','PTY_CD','CAND_PTY_AFFILIATION','TTL_RECEIPTS',
                                                          'TRANS_FROM_AUTH','TTL_DISB','TRANS_TO_AUTH','COH_BOP','COH_COP','CAND_CONTRIB',
                                                          'CAND_LOANS','OTHER_LOANS','CAND_LOAN_REPAY','OTHER_LOAN_REPAY','DEBTS_OWED_BY',
                                                          'TTL_INDIV_CONTRIB','CAND_OFFICE_ST','CAND_OFFICE_DISTRICT','SPEC_ELECTION','PRIM_ELECTION','RUN_ELECTION'
                                                          ,'GEN_ELECTION','GEN_ELECTION_PRECENT','OTHER_POL_CMTE_CONTRIB','POL_PTY_CONTRIB',
                                                          'CVG_END_DT','INDIV_REFUNDS','CMTE_REFUNDS'])
# 读取候选人和委员会的联系信息
raw_ccl = pd.read_csv("ccl.txt", sep = '|',names=['CAND_ID','CAND_ELECTION_YR','FEC_ELECTION_YR','CMTE_ID','CMTE_TP','CMTE_DSGN','LINKAGE_ID'])

##好像抄了也看不懂简写，不过我确实不怎么懂得美国选举体系，又只能看数据表头解释了
#CMTE_ID：委员会ID / CAND_ID：候选人ID / CAND_NAME：候选人姓名 / CAND_PTY_AFFILIATION：候选人党派

#这边还有个人捐赠数据：
raw_itcont = pd.read_csv(r'itcont_2020_20200722_20200820.txt', sep='|',names=['CMTE_ID','AMNDT_IND','RPT_TP','TRANSACTION_PGI',
                                                                                  'IMAGE_NUM','TRANSACTION_TP','ENTITY_TP','NAME','CITY',
                                                                                  'STATE','ZIP_CODE','EMPLOYER','OCCUPATION','TRANSACTION_DT',
                                                                                  'TRANSACTION_AMT','OTHER_ID','TRAN_ID','FILE_NUM','MEMO_CD',
                                                                                  'MEMO_TEXT','SUB_ID'])

print("read_complete!")

#digesting
#上面的结果表明，两表有同一字段CAND_ID,打算连起来。顺带去掉一点无法分析的数据

ccl = pd.merge(raw_ccl,raw_candi)
ccl = pd.DataFrame(ccl,columns = [ 'CMTE_ID','CAND_ID', 'CAND_NAME','CAND_PTY_AFFILIATION'])
itcont = pd.merge(ccl,raw_itcont)
cc_itcont = pd.DataFrame(itcont,columns = ['CMTE_ID','NAME','STATE','EMPLOYER','OCCUPATION','TRANSACTION_AMT', 'TRANSACTION_DT','CAND_PTY_AFFILIATION'])

#清理NAN：
print(ccl.info(),"\n",itcont.info())
cc_itcont['STATE','EMPLOYER','OCCUPATION'].fillna('?')

cc_itcont['TRANSACTION_DT'] =  datetime.datetime.strptime(cc_itcont['TRANSACTION_DT'] .astype(str),"%d%m%y")



ccl.head(10)
itcont.head(10)

