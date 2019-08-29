#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# my assistant
import requests, re, time
robotId = '7138bae6526b0adc5e5730e9678d0ae8a9a23697b32129f94c262f8cbabb360a'

def sendToDingtalk (message):
  requests.post(
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + robotId,
    json = ({ 'msgtype': 'text', 'text': { 'content': message }}),
    headers = { 'Content-Type': 'application/json' }
  )

def getIp ():
  # get public ip(may be I will use my server later)
  req = requests.get('http://aki.waterxp.site/ip')
  ip = req.text if req.ok else 'Warning! It lost.'
  return ip

def schedule (hour):
  # execute when run
  sendIp()
  while True:
    # so next time
    time.sleep(getNextTime(hour))
    sendIp()

def sendIp ():
  gm = 'Good morning! '
  ga = 'Good afternoon! '
  ge = 'Good evening! '
  gn = 'It\'t late at night. '
  tmlist = [
    gn, gn, gn, gn, gn, gm, gm, gm, gm, gm, gm, ga,
    ga, ga, ga, ga, ga, ge, ge, ge, ge, ge, ge, gn
  ]
  sendToDingtalk(tmlist[time.localtime().tm_hour] + 'Boss. Our ip is: ' + getIp() + '.')

def getNextTime (hour, immediately = False):
  targetTime = hour * 3600
  a = time.localtime()
  currentTime = a.tm_hour * 3600 + a.tm_min * 60 + a.tm_sec
  seconds = 86400 + targetTime - currentTime if currentTime > targetTime else targetTime - currentTime
  if (not immediately and seconds == 0):
    seconds = 86400
  return seconds

def main ():
  schedule(8)

main()

# run in back
# nohup python3 assistant.py >/dev/null 2>&1 &
