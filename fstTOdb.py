# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:49:28 2018

@author: Caden
"""
import re
import os
#函数功能：将fasta格式数据处理成导入数据库的数据格式（@@分割每个蛋白的五种数据；换行符分割蛋白）
def fstClear(fname='C:\\Users\\Caden\\Desktop\\NRProtein.txt',
             targetDir='C:\\',targetName='data.txt'):
    #读取fasta文件
    file=open(fname,'r')
    dataFst=file.read()
    
    #获取ID
    idPt=re.compile(r'[A-Za-z]{2,4}_?[0-9]{1,10}\.[0-9]?')
    id=re.findall(idPt,dataFst)
    
    #获取annotation
    annotPt=re.compile(r'\.[^\n]+\[')
    annot=re.findall(annotPt,dataFst)
    annot=[i[3:len(i)-2] for i in annot]
    
    #获取specie（即[]中的字母）
    spcPt=re.compile(r'\[.{1,40}\]')
    spc=re.findall(spcPt,dataFst)
    spc=[i[1:len(i)-1] for i in spc]
    
    #获取序列
    seqPt=re.compile(r'\][A-Za-z\n]+\n\n')
    seq=re.findall(seqPt,dataFst)
    seq=[i.strip(']').replace('\n','') for i in seq]
    
    #获取序列长度
    length=[len(i) for i in seq]
    
    #生成目标文件,使用@@分割每个蛋白的五种数据；换行符分割蛋白
    data=''
    for i in range(len(annot)):
        data=data+annot[i]+'@@'+id[i]+'@@'+str(length[i])+'@@'+seq[i]+'@@'+spc[i]+'\n'
    #将工作目录设置成C盘根目录下
    os.chdir(targetDir)
    f=open(targetName,'w')
    f.write(data)
    f.close
    
    return len(annot)
    
    
def main():
    #获取用户输入
    fname=input('Please input the fasta file with a absolute path(change \ to \\\)\n>>>')
    targetDir=input('Please input the target directory(change \ to \\\)\n>>>')
    targetName=input('Please input the target name\n>>>')
    #调用函数
    ll=fstClear(fname,targetDir,targetName)
    print('-'*67)
    print('数据转换完成！！！ 共%d行数据。' % ll)
    print('fasta文件来自：',fname)
    print('生成的文件在:',targetDir)
    print('文件名是：',targetName)
    

if __name__=='__main__':
    main()
    