from bs4 import BeautifulSoup as bs
import re
import pandas as pd


prod = []
exp = []

def parser():
    soup = bs(open('messages.html','rb').read(),'lxml')

    texts = '\n'.join([i.text for i in soup.find_all('div',class_='text')])
    # for i in texts:
    for i in texts.split('\n'):
        result = re.findall('(#.*?) (.*?)К.*?:(.*)Т.*?: (.*?)\s',i)
        if result == [] and i != '' and i != '       ':

            # print('++++++++++++++++++++++++++++++++++')
            # print(i)
            # print('---------------------------------')
            pass
        elif result != [] and i != '' and i != '       ':
            if 'эксперт' in result[0][0]:
                exp.append(result[0])
            else:
                prod.append(result[0])
    to_csv()
    to_csv2()



    # for i in re.findall('⠀◾️(.*?@)(.*?:).*?(https.*?)⠀',texts):
    #     print(i)
        # print(i.text)
    #     train = (i.text).split(' ')
    #     if 'продюсер' in train[0]:
    #         prod.append(train[0])
    #     elif 'эксперт' in train[0]:
    #         exp.append(train[0])
    #     print(train)
    #     print('******************************************')
    # print(prod)
    # print(exp)

def to_csv():
    frame = pd.DataFrame(columns = ['Prof', 'Name','Instagram','Telegram'])
    for i in range(len(exp)):
        frame.loc[i] = [exp[i][0],exp[i][1],exp[i][2],' '+exp[i][3]]
    frame.to_csv('expert.csv',mode='a',index=False,sep=';',encoding='cp1251',errors='ignore')
def to_csv2():
    frame = pd.DataFrame(columns = ['Prof', 'Name','Instagram','Telegram'])
    for i in range(len(prod)):
        frame.loc[i] = [prod[i][0],prod[i][1],prod[i][2],' '+prod[i][3]]
    frame.to_csv('produser.csv',mode='a',index=False,sep=';',encoding='cp1251',errors='ignore')


if __name__ == '__main__':
    parser()
    # to_csv()