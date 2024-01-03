from django.core.management.base import BaseCommand
from NBA.models import NBATeam, NBAPlayer, Playerscareer, Brands, ProLeague
from datetime import datetime

class Command(BaseCommand):
    help = 'Creates initial data for the application' #<description of the command>"""

    def handle(self, *args, **kwargs):
        self.create_nba_teams() 
        self.create_nba_players()
        self.create_brands()
        self.create_league()
        #self.create_collection()

    def create_nba_teams(self):
        # Create Pokemon Card instances
        team1 = NBATeam(name="Chicago Bulls", years_active="58")

        team2 = NBATeam(name= "Philadelphia Sixers", years_active= "75")

        team3 = NBATeam(name= "Miami Heat", years_active= "36")

        team4 = NBATeam(name= "Minnesota Timberwolves", years_active= "50")

        team5 = NBATeam(name= "Los Angeles Lakers", years_active= "78")

        team6 = NBATeam(name= "Cleveland Cavaliers",years_active= "49")

        team7 = NBATeam(name="Boston Celtics",years_active= "78")

        team8 = NBATeam(name= "Memphis Grizzlies",years_active="29")

        team9 = NBATeam(name="Brooklyn Nets",years_active= "78")

        team10 = NBATeam(name="Phoenix Suns",years_active= "43")

        team11 = NBATeam(name="Oklahoma City Thunder",years_active= "34",)

        team12 = NBATeam(name="Houston Rockets",years_active= "56",)

        team13 = NBATeam(name="Los Angeles Clippers",years_active= "30")

        team14 = NBATeam(name="Washington Wizards",years_active= "65")

        team15 = NBATeam(name="Indiana Pacers",years_active= "55")

        team16 = NBATeam(name="Detroit Pistons",years_active= "70")

        team17 = NBATeam(name="Charlotte Hornets",years_active= "34")

        team18 = NBATeam(name="Denver Nuggets",years_active= "46")

        team19 = NBATeam(name= "New York Knicks",years_active= "73")

        team20 = NBATeam(name= "Atlanta Hawks",years_active= "78")


        nba_teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14, team15, team16, team17, team18, team19, team20]

        for nba_teams in nba_teams:
            nba_teams.save()
            self.stdout.write(self.style.SUCCESS(
                'Successfully create NBA Team.'
            ))

    def create_nba_players(self):
        # bday = datetime.strptime()
        players1 = NBAPlayer(name="Jimmy Butler", birthdate= "1989-09-14",college= "Tyler Junior College") 
        players2 = NBAPlayer(name= "Lebron James",birthdate= "1984-12-30",college= "HS Recruit")
        players3 = NBAPlayer(name="Kyrie Irving",birthdate= "1992-03-23",college= "Duke University")
        players4 = NBAPlayer(name="Kevin Durant",birthdate= "1988-09-29",college= "University")
        players5 = NBAPlayer(name="Russell Westbrook",birthdate= "1988-11-12",college= "Erika University")
        players6 = NBAPlayer(name="James Harden",birthdate= "1989-08-26",college= "Ever Grande University")
        players7 = NBAPlayer(name="D'Angelo Russell",birthdate= "1996-02-23" ,college= "Rustboro University")
        players8 = NBAPlayer(name="Devin Booker" ,birthdate= "1996-10-30" ,college= "Sinoh University")
        players9 = NBAPlayer(name="Tyler Hero",birthdate= "2000-01-20",college= "Buncag University")
        players10 = NBAPlayer(name="Luka Doncic" ,birthdate= "1999-02-28" ,college= "University")
        
        nba_players = [players1, players2, players3, players4, players5, players6, players7, players8, players9, players10]

        for nba_players in nba_players:
            nba_players.save()
            self.stdout.write(self.style.SUCCESS(
                'Successfully create NBA player.'
            ))
            
            
    def create_brands(self):
        # bday = datetime.strptime()
        brand1 = Brands(brand_name="Nike") 
        brand2 = Brands(brand_name= "Adidas")
        brand3 = Brands(brand_name="Rebook")
        brand4 = Brands(brand_name="Under Armour")
        brand5 = Brands(brand_name="Anta")
    
        
        brandss = [brand1, brand2, brand3, brand4, brand5]

        for brandss in brandss:
            brandss.save()
            self.stdout.write(self.style.SUCCESS(
                'Successfully create Brands.'
            ))
    
    def create_league(self):
        # bday = datetime.strptime()
        l1 = ProLeague(name="NBA") 
        l2 = ProLeague(name="NFl")
        
    
        
        league = [l1]

        for league in league:
            league.save()
            self.stdout.write(self.style.SUCCESS(
                'Successfully create Brands.'
            ))







