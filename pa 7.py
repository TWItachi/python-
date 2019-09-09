from urllib.robotparser import RobotFileParser
rp = RobotFileParser('http://www.jianshu.com/robot.txt')

rp.read()
print(rp.can_fetch('*', 'https://www.jianshu.com/p/fc1c113e5b6b'))

print(rp.can_fetch('*', "http;//www.jianshu.com/search?q=python&page=1&type=collections"))