# encoding: utf-8
print('欢迎使用单曲PTT计算器！算法根据Arcaea Wiki计算。\n更新日期：2020/9/16')
level = input('请输入您的游玩级别（pst,prs,ftr,byd）：[请直接Enter跳过]')
def songchoose():
    if level == 'pst':
        blossoms = int(1)
        fairytale = int(1)
        Utopia_of_Spring = int(1)
        shennaichuan= int(1)
        Paradise = int(1)
        Romance_Wars = int(1)
        Dream_Goes_On = float(1.5)
        dropdead = float(1.5)
        Infinity_Heaven = float(1.5)
        Moonlight_of_Sand_Castle = float(1.5)
        Sayonara_Hatsukoi = float(1.5)
        Antithese = int(2)
        Brand_New_World = int(2)
        xingguance = int(2)
        Evoltex = int(2)
        Flashback = int(2)
        Genesis = int(2)
        AutumnGarden = int(2)
        Impure_Bird = int(2)
        inkarusi = int(2)
        suomi = int(2)
        Vivid_Theory = int(2)
        oneF = float(2.5)
        Altale = float(2.5)
        Anokumene = float(2.5)
        Dandelion = float(2.5)
        Diode = float(2.5)
        Grimheart = float(2.5)
        light = float(2.5)
        LinearAccelerator = float(2.5)
        Lumia = float(2.5)

ptt = int(input('请输入您的PTT[暂时无卵用]：'))
score = int(input('请输入您的单曲成绩（完整成绩）：'))
song = float(input('请输入歌曲定数：'))
def singleptt():
    global singleptt
    if score >=10000000:
        singleptt = song + 2.0
    elif 9800000 <= score < 10000000:
        singleptt = song + 1 + (score - 9800000) / 200000
    elif score < 9800000:
        singleptt = song + (score - 9500000) / 300000
    else:
        print('请您输入正确的成绩/PTT/定数。')
def result():
    if singleptt > 0:
        print('============\n歌曲信息:\n定数：'+str(song)+'\n分数：'+str(score)+'\n============\n您的单曲PTT成绩为：'+str(singleptt)+'\n============')
singleptt()
result()
