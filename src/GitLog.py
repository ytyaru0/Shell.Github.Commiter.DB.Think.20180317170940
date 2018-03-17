import subprocess
import re
class GitLog:
    def __init__(self):
        pass
    def Get(self, username:str):
        command = ""
        command += "cd /tmp/work/Sqlite.Github.Commiter.DB.20180317062806;"
        command += "git log --numstat --date=iso --author='{}';".format(username)
        #print(command)
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data, stderr_data = p.communicate()
        #print(stdout_data.decode('UTF-8'))
        #print(stderr_data.decode('UTF-8'))
        self.__Analize(stdout_data.decode('UTF-8').split('\n'))
    def __Analize(self, stdout):
        # 1commitあたり以下のような書式。これが複数ある。
        """
        commit f132792d261ea41134501b5696a0e4ceaf617657
        Author: ytyaru0 <ytyaru0@outlook.jp>
        Date:   2018-03-16 17:00:13 +0900

            初回コミット

        20	0	.gitignore
        116	0	LICENSE.txt
        65	0	ReadMe.md
        97	0	src/push.sh
        """
        commits = []
        #{'sha':'', 'date':'', 'message':'', 'files':[{'name':'', insertion: 0, deletion: 0}]}
        start_lines = self.__SplitLog(stdout)
        for i, start in enumerate(start_lines):
            commit = {}
            commit['sha'] = stdout[start]
            commit['date'] = stdout[start+2]
            commit['message'] = stdout[start+4]
            
            end = len(stdout)
            if i+1 < len(start_lines): end = start_lines[i+1]
            commit['files'] = self.__GetAmounts(stdout, start, end)
            commits.append(commit)
        #print(commits)
        print('commits:', len(commits))
            
    # '^commit '行を開始行位置としてリストにして返す
    def __SplitLog(self, stdout):
        start_lines = []
        for i, line in enumerate(stdout):
            if line.startswith('commit '): start_lines.append(i)
        return start_lines

    def __GetAmounts(self, stdout, start, end):
        files = []
        for i in range(start+6, end):
            if 0 == len(stdout[i].strip()): continue
            counts = stdout[i].split()
            f = {}
            f['insertions'] = int(counts[0])
            f['deletions'] = int(counts[1])
            f['name'] = counts[2]
            files.append(f)
        return files

        
if __name__ == '__main__':
    GitLog().Get('ytyaru0')
