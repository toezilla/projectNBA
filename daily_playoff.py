import requests
import schedule
import time
import sys
from settings import Settings
from Models import DailyPlayoff


def message():
    print("schedule will be started in one minute...")


def exit():
    print("schedule ends...")
    sys.exit()


def DailyScrap():
    settings = Settings()
    settings.db.create_tables([DailyPlayoff], safe=True)

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    season_segment = 1  # 최근 n경기. 전날 경기 집계를 위해
    per_mode = 'Totals'  # PER 집계방식
    season_id = '2021-22'  # 시즌
    season_type = 'Playoffs'  # 정규시즌(Regular+Season)/플레이오프(Playoffs)/플레이-인 토너먼트(Play-in)/올스타경기(All-Star)

    player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames={}&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode={}&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={}&SeasonSegment=&SeasonType={}&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='.format(
        season_segment, per_mode, season_id, season_type)

    response = requests.get(url=player_info_url, headers=headers).json()
    player_info = response['resultSets'][0]['rowSet']


    for row in player_info:
        player = DailyPlayoff(
            season_id=season_id,
            player_id=row[0],
            player_name=row[1],
            team_id=row[2],
            team_abbreviation=row[3],
            age=row[4],
            gp=row[5],
            w=row[6],
            l=row[7],
            w_pct=row[8],
            min=row[9],
            fgm=row[10],
            fga=row[11],
            fg_pct=row[12],
            fg3m=row[13],
            fg3a=row[14],
            fg3_pct=row[15],
            ftm=row[16],
            fta=row[17],
            ft_pct=row[18],
            oreb=row[19],
            dreb=row[20],
            reb=row[21],
            ast=row[22],
            tov=row[23],
            stl=row[24],
            blk=row[25],
            blka=row[26],
            pf=row[27],
            pfd=row[28],
            pts=row[29],
            plus_minus=row[30],
            nba_fantasy_pts=row[31],
            dd2=row[32],
            td3=row[33],
            gp_rank=row[34],
            w_rank=row[35],
            l_rank=row[36],
            w_pct_rank=row[37],
            min_rank=row[38],
            fgm_rank=row[39],
            fga_rank=row[40],
            fg_pct_rank=row[41],
            fg3m_rank=row[42],
            fg3a_rank=row[43],
            fg3_pct_rank=row[44],
            ftm_rank=row[45],
            fta_rank=row[46],
            ft_pct_rank=row[47],
            oreb_rank=row[48],
            dreb_rank=row[49],
            reb_rank=row[50],
            ast_rank=row[51],
            tov_rank=row[52],
            stl_rank=row[53],
            blk_rank=row[54],
            blka_rank=row[55],
            pf_rank=row[56],
            pfd_rank=row[57],
            pts_rank=row[58],
            plus_minus_rank=row[59],
            nba_fantasy_pts_rank=row[60],
            dd2_rank=row[61],
            td3_rank=row[62],
            cfid=row[63],
            cfparams=row[64])

        player.save()

    print("Done inserting player general traditional season total playoff data to the DB!")


if __name__ == "__main__":
    schedule.every().day.at("14:59").do(message)
    schedule.every().day.at("15:00").do(DailyScrap)
    schedule.every().day.at("15:10").do(exit)

    while True:
        schedule.run_pending()
        time.sleep(1)