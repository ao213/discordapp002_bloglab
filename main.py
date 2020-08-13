##ライブラリインポート領域##
import discord
import random
import re
import time
import threading
import datetime
import asyncio
import fibonatti
import os
import subprocess
import schedule
from discord.ext import tasks


##関数領域##
def game1(x): #数当て用関数　エラーは値が入ってないエラーなのでコマンドを送れば問題はない
    
    game1_rand = random.randint(1,100)
    game1_hit = True
    if(game1_rand != x):
        game1_hit = False
    return game1_hit
def theme_get(x): ##テーマを決定するための関数、囲い文字削除と区切りで配列に分ける
    strs = x
    strs = strs.strip('('')')
    themes = strs.split(',')
    return themes

def job_1():#スケジュール用関数
    print('test')
    

def weekperiod():#お題ブログのイベント期間
    aDate = datetime.datetime.today()
    weekday = aDate.weekday()#今日は何曜日？( 月曜日 = 0, 日曜日 = 6 )
    arToWednesday=[0,6,5,4,3,2,1]#次の水曜日までの日数を配列にしておく。先頭が月曜日からの日数を示す
    shiftNum = arToWednesday[weekday]#今日からの日数は？
    delta = datetime.timedelta(days=shiftNum)
    nextDate = aDate + delta
    lastdelta = datetime.timedelta(days=shiftNum + 6)
    lastDate = aDate + lastdelta
    arraypri =[nextDate.strftime('%Y.%m.%d'),lastDate.strftime('%Y.%m.%d')]
    return arraypri


##クラス定義領域##
###変数指定領域###
client = discord.Client()##discordのオブジェクト生成
prefix = '!!'    ##コマンドの頭
member = [] ##メンバーリスト
notoinmess = 'CODMから逃げるな' ##メッセージ
times = [1,60,3600,86400]
#トークン設定#
bot_token = os.environ['DISCORD_BOT_TOKEN']
#embed設定#
embed1 = discord.Embed(title="予定表の提出", description="予定を教えてください。", color=0xff7b7b)

#ループタスク#
@tasks.loop(seconds=30)
async def loop():
    channel_001 = client.get_channel(730484509425926225)
    now = datetime.datetime.now().strftime('%A:%H:%M')
    print(now)
    if now == 'Monday:00:00':
        await channel_001.send(embed=embed_3)
        await asyncio.sleep(60)


@client.event
async def on_ready():
    ###オンライン時の処理##
    ##アクティビティ処理##
    activity = discord.Activity(name = '✧ʕ̢̣̣̣̣̩̩̩̩·͡˔·ོɁ̡̣̣̣̣̩̩̩̩✧',type = discord.ActivityType.playing)
    await client.change_presence(activity=activity)
    print('botはオンライン') ##ターミナル表示##
 
@client.event
#テキストに反応してメッセージを送信するbot
async def on_message(message):
    #API省略定義
    messagecont = message.content
    messagech = message.channel
    messageguil = message.guild
    BANchID = '633845736655814685' #BAN用チャンネルID

    if message.author.bot:
        return 

    if messagecont.startswith(prefix + 'test'):     #テストメッセージ
        print('test')
        await messagech.send('test')

    if messagecont.startswith(prefix + 'DM'):   #DMへメッセージ
        await message.author.send('HI DM')

    if messagecont.startswith(prefix + 'game'): #数当てゲームno1
        Num = int(messagecont[6:])
        game1_ans = game1(Num)
        if(game1_ans == True):
            await messagech.send('HIT!! おめでとう！')
        else:
            await messagech.send('NO HIT! 残念！')

    if messagecont.startswith(prefix + 'getch '): #チャンネルを指定
        global get_channel
        get_ch_id = int(messagecont[10:28])
        get_channel = client.get_channel(get_ch_id)
        await messagech.send('チャンネルを' + messagecont[8:] + 'に指定しました')

    if messagecont.startswith(prefix + 'timemess'): #一定期間メッセージを送る 未完
        
        time_interval = int(messagecont[10:])
        Now_time1 = datetime.datetime.today()
        Now_time2 = datetime.datetime.today()
        End_time = datetime.datetime.today()
        End_time = Now_time1 + datetime.timedelta(minutes=time_interval)
        embed2 = discord.Embed(title="お知らせ", url="https://forms.gle/TgTs2kRdixnDYe49A", description="来週の予定を提出してください", color=0x008080)
        time_flag = True
        i = 0
        
        print(f'test;{End_time.minute}')
        while time_flag:
            i +=1
            print(f'{Now_time1}現在時間')
            print(f'{End_time}終了時間')
            print(f'現在{i}時間経過')
            print('////////////////')
            
            if Now_time1 >= End_time:
                print('終了')
                await get_channel.send(embed=embed1)
                break
            if Now_time1.minute >= Now_time2.minute:
                Now_time2 = Now_time1
                Now_time1 = datetime.datetime.today()
                await get_channel.send(f'このメッセージは{time_interval}分間続きます、{i}分間経過')
                await get_channel.send('!d bump')
            await asyncio.sleep(times[1])
    if messagecont.startswith(prefix + 'memcount'): ##にんずうかぞえてくれるけいだんじｄddddフェjふぃえあ音階ふぁんせあの得あvmあぁ⒡目亜lmふぇいあ⒡時あ⒡なフェア⒡場hfbhbヴぁ；枝折を：pfかpr化：フェ
        count_mem = message.guild.member_count
        await messagech.send(f'{count_mem}人が参加してます')
    if messagecont.startswith(prefix + 'テーマ'):
        strs = messagecont[5:]
        global embed_3
        evetime = weekperiod()
        global embed_3
        themes = theme_get(strs)
        embed_3 = discord.Embed(title="【お知らせ】", description=f"お題ブログを開催します！\n\n期間：{evetime[0]}日から{evetime[1]}日\n提出先：企画シェア\nほかの人の記事へのレビューは、ブログの感想へお願いします。\n\n **お題**", color=0x22bcbf)
        for s in range(0,len(themes)):
            embed_3.add_field(name=s + 1, value=themes[s], inline=True)
        embed_3.set_footer(text="上記のお題の中から最低１つの内容で記事を１つ完成させてください。")
        await messagech.send('以下のように表示されます。')
        await messagech.send(embed=embed_3)
        loop.start()


client.run(bot_token)
