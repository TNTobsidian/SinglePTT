print('欢迎使用单曲PTT计算器！算法根据Arcaea Wiki计算。')
ptt = int(input('请输入您的PTT：'))
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
