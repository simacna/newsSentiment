import json
import sys
from watson_developer_cloud import ToneAnalyzerV3
import requests

USERNAME = "a2d61d82-1233-4d72-afe3-5f0aa287460e"
PASSWORD = "QX0z2mntUpKQ"
URL = "https://gateway.watsonplatform.net/tone-analyzer/api"



tone_analyzer = ToneAnalyzerV3(
  version='2017-09-21',
  username=USERNAME,
  password=PASSWORD,
  url=URL
)


 

text = """
The Obama administration approved a $200,000 grant to a group in Sudan with ties to Al Qaeda even though it had been designated a terrorist-financing organization by the U.S. years earlier, a conservative think tank revealed this week. 

Further, an agency official acknowledged the prior administration allowed taxpayer money to flow to the group even after its designation was discovered. 

The 2014 grant to the Islamic Relief Agency, through the U.S. Agency for International Development, was revealed by Sam Westrop of the Middle East Forum in a story for the National Review.

“More stunningly, government officials specifically authorized the release of at least $115,000 of this grant even after learning that it was a designated terror organization,” Westrop wrote in the article. 

USAID has since reviewed its policies, though the Trump administration stressed this all occurred in the Obama years. 
”"""

content_type = 'application/json'

tone = tone_analyzer.tone({"text": text},content_type)

print(json.dumps(tone, indent=2))