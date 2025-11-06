'''创建应用实例'''
import sys
from wxcloudrun import app


if __name__ == '__main__':
    app.run(host=sys.argv[1], port=int(sys.argv[2]))
