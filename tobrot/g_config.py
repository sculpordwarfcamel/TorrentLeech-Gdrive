from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1648861366:AAHypiRRn4qIfsCAbR9mWd5KwSDtFu47Eiw"
	APP_ID = 1858153
	API_HASH = "5fb9328cdf9a7aaad5fed030484d6022"
	OWNER_ID = "1196519780" #ID of bot owner
	AUTH_CHANNEL = [-1001277862770]
	DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMANCcYn_2c_I1N6Aylq8JYJin19xw1SurmiXy4ZImlTvgzK1XA2AQZ2tihyNeAMR68FAvw_njwacqQjAHyCAqPP5glNIPts1-YqeLZ7QTi6Oe3IRUuT-6hWs40kcHjg3HmHf8kowlAMa1nqcZ8gI543","token_type":"Bearer","refresh_token":"1//03ZM2101W84YNCgYIARAAGAMSNwF-L9Irx3yxaCOobCV9AbrzSulNkl7jVuDaG3jsZbHXuxvN4XEaqbnlFB-bUgcRy4b3W4Lf8eE","expiry":"2021-03-06T19:43:34.2077008+03:30"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
