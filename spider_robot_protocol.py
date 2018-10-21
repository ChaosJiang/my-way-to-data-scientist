from urllib.robotparser import RobotFileParser
'''

'''
def robot_parse():
    rp = RobotFileParser()
    rp.set_url('http://www.jianshu.com/robots.txt')
    rp.read()

    print(rp.can_fetch('*', 'http://www.jianshu.com/p/'))
    print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
if __name__ == '__main__':
    robot_parse()